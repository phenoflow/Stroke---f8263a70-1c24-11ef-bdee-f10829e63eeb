# Victor W Zhong, Juhaeri Juhaeri, Stephen R Cole, Christian M Shay, Carolyn A Chew-Graham, Penny Gordon-Larsen, Evangelos Kontopantelis, Elizabeth J Mayer-Davis, 2024.

import sys, csv, re

codes = [{"code":"G671100","system":"readv2"},{"code":"1477","system":"readv2"},{"code":"G64..12","system":"readv2"},{"code":"G64z.12","system":"readv2"},{"code":"G679.00","system":"readv2"},{"code":"F23..12","system":"readv2"},{"code":"G65z100","system":"readv2"},{"code":"F23yz00","system":"readv2"},{"code":"F2B0.00","system":"readv2"},{"code":"G6z..00","system":"readv2"},{"code":"G67z.00","system":"readv2"},{"code":"G65z000","system":"readv2"},{"code":"G64z200","system":"readv2"},{"code":"G67..00","system":"readv2"},{"code":"G65zz00","system":"readv2"},{"code":"F2B1.00","system":"readv2"},{"code":"F23..00","system":"readv2"},{"code":"F23y.00","system":"readv2"},{"code":"Gyu6400","system":"readv2"},{"code":"G640000","system":"readv2"},{"code":"G640.00","system":"readv2"},{"code":"F23z.00","system":"readv2"},{"code":"F23y100","system":"readv2"},{"code":"F2Bz.00","system":"readv2"},{"code":"F23y300","system":"readv2"},{"code":"G664.00","system":"readv2"},{"code":"F23y200","system":"readv2"},{"code":"G683.00","system":"readv2"},{"code":"Fyu9000","system":"readv2"},{"code":"G6...00","system":"readv2"},{"code":"Q488.00","system":"readv2"},{"code":"F2By.00","system":"readv2"},{"code":"G67y.00","system":"readv2"},{"code":"G65z.00","system":"readv2"},{"code":"Gyu6.00","system":"readv2"},{"code":"G65y.00","system":"readv2"},{"code":"F11x200","system":"readv2"},{"code":"F2B..00","system":"readv2"},{"code":"G64z.00","system":"readv2"},{"code":"Gyu6A00","system":"readv2"},{"code":"G641.11","system":"readv2"},{"code":"G65..00","system":"readv2"},{"code":"F23..11","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('stroke-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["stroke-cereb---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["stroke-cereb---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["stroke-cereb---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
