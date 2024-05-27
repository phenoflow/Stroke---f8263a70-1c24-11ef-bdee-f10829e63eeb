# Victor W Zhong, Juhaeri Juhaeri, Stephen R Cole, Christian M Shay, Carolyn A Chew-Graham, Penny Gordon-Larsen, Evangelos Kontopantelis, Elizabeth J Mayer-Davis, 2024.

import sys, csv, re

codes = [{"code":"G66..13","system":"readv2"},{"code":"Q200100","system":"readv2"},{"code":"Gyu6G00","system":"readv2"},{"code":"Gyu6F00","system":"readv2"},{"code":"G62..00","system":"readv2"},{"code":"G61X000","system":"readv2"},{"code":"G60X.00","system":"readv2"},{"code":"SN20000","system":"readv2"},{"code":"Gyu6E00","system":"readv2"},{"code":"G66..12","system":"readv2"},{"code":"G66..00","system":"readv2"},{"code":"G61X.00","system":"readv2"},{"code":"G66..11","system":"readv2"},{"code":"G61X100","system":"readv2"},{"code":"L440000","system":"readv2"},{"code":"G6W..00","system":"readv2"},{"code":"G68W.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('stroke-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["stroke-unspecif---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["stroke-unspecif---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["stroke-unspecif---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
