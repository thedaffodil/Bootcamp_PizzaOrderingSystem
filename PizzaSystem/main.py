if __name__=="__main__":
    from tkinter import *
    from tkinter import messagebox
    import csv
    from datetime import datetime
    import Pizza
    import Decorator


    #pizza tabanlarını tanımla
    klasik=Pizza.Klasik()
    klasik_info=klasik.get_description()
    klasik_fiyat=klasik.get_cost()


    margarita=Pizza.Margarita()
    margarita_info=margarita.get_description()
    margarita_fiyat=margarita.get_cost()

    ince=Pizza.Ince()
    ince_info=ince.get_description()
    ince_fiyat=ince.get_cost()

    #sosları tanımla

    zeytin=Decorator.Zeytin()
    zeytin_info=zeytin.get_description()
    zeytin_fiyat=zeytin.get_cost()


    mantar=Decorator.Mantar()
    mantar_info=mantar.get_description()
    mantar_fiyat=mantar.get_cost()


    sogan=Decorator.Sogan()
    sogan_info=sogan.get_description()
    sogan_fiyat=sogan.get_cost()


    #listeden pizza tabanı ve sos seç
    def add_pizza():
        result=""
        for i in pizza_list.curselection():
            result=result+str(pizza_list.get(i))+"\n"

            add_lbl.config(text="Tercihiniz: "+"\n"+result)

    def add_extra():
        result=""
        for i in extra_list.curselection():
            result=result+str(extra_list.get(i))+"\n"

            add_lbl1.config(text="Tercihiniz: "+"\n"+result)

    #seçilen ürünlerin fiyatlarını topla
    def sum():
        sum1=0
        sum2=0
        
        if str(pizza_list.get(0))=="Margarita":
                sum1=sum1+margarita_fiyat
        elif str(pizza_list.get(0))=="Klasik":
                sum1=sum1+klasik_fiyat
        elif str(pizza_list.get(0))=="İnce":
                sum1=sum1+ince_fiyat

        for i in extra_list.curselection():
            if str(extra_list.get(i))=="Zeytin":
                sum2=sum2+zeytin_fiyat
            elif str(extra_list.get(i))=="Mantar":
                sum2=sum2+mantar_fiyat
            elif str(extra_list.get(i))=="Soğan":
                sum2=sum2+sogan_fiyat
        
        return sum1+sum2

    #ödemeden önce kontrol et      

    def check():
        text1=name_entry.get()
        new_lbl=Label(pizza,text="Name: "+text1)
        new_lbl.grid(row=18,column=0)

        text2=TCno_entry.get()
        new_lbl2=Label(pizza,text="TC No: "+text2)
        new_lbl2.grid(row=19,column=0)

        text3=card_entry.get()
        new_lbl3=Label(pizza,text="CreditCard No: "+text3)
        new_lbl3.grid(row=20,column=0)

        text4=TCno_entry.get()
        new_lbl4=Label(pizza,text="Password: "+text4)
        new_lbl4.grid(row=21,column=0)

        text5=str(sum())
        new_lbl5=Label(pizza,text="Toplam Tutar: "+text5)
        new_lbl5.grid(row=22,column=0)

        
    #ödeme yapıldığı an DB'ye bilgilerin kaydı yapılır
    def addDB():
        name=name_entry.get()
        tc=TCno_entry.get()
        card=card_entry.get()
        password=TCno_entry.get()
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        DBList=[name,tc,card,password,str(sum()),dt_string]
        
        with open('Orders_Database.csv', 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(DBList)

    #uygulamayı kapa
    def closeApp():
        answer=messagebox.askyesno("Çıkmak istediğinize emin misiniz?")
        if answer==1:
            pizza.destroy()
        else:
            return





    pizza=Tk()
    pizza.geometry("1600x1600")
    pizza.title("Pizza Ordering")

    name_label=Label(pizza,text="Name:")
    name_label.grid(row=0,column=0)
    name_entry=Entry(pizza, width=30)
    name_entry.grid(row=0,column=1)

    TCno_label=Label(pizza,text="TC:")
    TCno_label.grid(row=1,column=0)
    TCno_entry=Entry(pizza, width=30)
    TCno_entry.grid(row=1,column=1)

    card_label=Label(pizza,text="CreditCard No:")
    card_label.grid(row=2,column=0)
    card_entry=Entry(pizza, width=30)
    card_entry.grid(row=2,column=1)

    password_label=Label(pizza,text="Password:")
    password_label.grid(row=3,column=0)
    password_entry=Entry(pizza, width=30)
    password_entry.grid(row=3,column=1)


    #menüyü oluşutr
    choose_label1=Label(pizza,text="Pizza Tabanı Seçiniz")
    choose_label1.grid(row=5,column=1)
    pizzas=["Klasik","Margarita","İnce"]
    pizza_list=Listbox(pizza)
    pizza_list.grid(row=6,column=1)

    for i in pizzas:
        pizza_list.insert(0,i)

    add_button=Button(pizza,text="Pizza Tabanı Ekle Ekle",command=add_pizza)
    add_button.grid(row=7,column=1)
    add_lbl=Label(pizza,text="")
    add_lbl.grid(row=8,column=1)



    choose_label2=Label(pizza,text="Extraları Seçiniz(Birden fazla seçilebilir)")
    choose_label2.grid(row=5,column=2)

    extras=["Zeytin","Mantar","Soğan"]
    extra_list=Listbox(pizza,selectmode=MULTIPLE)
    extra_list.grid(row=6,column=2)

    for i in extras:
        extra_list.insert(0,i)

    add_button2=Button(pizza,text="Extra Ekle",command=add_extra)
    add_button2.grid(row=7,column=2)
    add_lbl1=Label(pizza,text="")
    add_lbl1.grid(row=8,column=2)




    check_button=Button(pizza,text="Kontrol Et",command=check)
    check_button.grid(row=17,column=0)


    pay_button=Button(pizza,text="Öde",command=addDB)
    pay_button.grid(row=23,column=0)


    exit_button=Button(pizza,text="Çıkış",command=closeApp)
    exit_button.grid(row=24,column=0)

    pizza.mainloop()