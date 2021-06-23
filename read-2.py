def read_file(filename):
    lines = []
    with open(filename,'r',encoding = 'utf-8-sig') as f :
    	for line in f :
    		lines.append(line.strip())
    return lines

def convert(lines):
    
    person = None
    Allen_word_count = 0
    Allen_sticker_count = 0
    Allen_image_count = 0
    Viki_word_count = 0
    Viki_sticker_count = 0 
    Viki_image_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0] 
        name = s[1] 
        if name =='Allen' :
            if s[2] == '貼圖' :
                Allen_sticker_count += 1
            elif s[2] =='圖片' :
                Allen_image_count +=1
            else :
                for message in s[2:] :
                    Allen_word_count += len(message) 

        elif name =='Viki' :
            if s[2] == '貼圖' :
               Viki_sticker_count += 1
            elif s[2] =='圖片' :
                Viki_image_count +=1 
            else :
                for message in s[2:] :
                    Viki_word_count += len(message)

    print('Allen 總共說了' , Allen_word_count , '字數')
    print(Allen_sticker_count , '個貼圖')
    print(Allen_image_count , '張圖片')
    print('Viki 總共說了' , Viki_word_count , '字數')
    print(Viki_sticker_count , '個貼圖')
    print(Viki_image_count , '張圖片')

        #print(s)
 
        
def write_file(filename , lines):
    with open(filename,'w') as f :
        for line in lines :
            f.write(line + '\n')

def main():   
    lines = read_file('LINE-Viki.txt')
    lines = convert(lines)
    #write_file('output.txt' , lines)
    
main()




