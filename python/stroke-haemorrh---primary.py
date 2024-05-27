# Victor W Zhong, Juhaeri Juhaeri, Stephen R Cole, Christian M Shay, Carolyn A Chew-Graham, Penny Gordon-Larsen, Evangelos Kontopantelis, Elizabeth J Mayer-Davis, 2024.

import sys, csv, re

codes = [{"code":"Q200011","system":"readv2"},{"code":"G60..00","system":"readv2"},{"code":"G613.00","system":"readv2"},{"code":"G615.00","system":"readv2"},{"code":"S621.00","system":"readv2"},{"code":"G614.00","system":"readv2"},{"code":"G602.00","system":"readv2"},{"code":"G618.00","system":"readv2"},{"code":"G616.00","system":"readv2"},{"code":"S62..12","system":"readv2"},{"code":"G610.00","system":"readv2"},{"code":"Q200012","system":"readv2"},{"code":"G682.00","system":"readv2"},{"code":"S622.00","system":"readv2"},{"code":"G603.00","system":"readv2"},{"code":"Gyu6000","system":"readv2"},{"code":"G681.00","system":"readv2"},{"code":"G61..11","system":"readv2"},{"code":"S627.00","system":"readv2"},{"code":"G62z.00","system":"readv2"},{"code":"S623.00","system":"readv2"},{"code":"G623.00","system":"readv2"},{"code":"G61..12","system":"readv2"},{"code":"Q412.00","system":"readv2"},{"code":"G604.00","system":"readv2"},{"code":"G605.00","system":"readv2"},{"code":"G61..00","system":"readv2"},{"code":"S620.00","system":"readv2"},{"code":"S62..13","system":"readv2"},{"code":"Q412000","system":"readv2"},{"code":"G617.00","system":"readv2"},{"code":"G601.00","system":"readv2"},{"code":"S628.00","system":"readv2"},{"code":"Gyu6200","system":"readv2"},{"code":"G680.00","system":"readv2"},{"code":"Gyu6100","system":"readv2"},{"code":"G61z.00","system":"readv2"},{"code":"G621.00","system":"readv2"},{"code":"G60z.00","system":"readv2"},{"code":"G606.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('stroke-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["stroke-haemorrh---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["stroke-haemorrh---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["stroke-haemorrh---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
