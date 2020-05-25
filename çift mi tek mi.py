print("\nBu program sayının tek mi çift mi olduğunu açıklar") 
while True: #Bir döngü oluşturur.
	sayı = input("\n\nSayıyı giriniz: ") #Girmen için bir sayı ister.
	if int(sayı) < 0:  #Eğer sayı 0dan küçükse
		print("\nNegatif sayı girmeyiniz!!") #Negatif sayı girmeyiniz!! yazdırır

	elif int(sayı) % 2 == 0 #eğer sayı 2ye bölündüğünde kalan 0 ise
		print("\nSayı çifttir") #Sayı çifttir
  
        else: #Değilse
                print("\nSayı tektir.") #Sayı tektir
		



	

