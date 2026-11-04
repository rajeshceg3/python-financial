#!/usr/bin/env python3
import argparse,contextlib,datetime,io,json,math,os,pathlib,runpy,sys
root=pathlib.Path(__file__).resolve().parents[4]
p=argparse.ArgumentParser();p.add_argument('mode',choices=['doctor','drive']);p.add_argument('--out',default='.verification-evidence');a=p.parse_args();out=pathlib.Path(a.out).resolve();out.mkdir(parents=True,exist_ok=True)
os.environ['MPLBACKEND']='Agg';r={'mode':a.mode,'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'ok':False,'steps':[]}
try:
 import numpy as np,pandas as pd,matplotlib.pyplot as plt,seaborn,statsmodels
 assert (root/'health.csv').is_file(),'Wrong repository'
 r['versions']={n:m.__version__ for n,m in [('numpy',np),('pandas',pd),('statsmodels',statsmodels)]}
 for path in root.glob('*.ipynb'):
  notebook=json.loads(path.read_text());assert isinstance(notebook['cells'],list);assert not __import__('re').search(r'(?:TimeSeries|CryptoCurrencies)\([\'\"]?[A-Z0-9]{16}', ''.join(''.join(c.get('source',[])) for c in notebook['cells'])), 'Credential-like provider literal in source';r['steps'].append({'notebook':path.name,'cells':len(notebook['cells']),'parsed_only':True})
 if a.mode=='drive':
  old=os.getcwd()
  try:
   os.chdir(root);stdout=io.StringIO()
   with contextlib.redirect_stdout(stdout):data=runpy.run_path(str(root/'linear_regression.py'))
   df=pd.read_csv(root/'health.csv');expected=df.workout.corr(df.points);actual=float(stdout.getvalue().strip());assert math.isclose(actual,expected,abs_tol=1e-12)
   fit=data['result'];assert math.isfinite(float(fit.rsquared)) and len(fit.params)==2
   plt.gcf().savefig(out/'regression.png');plt.close('all');r['steps'].append({'source':'linear_regression.py','rows':len(df),'correlation':actual,'r_squared':float(fit.rsquared),'parameters':fit.params.to_dict()})
   example=runpy.run_path(str(root/'np_normal_distribution.py'));sample=example['s'];assert len(sample)==1000 and np.isfinite(sample).all();plt.gcf().savefig(out/'distribution.png');plt.close('all');r['steps'].append({'source':'np_normal_distribution.py','finite_samples':len(sample),'deterministic_mean_claim':False})
  finally:os.chdir(old);plt.close('all')
 r['ok']=True
except Exception as e:r['failure']=str(e)
(out/(a.mode+'.json')).write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2));raise SystemExit(0 if r['ok'] else 1)
