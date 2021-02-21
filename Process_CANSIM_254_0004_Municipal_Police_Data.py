import os
import petl
import logging as log


log.basicConfig(level=os.environ.get("LOGLEVEL","INFO"))

inputFile='./35100077.csv'
try:
    cansimData = petl.fromcsv(inputFile)

except Exception as e:
    log.error(e)

cansimData = petl.cut(cansimData,0,'GEO','DGUID','Statistics','VALUE')

outputData = petl.recast(cansimData,variablefield='Statistics',valuefield='VALUE')
petl.io.csv.tocsv(outputData,'output.csv')