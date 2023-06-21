from datetime import datetime

file = open('HIST_012022_002_2_sch.inc', 'r')

date_section = False

well_section = False

start_parse = False

date = None

result = {}

line: str
for line in file:
    line = line.rstrip()
    
    if line.startswith('DATES'):
        start_parse = True
    elif start_parse:
        if not date_section and line.endswith('/'):
            date = line.removesuffix('/').rstrip()
            date = datetime.strptime(date, '%d %b %Y').strftime('%d.%m.%Y')
            date_section = True
            
        elif line.startswith('WCONHIST'):
            well_section = True
            
        elif line.startswith('/') and well_section:
            date_section = False
            start_parse = False
            well_section = False
        
        elif well_section and line.endswith('/'):
            line = line.removesuffix('/').rstrip()
            
            data = line.split()
            
            if len(data) < 8:
                continue

            year: str = data[0].replace("'", '')
            
            if not year.isnumeric():
                continue
            
            if date in result.keys():
                result[date][year] = (data[4], data[7])
            else:
                result[date] = {}
                result[date][year] = (data[4], data[7])
                
file.close()

print(result)