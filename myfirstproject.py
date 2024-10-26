i = int(input('Makanan apa yang ingin kamu pesan? \n 1. roti \n 2. nasi \n 3. wafer \n 4. nugget \n 5. keluar \n Masukkan angka: '))

if (i == 1):
    print('roti sedang dibuat')
elif (i == 2):
    print('nasi sedang di masak')
elif (i == 3):
    print('wafer habis')
elif (i == 4):
    print('nugget sedang digoreng')
else:
    print('angka tidak terverifikasi')
    
    
while(i != 5):
    i = int(input('Makanan apa yang ingin kamu pesan? \n 1. roti \n 2. nasi \n 3. wafer \n 4. nugget \n 5. keluar \n Masukkan angka: '))
    print('terimakasih sudah berkunjung')
    