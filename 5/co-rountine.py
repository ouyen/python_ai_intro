
import asyncio
import time
import csv

async def readfile(file='IBM_2006-01-01_to_2018-01-01.csv'):
    # TODO
    odd_lines=[]
    with open(file,'r') as f:
        i=0
        for line in f:
            i+=1
            if i%2:
                odd_lines.append(line)
    return odd_lines
            

async def writefile(lines,file='new.csv'):
    # TODO
    with open(file,'w') as f:
        f.writelines(lines)

async def main():
    print(f"start at {time.strftime('%X')}")
    # TODO
    odd_lines=await readfile()
    await writefile(odd_lines)
    print(f"finish at {time.strftime('%X')}")
          
asyncio.run(main())
          
