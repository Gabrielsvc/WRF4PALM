import pandas as pd
import pdb
import sys


df = pd.read_table(sys.argv[1], '\\s+', skiprows=3, header=None,
                   names = ['Name', 'Version', 'Build', 'Channel'])
env = df.Name + '=' + df.Version
env.to_csv('environment.yml', header=False, index=False)
