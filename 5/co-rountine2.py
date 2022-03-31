import asyncio
import time
import csv

async def readfile(file):
    with open(file,'r') as f:
        lines=f.readlines()
    return lines
            

async def writefile(lines,file='combine.csv'):
    with open(file,'a') as f:
        f.writelines(lines)

async def main():
    print(f"start at {time.strftime('%X')}")
    lines_IBM=await readfile('IBM_2006-01-01_to_2018-01-01.csv')
    lines_AMZN=await readfile('AMZN_2006-01-01_to_2018-01-01.csv')
    await writefile(lines_IBM+lines_AMZN)
    print(f"finish at {time.strftime('%X')}")
          
asyncio.run(main())
