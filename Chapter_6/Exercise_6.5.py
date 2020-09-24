str='X=DSPAM-Confidence:0.8475'
pos=str.find('0')
print(float((str[pos:pos+6])))
