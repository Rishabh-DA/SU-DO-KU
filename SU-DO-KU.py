from tkinter import *
from tkinter import messagebox


root = Tk()
root.title('SU-DO-KU')

def submit():
    global f
    global s
    global t
    global fo
    global fi
    global si
    global se
    global e
    global n
    c1=[f[0].get(),s[0].get(),t[0].get(),fo[0].get(),fi[0].get(),si[0].get(),se[0].get(),e[0].get(),n[0].get()]
    c2=[f[1].get(),s[1].get(),t[1].get(),fo[1].get(),fi[1].get(),si[1].get(),se[1].get(),e[1].get(),n[1].get()]
    c3=[f[2].get(),s[2].get(),t[2].get(),fo[2].get(),fi[2].get(),si[2].get(),se[2].get(),e[2].get(),n[2].get()]
    c4=[f[3].get(),s[3].get(),t[3].get(),fo[3].get(),fi[3].get(),si[3].get(),se[3].get(),e[3].get(),n[3].get()]
    c5=[f[4].get(),s[4].get(),t[4].get(),fo[4].get(),fi[4].get(),si[4].get(),se[4].get(),e[4].get(),n[4].get()]
    c6=[f[5].get(),s[5].get(),t[5].get(),fo[5].get(),fi[5].get(),si[5].get(),se[5].get(),e[5].get(),n[5].get()]
    c7=[f[6].get(),s[6].get(),t[6].get(),fo[6].get(),fi[6].get(),si[6].get(),se[6].get(),e[6].get(),n[6].get()]
    c8=[f[7].get(),s[7].get(),t[7].get(),fo[7].get(),fi[7].get(),si[7].get(),se[7].get(),e[7].get(),n[7].get()]
    c9=[f[8].get(),s[8].get(),t[8].get(),fo[8].get(),fi[8].get(),si[8].get(),se[8].get(),e[8].get(),n[8].get()]

    r1=[]
    r2=[]
    r3=[]
    r4=[]
    r5=[]
    r6=[]
    r7=[]
    r8=[]
    r9=[]
    for i in range(0,9):
        r1.append(f[i].get())
        r2.append(s[i].get())
        r3.append(t[i].get())
        r4.append(fo[i].get())
        r5.append(fi[i].get())
        r6.append(si[i].get())
        r7.append(se[i].get())
        r8.append(e[i].get())
        r9.append(n[i].get())

    for i in range(0,9):
        h=0
        if c1[i]=='' or (int(c1[i])>9 or int(c1[i])<1):
            messagebox.showinfo('invalid','INVALID ENTRY IN COLUMN 1')
            h=1
            break
        if c2[i]=='' or (int(c2[i])>9 or int(c2[i])<1):
            messagebox.showinfo('invalid','INVALID ENTRY IN COLUMN 2')
            h=1
            break
        if c3[i]=='' or (int(c3[i])>9 or int(c3[i])<1):
            messagebox.showinfo('invalid','INVALID ENTRY IN COLUMN 3')
            h=1
            break
        if c4[i]=='' or (int(c4[i])>9 or int(c4[i])<1):
            messagebox.showinfo('invalid','INVALID ENTRY IN COLUMN 4')
            h=1
            break
        if c5[i]=='' or (int(c5[i])>9 or int(c5[i])<1):
            messagebox.showinfo('invalid','INVALID ENTRY IN COLUMN 5')
            h=1
            break
        if c6[i]=='' or (int(c6[i])>9 or int(c6[i])<1):
            messagebox.showinfo('invalid','INVALID ENTRY IN COLUMN 6')
            h=1
            break
        if c7[i]=='' or (int(c7[i])>9 or int(c7[i])<1):
            messagebox.showinfo('invalid','INVALID ENTRY IN COLUMN 7')
            h=1
            break
        if c8[i]=='' or (int(c8[i])>9 or int(c8[i])<1):
            messagebox.showinfo('invalid','INVALID ENTRY IN COLUMN 8')
            h=1
            break
        if c9[i]=='' or (int(c9[i])>9 or int(c9[i])<1):
            messagebox.showinfo('invalid','INVALID ENTRY IN COLUMN 9')
            h=1
            break





    for i in range(0,9):
        g=0
        if c1.count(c1[i])>1 or r1.count(r1[i])>1:
            messagebox.showerror('wrong','not completed,repeated number in column 1 or row 1')
            g=1
            break
        if c2.count(c2[i])>1 or r2.count(r2[i])>1:
            messagebox.showerror('wrong','not completed,repeated number in column 2 or row 2')
            g=1
            break
        if c3.count(c3[i])>1 or r3.count(r3[i])>1:
            messagebox.showerror('wrong','not completed,repeated number in column 3 or row 3')
            g=1
            break
        if c4.count(c4[i])>1 or r4.count(r4[i])>1:
            messagebox.showerror('wrong','not completed,repeated number in column 4 or row 4')
            g=1
            break
        if c5.count(c5[i])>1 or r5.count(r5[i])>1:
            messagebox.showerror('wrong','not completed,repeated number in column 5 or row 5')
            g=1
            break
        if c6.count(c6[i])>1 or r6.count(r6[i])>1:
            messagebox.showerror('wrong','not completed,repeated number in column 6 or row 6')
            g=1
            break
        if c7.count(c7[i])>1 or r7.count(r7[i])>1:
            messagebox.showerror('wrong','not completed,repeated number in column 7 or row 7')
            g=1
            break
        if c8.count(c8[i])>1 or r8.count(r8[i])>1:
            messagebox.showerror('wrong','not completed,repeated number in column 8 or row 8')
            g=1
            break
        if c9.count(c9[i])>1 or r9.count(r9[i])>1:
            messagebox.showerror('wrong','not completed,repeated number in column 9 or row 9')
            g=1
            break

    if g==0 and h==0:
        messagebox.showinfo('correct','YOU WON!! CONGRATS')


def easy_level():
    easy.destroy()
    medium.destroy()
    hard.destroy()
    evil.destroy()
    global f
    f=['f1','f2','f3','f4','f5','f6','f7','f8','f9']
    for i in range(0,9):
        f[i]=Entry(root,relief=RAISED,width=10,justify=CENTER,font='Times 17 bold')
        f[i].grid(row=1,column=i,sticky=W,ipady=10)
        if i <= 2 or i>=6:
            f[i]['background']='light goldenrod'
    f[1].insert(0,7)
    f[1]['state']=DISABLED
    f[1].config(disabledbackground='light goldenrod',disabledforeground='blue')
    f[3].insert(0,4)
    f[3]['state']=DISABLED
    f[3].config(disabledbackground='white',disabledforeground='blue')
    f[5].insert(0,5)
    f[5]['state']=DISABLED
    f[5].config(disabledbackground='white',disabledforeground='blue')
    f[6].insert(0,6)
    f[6]['state']=DISABLED
    f[6].config(disabledbackground='light goldenrod',disabledforeground='blue')

    global s
    s=['s1','s2','s3','s4','s5','s6','s7','s8','s9']
    for i in range(0,9):
        s[i]=Entry(root,relief=RAISED,width=10,justify=CENTER,font='Times 17 bold')
        s[i].grid(row=2,column=i,sticky=W,ipady=10)
        if i <= 2 or i>=6:
            s[i]['background']='light goldenrod'
    s[0].insert(0,9)
    s[0]['state']=DISABLED
    s[0].config(disabledbackground='light goldenrod',disabledforeground='blue')
    s[1].insert(0,2)
    s[1]['state']=DISABLED
    s[1].config(disabledbackground='light goldenrod',disabledforeground='blue')
    s[2].insert(0,4)
    s[2]['state']=DISABLED
    s[2].config(disabledbackground='light goldenrod',disabledforeground='blue')
    s[4].insert(0,6)
    s[4]['state']=DISABLED
    s[4].config(disabledbackground='white',disabledforeground='blue')
    s[6].insert(0,8)
    s[6]['state']=DISABLED
    s[6].config(disabledbackground='light goldenrod',disabledforeground='blue')

    global t
    t=['t1','t2','t3','t4','t5','t6','t7','t8','t9']
    for i in range(0,9):
        t[i]=Entry(root,relief=RAISED,width=10,justify=CENTER,font='Times 17 bold')
        t[i].grid(row=3,column=i,sticky=W,ipady=10)
        if i <= 2 or i>=6:
            t[i]['background']='light goldenrod'
    t[0].insert(0,1)
    t[0]['state']=DISABLED
    t[0].config(disabledbackground='light goldenrod',disabledforeground='blue')
    t[2].insert(0,5)
    t[2]['state']=DISABLED
    t[2].config(disabledbackground='light goldenrod',disabledforeground='blue')
    t[5].insert(0,8)
    t[5]['state']=DISABLED
    t[5].config(disabledbackground='white',disabledforeground='blue')
    t[6].insert(0,7)
    t[6]['state']=DISABLED
    t[6].config(disabledbackground='light goldenrod',disabledforeground='blue')

    global fo
    fo=['fo1','fo2','fo3','fo4','fo5','fo6','fo7','fo8','fo9']

    for i in range(0,9):
        fo[i]=Entry(root,relief=RAISED,width=10,justify=CENTER,font='Times 17 bold')
        fo[i].grid(row=4,column=i,sticky=W,ipady=10)
        if i>=3 and i<=5:
            fo[i]['background']='light goldenrod'
    fo[1].insert(0,3)
    fo[1]['state']=DISABLED
    fo[1].config(disabledbackground='white',disabledforeground='blue')

    fo[2].insert(0,8)
    fo[2]['state']=DISABLED
    fo[2].config(disabledbackground='white',disabledforeground='blue')

    fo[4].insert(0,5)
    fo[4]['state']=DISABLED
    fo[4].config(disabledbackground='light goldenrod',disabledforeground='blue')

    fo[5].insert(0,7)
    fo[5]['state']=DISABLED
    fo[5].config(disabledbackground='light goldenrod',disabledforeground='blue')

    global fi
    fi=['fi1','fi2','fi3','fi4','fi5','fi6','fi7','fi8','fi9']
    for i in range(0,9):
        fi[i]=Entry(root,relief=RAISED,width=10,justify=CENTER,font='Times 17 bold')
        fi[i].grid(row=5,column=i,sticky=W,ipady=10)
        if i>=3 and i<=5:
            fi[i]['background']='light goldenrod'
    fi[8].insert(0,3)
    fi[8]['state']=DISABLED
    fi[8].config(disabledbackground='white',disabledforeground='blue')

    fi[7].insert(0,7)
    fi[7]['state']=DISABLED
    fi[7].config(disabledbackground='white',disabledforeground='blue')

    global si
    si=['si1','si2','si3','si4','si5','si6','si7','si8','si9']
    for i in range(0,9):
        si[i]=Entry(root,relief=RAISED,width=10,justify=CENTER,font='Times 17 bold')
        si[i].grid(row=6,column=i,sticky=W,ipady=10)
        if i>=3 and i<=5:
            si[i]['background']='light goldenrod'
    si[1].insert(0,4)
    si[1]['state']=DISABLED
    si[1].config(disabledbackground='white',disabledforeground='blue')
    si[2].insert(0,7)
    si[2]['state']=DISABLED
    si[2].config(disabledbackground='white',disabledforeground='blue')
    si[4].insert(0,9)
    si[4]['state']=DISABLED
    si[4].config(disabledbackground='light goldenrod',disabledforeground='blue')
    si[6].insert(0,1)
    si[6]['state']=DISABLED
    si[6].config(disabledbackground='white',disabledforeground='blue')
    si[7].insert(0,2)
    si[7]['state']=DISABLED
    si[7].config(disabledbackground='white',disabledforeground='blue')

    global se
    se=['se1','se2','se3','se4','se5','se6','se7','se8','se9']
    for i in range(0,9):
        se[i]=Entry(root,relief=RAISED,width=10,justify=CENTER,font='Times 17 bold')
        se[i].grid(row=7,column=i,sticky=W,ipady=10)
        if i <= 2 or i>=6:
            se[i]['background']='light goldenrod'
    se[0].insert(0,4)
    se[0]['state']=DISABLED
    se[0].config(disabledbackground='light goldenrod',disabledforeground='blue')
    se[2].insert(0,9)
    se[2]['state']=DISABLED
    se[2].config(disabledbackground='light goldenrod',disabledforeground='blue')
    se[3].insert(0,6)
    se[3]['state']=DISABLED
    se[3].config(disabledbackground='white',disabledforeground='blue')
    se[5].insert(0,2)
    se[5]['state']=DISABLED
    se[5].config(disabledbackground='white',disabledforeground='blue')
    se[8].insert(0,1)
    se[8]['state']=DISABLED
    se[8].config(disabledbackground='light goldenrod',disabledforeground='blue')

    global e
    e=['e1','e2','e3','e4','e5','e6','e7','e8','e9']
    for i in range(0,9):
        e[i]=Entry(root,relief=RAISED,width=10,justify=CENTER,font='Times 17 bold')
        e[i].grid(row=8,column=i,sticky=W,ipady=10)
        if i <= 2 or i>=6:
            e[i]['background']='light goldenrod'
    e[0].insert(0,7)
    e[0]['state']=DISABLED
    e[0].config(disabledbackground='light goldenrod',disabledforeground='blue')
    e[3].insert(0,8)
    e[3]['state']=DISABLED
    e[3].config(disabledbackground='white',disabledforeground='blue')
    e[4].insert(0,3)
    e[4]['state']=DISABLED
    e[4].config(disabledbackground='white',disabledforeground='blue')
    e[6].insert(0,4)
    e[6]['state']=DISABLED
    e[6].config(disabledbackground='light goldenrod',disabledforeground='blue')
    e[8].insert(0,9)
    e[8]['state']=DISABLED
    e[8].config(disabledbackground='light goldenrod',disabledforeground='blue')

    global n
    n=['n1','n2','n3','n4','n5','n6','n7','n8','n9']
    for i in range(0,9):
        n[i]=Entry(root,relief=RAISED,width=10,justify=CENTER,font='Times 17 bold')
        n[i].grid(row=9,column=i,sticky=W,ipady=10)
        if i <= 2 or i>=6:
            n[i]['background']='light goldenrod'
    n[1].insert(0,1)
    n[1]['state']=DISABLED
    n[1].config(disabledbackground='light goldenrod',disabledforeground='blue')
    n[3].insert(0,5)
    n[3]['state']=DISABLED
    n[3].config(disabledbackground='white',disabledforeground='blue')
    n[4].insert(0,4)
    n[4]['state']=DISABLED
    n[4].config(disabledbackground='white',disabledforeground='blue')
    n[5].insert(0,9)
    n[5]['state']=DISABLED
    n[5].config(disabledbackground='white',disabledforeground='blue')

    sub = Button(root,text='submit',command=submit)
    sub.grid(row=10,column=8,pady=10,columnspan=2)

def medium_level():
    easy.destroy()
    medium.destroy()
    hard.destroy()
    evil.destroy()
    global f
    f=['f1','f2','f3','f4','f5','f6','f7','f8','f9']
    for i in range(0,9):
        f[i]=Entry(root,relief=RAISED,width=10,justify=CENTER,font='Times 17 bold')
        f[i].grid(row=1,column=i,sticky=W,ipady=10)
        if i <= 2 or i>=6:
            f[i]['background']='light goldenrod'
    f[7].insert(0,3)
    f[7]['state']=DISABLED
    f[7].config(disabledbackground='light goldenrod',disabledforeground='blue')
    f[8].insert(0,1)
    f[8]['state']=DISABLED
    f[8].config(disabledbackground='light goldenrod',disabledforeground='blue')

    global s
    s=['s1','s2','s3','s4','s5','s6','s7','s8','s9']
    for i in range(0,9):
        s[i]=Entry(root,relief=RAISED,width=10,justify=CENTER,font='Times 17 bold')
        s[i].grid(row=2,column=i,sticky=W,ipady=10)
        if i <= 2 or i>=6:
            s[i]['background']='light goldenrod'
    s[0].insert(0,1)
    s[0]['state']=DISABLED
    s[0].config(disabledbackground='light goldenrod',disabledforeground='blue')
    s[1].insert(0,6)
    s[1]['state']=DISABLED
    s[1].config(disabledbackground='light goldenrod',disabledforeground='blue')
    s[5].insert(0,4)
    s[5]['state']=DISABLED
    s[5].config(disabledbackground='white',disabledforeground='blue')
    s[4].insert(0,3)
    s[4]['state']=DISABLED
    s[4].config(disabledbackground='white',disabledforeground='blue')
    s[7].insert(0,9)
    s[7]['state']=DISABLED
    s[7].config(disabledbackground='light goldenrod',disabledforeground='blue')
    s[8].insert(0,5)
    s[8]['state']=DISABLED
    s[8].config(disabledbackground='light goldenrod',disabledforeground='blue')

    global t
    t=['t1','t2','t3','t4','t5','t6','t7','t8','t9']
    for i in range(0,9):
        t[i]=Entry(root,relief=RAISED,width=10,justify=CENTER,font='Times 17 bold')
        t[i].grid(row=3,column=i,sticky=W,ipady=10)
        if i <= 2 or i>=6:
            t[i]['background']='light goldenrod'

    t[2].insert(0,8)
    t[2]['state']=DISABLED
    t[2].config(disabledbackground='light goldenrod',disabledforeground='blue')
    t[5].insert(0,9)
    t[5]['state']=DISABLED
    t[5].config(disabledbackground='white',disabledforeground='blue')
    t[6].insert(0,4)
    t[6]['state']=DISABLED
    t[6].config(disabledbackground='light goldenrod',disabledforeground='blue')
    t[7].insert(0,6)
    t[7]['state']=DISABLED
    t[7].config(disabledbackground='light goldenrod',disabledforeground='blue')

    global fo
    fo=['fo1','fo2','fo3','fo4','fo5','fo6','fo7','fo8','fo9']

    for i in range(0,9):
        fo[i]=Entry(root,relief=RAISED,width=10,justify=CENTER,font='Times 17 bold')
        fo[i].grid(row=4,column=i,sticky=W,ipady=10)
        if i>=3 and i<=5:
            fo[i]['background']='light goldenrod'
    fo[7].insert(0,7)
    fo[7]['state']=DISABLED
    fo[7].config(disabledbackground='white',disabledforeground='blue')

    fo[8].insert(0,8)
    fo[8]['state']=DISABLED
    fo[8].config(disabledbackground='white',disabledforeground='blue')

    fo[3].insert(0,9)
    fo[3]['state']=DISABLED
    fo[3].config(disabledbackground='light goldenrod',disabledforeground='blue')

    fo[5].insert(0,6)
    fo[5]['state']=DISABLED
    fo[5].config(disabledbackground='light goldenrod',disabledforeground='blue')

    global fi
    fi=['fi1','fi2','fi3','fi4','fi5','fi6','fi7','fi8','fi9']
    for i in range(0,9):
        fi[i]=Entry(root,relief=RAISED,width=10,justify=CENTER,font='Times 17 bold')
        fi[i].grid(row=5,column=i,sticky=W,ipady=10)
        if i>=3 and i<=5:
            fi[i]['background']='light goldenrod'
    fi[0].insert(0,8)
    fi[0]['state']=DISABLED
    fi[0].config(disabledbackground='white',disabledforeground='blue')

    global si
    si=['si1','si2','si3','si4','si5','si6','si7','si8','si9']
    for i in range(0,9):
        si[i]=Entry(root,relief=RAISED,width=10,justify=CENTER,font='Times 17 bold')
        si[i].grid(row=6,column=i,sticky=W,ipady=10)
        if i>=3 and i<=5:
            si[i]['background']='light goldenrod'
    si[0].insert(0,7)
    si[0]['state']=DISABLED
    si[0].config(disabledbackground='white',disabledforeground='blue')
    si[4].insert(0,5)
    si[4]['state']=DISABLED
    si[4].config(disabledbackground='light goldenrod',disabledforeground='blue')
    si[8].insert(0,3)
    si[8]['state']=DISABLED
    si[8].config(disabledbackground='white',disabledforeground='blue')

    global se
    se=['se1','se2','se3','se4','se5','se6','se7','se8','se9']
    for i in range(0,9):
        se[i]=Entry(root,relief=RAISED,width=10,justify=CENTER,font='Times 17 bold')
        se[i].grid(row=7,column=i,sticky=W,ipady=10)
        if i <= 2 or i>=6:
            se[i]['background']='light goldenrod'

    se[4].insert(0,6)
    se[4]['state']=DISABLED
    se[4].config(disabledbackground='white',disabledforeground='blue')
    se[5].insert(0,8)
    se[5]['state']=DISABLED
    se[5].config(disabledbackground='white',disabledforeground='blue')
    se[6].insert(0,7)
    se[6]['state']=DISABLED
    se[6].config(disabledbackground='light goldenrod',disabledforeground='blue')
    se[7].insert(0,2)
    se[7]['state']=DISABLED
    se[7].config(disabledbackground='light goldenrod',disabledforeground='blue')

    global e
    e=['e1','e2','e3','e4','e5','e6','e7','e8','e9']
    for i in range(0,9):
        e[i]=Entry(root,relief=RAISED,width=10,justify=CENTER,font='Times 17 bold')
        e[i].grid(row=8,column=i,sticky=W,ipady=10)
        if i <= 2 or i>=6:
            e[i]['background']='light goldenrod'


    e[5].insert(0,2)
    e[5]['state']=DISABLED
    e[5].config(disabledbackground='white',disabledforeground='blue')
    e[6].insert(0,5)
    e[6]['state']=DISABLED
    e[6].config(disabledbackground='light goldenrod',disabledforeground='blue')

    global n
    n=['n1','n2','n3','n4','n5','n6','n7','n8','n9']
    for i in range(0,9):
        n[i]=Entry(root,relief=RAISED,width=10,justify=CENTER,font='Times 17 bold')
        n[i].grid(row=9,column=i,sticky=W,ipady=10)
        if i <= 2 or i>=6:
            n[i]['background']='light goldenrod'
    n[1].insert(0,5)
    n[1]['state']=DISABLED
    n[1].config(disabledbackground='light goldenrod',disabledforeground='blue')
    n[0].insert(0,2)
    n[0]['state']=DISABLED
    n[0].config(disabledbackground='light goldenrod',disabledforeground='blue')
    n[2].insert(0,4)
    n[2]['state']=DISABLED
    n[2].config(disabledbackground='light goldenrod',disabledforeground='blue')
    n[6].insert(0,3)
    n[6]['state']=DISABLED
    n[6].config(disabledbackground='light goldenrod',disabledforeground='blue')

    sub = Button(root,text='submit',command=submit)
    sub.grid(row=10,column=8,pady=10,columnspan=2)

def hard_level():
    easy.destroy()
    medium.destroy()
    hard.destroy()
    evil.destroy()
    global f
    f=['f1','f2','f3','f4','f5','f6','f7','f8','f9']
    for i in range(0,9):
        f[i]=Entry(root,relief=RAISED,width=10,justify=CENTER,font='Times 17 bold')
        f[i].grid(row=1,column=i,sticky=W,ipady=10)
        if i <= 2 or i>=6:
            f[i]['background']='light goldenrod'
    f[0].insert(0,2)
    f[0]['state']=DISABLED
    f[0].config(disabledbackground='light goldenrod',disabledforeground='blue')
    f[1].insert(0,5)
    f[1]['state']=DISABLED
    f[1].config(disabledbackground='light goldenrod',disabledforeground='blue')
    f[2].insert(0,4)
    f[2]['state']=DISABLED
    f[2].config(disabledbackground='light goldenrod',disabledforeground='blue')
    f[5].insert(0,3)
    f[5]['state']=DISABLED
    f[5].config(disabledbackground='white',disabledforeground='blue')

    global s
    s=['s1','s2','s3','s4','s5','s6','s7','s8','s9']
    for i in range(0,9):
        s[i]=Entry(root,relief=RAISED,width=10,justify=CENTER,font='Times 17 bold')
        s[i].grid(row=2,column=i,sticky=W,ipady=10)
        if i <= 2 or i>=6:
            s[i]['background']='light goldenrod'

    s[1].insert(0,8)
    s[1]['state']=DISABLED
    s[1].config(disabledbackground='light goldenrod',disabledforeground='blue')
    s[2].insert(0,7)
    s[2]['state']=DISABLED
    s[2].config(disabledbackground='light goldenrod',disabledforeground='blue')
    s[7].insert(0,4)
    s[7]['state']=DISABLED
    s[7].config(disabledbackground='light goldenrod',disabledforeground='blue')

    global t
    t=['t1','t2','t3','t4','t5','t6','t7','t8','t9']
    for i in range(0,9):
        t[i]=Entry(root,relief=RAISED,width=10,justify=CENTER,font='Times 17 bold')
        t[i].grid(row=3,column=i,sticky=W,ipady=10)
        if i <= 2 or i>=6:
            t[i]['background']='light goldenrod'

    t[0].insert(0,9)
    t[0]['state']=DISABLED
    t[0].config(disabledbackground='light goldenrod',disabledforeground='blue')
    t[4].insert(0,2)
    t[4]['state']=DISABLED
    t[4].config(disabledbackground='white',disabledforeground='blue')

    global fo
    fo=['fo1','fo2','fo3','fo4','fo5','fo6','fo7','fo8','fo9']

    for i in range(0,9):
        fo[i]=Entry(root,relief=RAISED,width=10,justify=CENTER,font='Times 17 bold')
        fo[i].grid(row=4,column=i,sticky=W,ipady=10)
        if i>=3 and i<=5:
            fo[i]['background']='light goldenrod'
    fo[7].insert(0,1)
    fo[7]['state']=DISABLED
    fo[7].config(disabledbackground='white',disabledforeground='blue')

    fo[8].insert(0,2)
    fo[8]['state']=DISABLED
    fo[8].config(disabledbackground='white',disabledforeground='blue')

    fo[1].insert(0,3)
    fo[1]['state']=DISABLED
    fo[1].config(disabledbackground='white',disabledforeground='blue')

    fo[5].insert(0,4)
    fo[5]['state']=DISABLED
    fo[5].config(disabledbackground='light goldenrod',disabledforeground='blue')

    global fi
    fi=['fi1','fi2','fi3','fi4','fi5','fi6','fi7','fi8','fi9']
    for i in range(0,9):
        fi[i]=Entry(root,relief=RAISED,width=10,justify=CENTER,font='Times 17 bold')
        fi[i].grid(row=5,column=i,sticky=W,ipady=10)
        if i>=3 and i<=5:
            fi[i]['background']='light goldenrod'
    fi[4].insert(0,9)
    fi[4]['state']=DISABLED
    fi[4].config(disabledbackground='light goldenrod',disabledforeground='blue')
    fi[6].insert(0,4)
    fi[6]['state']=DISABLED
    fi[6].config(disabledbackground='white',disabledforeground='blue')
    fi[8].insert(0,7)
    fi[8]['state']=DISABLED
    fi[8].config(disabledbackground='white',disabledforeground='blue')

    global si
    si=['si1','si2','si3','si4','si5','si6','si7','si8','si9']
    for i in range(0,9):
        si[i]=Entry(root,relief=RAISED,width=10,justify=CENTER,font='Times 17 bold')
        si[i].grid(row=6,column=i,sticky=W,ipady=10)
        if i>=3 and i<=5:
            si[i]['background']='light goldenrod'

    si[6].insert(0,5)
    si[6]['state']=DISABLED
    si[6].config(disabledbackground='white',disabledforeground='blue')

    global se
    se=['se1','se2','se3','se4','se5','se6','se7','se8','se9']
    for i in range(0,9):
        se[i]=Entry(root,relief=RAISED,width=10,justify=CENTER,font='Times 17 bold')
        se[i].grid(row=7,column=i,sticky=W,ipady=10)
        if i <= 2 or i>=6:
            se[i]['background']='light goldenrod'

    se[4].insert(0,7)
    se[4]['state']=DISABLED
    se[4].config(disabledbackground='white',disabledforeground='blue')
    se[8].insert(0,9)
    se[8]['state']=DISABLED
    se[8].config(disabledbackground='light goldenrod',disabledforeground='blue')

    global e
    e=['e1','e2','e3','e4','e5','e6','e7','e8','e9']
    for i in range(0,9):
        e[i]=Entry(root,relief=RAISED,width=10,justify=CENTER,font='Times 17 bold')
        e[i].grid(row=8,column=i,sticky=W,ipady=10)
        if i <= 2 or i>=6:
            e[i]['background']='light goldenrod'


    e[1].insert(0,2)
    e[1]['state']=DISABLED
    e[1].config(disabledbackground='light goldenrod',disabledforeground='blue')
    e[7].insert(0,5)
    e[7]['state']=DISABLED
    e[7].config(disabledbackground='light goldenrod',disabledforeground='blue')

    global n
    n=['n1','n2','n3','n4','n5','n6','n7','n8','n9']
    for i in range(0,9):
        n[i]=Entry(root,relief=RAISED,width=10,justify=CENTER,font='Times 17 bold')
        n[i].grid(row=9,column=i,sticky=W,ipady=10)
        if i <= 2 or i>=6:
            n[i]['background']='light goldenrod'
    n[5].insert(0,6)
    n[5]['state']=DISABLED
    n[5].config(disabledbackground='white',disabledforeground='blue')
    n[4].insert(0,5)
    n[4]['state']=DISABLED
    n[4].config(disabledbackground='white',disabledforeground='blue')
    n[7].insert(0,7)
    n[7]['state']=DISABLED
    n[7].config(disabledbackground='light goldenrod',disabledforeground='blue')
    n[6].insert(0,3)
    n[6]['state']=DISABLED
    n[6].config(disabledbackground='light goldenrod',disabledforeground='blue')

    sub = Button(root,text='submit',command=submit)
    sub.grid(row=10,column=8,pady=10,columnspan=2)

def evil_level():
    easy.destroy()
    medium.destroy()
    hard.destroy()
    evil.destroy()
    global f
    f=['f1','f2','f3','f4','f5','f6','f7','f8','f9']
    for i in range(0,9):
        f[i]=Entry(root,relief=RAISED,width=10,justify=CENTER,font='Times 17 bold')
        f[i].grid(row=1,column=i,sticky=W,ipady=10)
        if i <= 2 or i>=6:
            f[i]['background']='light goldenrod'

    f[6].insert(0,6)
    f[6]['state']=DISABLED
    f[6].config(disabledbackground='light goldenrod',disabledforeground='blue')
    f[2].insert(0,3)
    f[2]['state']=DISABLED
    f[2].config(disabledbackground='light goldenrod',disabledforeground='blue')
    f[3].insert(0,4)
    f[3]['state']=DISABLED
    f[3].config(disabledbackground='white',disabledforeground='blue')

    global s
    s=['s1','s2','s3','s4','s5','s6','s7','s8','s9']
    for i in range(0,9):
        s[i]=Entry(root,relief=RAISED,width=10,justify=CENTER,font='Times 17 bold')
        s[i].grid(row=2,column=i,sticky=W,ipady=10)
        if i <= 2 or i>=6:
            s[i]['background']='light goldenrod'

    s[0].insert(0,5)
    s[0]['state']=DISABLED
    s[0].config(disabledbackground='light goldenrod',disabledforeground='blue')
    s[4].insert(0,2)
    s[4]['state']=DISABLED
    s[4].config(disabledbackground='white',disabledforeground='blue')
    s[7].insert(0,3)
    s[7]['state']=DISABLED
    s[7].config(disabledbackground='light goldenrod',disabledforeground='blue')

    global t
    t=['t1','t2','t3','t4','t5','t6','t7','t8','t9']
    for i in range(0,9):
        t[i]=Entry(root,relief=RAISED,width=10,justify=CENTER,font='Times 17 bold')
        t[i].grid(row=3,column=i,sticky=W,ipady=10)
        if i <= 2 or i>=6:
            t[i]['background']='light goldenrod'

    t[4].insert(0,8)
    t[4]['state']=DISABLED
    t[4].config(disabledbackground='white',disabledforeground='blue')

    global fo
    fo=['fo1','fo2','fo3','fo4','fo5','fo6','fo7','fo8','fo9']

    for i in range(0,9):
        fo[i]=Entry(root,relief=RAISED,width=10,justify=CENTER,font='Times 17 bold')
        fo[i].grid(row=4,column=i,sticky=W,ipady=10)
        if i>=3 and i<=5:
            fo[i]['background']='light goldenrod'


    fo[1].insert(0,1)
    fo[1]['state']=DISABLED
    fo[1].config(disabledbackground='white',disabledforeground='blue')

    fo[2].insert(0,7)
    fo[2]['state']=DISABLED
    fo[2].config(disabledbackground='white',disabledforeground='blue')

    global fi
    fi=['fi1','fi2','fi3','fi4','fi5','fi6','fi7','fi8','fi9']
    for i in range(0,9):
        fi[i]=Entry(root,relief=RAISED,width=10,justify=CENTER,font='Times 17 bold')
        fi[i].grid(row=5,column=i,sticky=W,ipady=10)
        if i>=3 and i<=5:
            fi[i]['background']='light goldenrod'
    fi[4].insert(0,6)
    fi[4]['state']=DISABLED
    fi[4].config(disabledbackground='light goldenrod',disabledforeground='blue')
    fi[2].insert(0,4)
    fi[2]['state']=DISABLED
    fi[2].config(disabledbackground='white',disabledforeground='blue')
    fi[5].insert(0,2)
    fi[5]['state']=DISABLED
    fi[5].config(disabledbackground='light goldenrod',disabledforeground='blue')

    global si
    si=['si1','si2','si3','si4','si5','si6','si7','si8','si9']
    for i in range(0,9):
        si[i]=Entry(root,relief=RAISED,width=10,justify=CENTER,font='Times 17 bold')
        si[i].grid(row=6,column=i,sticky=W,ipady=10)
        if i>=3 and i<=5:
            si[i]['background']='light goldenrod'

    si[5].insert(0,9)
    si[5]['state']=DISABLED
    si[5].config(disabledbackground='light goldenrod',disabledforeground='blue')

    global se
    se=['se1','se2','se3','se4','se5','se6','se7','se8','se9']
    for i in range(0,9):
        se[i]=Entry(root,relief=RAISED,width=10,justify=CENTER,font='Times 17 bold')
        se[i].grid(row=7,column=i,sticky=W,ipady=10)
        if i <= 2 or i>=6:
            se[i]['background']='light goldenrod'

    se[1].insert(0,7)
    se[1]['state']=DISABLED
    se[1].config(disabledbackground='light goldenrod',disabledforeground='blue')
    se[6].insert(0,5)
    se[6]['state']=DISABLED
    se[6].config(disabledbackground='light goldenrod',disabledforeground='blue')
    se[8].insert(0,8)
    se[8]['state']=DISABLED
    se[8].config(disabledbackground='light goldenrod',disabledforeground='blue')

    global e
    e=['e1','e2','e3','e4','e5','e6','e7','e8','e9']
    for i in range(0,9):
        e[i]=Entry(root,relief=RAISED,width=10,justify=CENTER,font='Times 17 bold')
        e[i].grid(row=8,column=i,sticky=W,ipady=10)
        if i <= 2 or i>=6:
            e[i]['background']='light goldenrod'


    e[0].insert(0,9)
    e[0]['state']=DISABLED
    e[0].config(disabledbackground='light goldenrod',disabledforeground='blue')
    e[3].insert(0,6)
    e[3]['state']=DISABLED
    e[3].config(disabledbackground='white',disabledforeground='blue')

    global n
    n=['n1','n2','n3','n4','n5','n6','n7','n8','n9']
    for i in range(0,9):
        n[i]=Entry(root,relief=RAISED,width=10,justify=CENTER,font='Times 17 bold')
        n[i].grid(row=9,column=i,sticky=W,ipady=10)
        if i <= 2 or i>=6:
            n[i]['background']='light goldenrod'

    n[4].insert(0,4)
    n[4]['state']=DISABLED
    n[4].config(disabledbackground='white',disabledforeground='blue')
    n[8].insert(0,7)
    n[8]['state']=DISABLED
    n[8].config(disabledbackground='light goldenrod',disabledforeground='blue')
    n[6].insert(0,1)
    n[6]['state']=DISABLED
    n[6].config(disabledbackground='light goldenrod',disabledforeground='blue')

    sub = Button(root,text='submit',command=submit)
    sub.grid(row=10,column=8,pady=10,columnspan=2)


title=Label(root,text='sudoku',font='times 20 italic',background='black',fg='white',padx=5,pady=5)
title.grid(row=0,column=0,sticky=W+E,pady=10,columnspan=9)

easy = Button(root,text='EASY',relief=RAISED,width=10,justify=CENTER,font='Times 17 bold',command=easy_level)
easy.grid(row=1,column=0,sticky=W+E,pady=5)
medium = Button(root,text='MEDIUM',relief=RAISED,width=10,justify=CENTER,font='Times 17 bold',command=medium_level)
medium.grid(row=2,column=0,sticky=W+E,pady=5)
hard = Button(root,text='HARD',relief=RAISED,width=10,justify=CENTER,font='Times 17 bold',command=hard_level)
hard.grid(row=3,column=0,sticky=W+E,pady=5)
evil =  Button(root,text='EVIL',relief=RAISED,width=10,justify=CENTER,font='Times 17 bold',command=evil_level)
evil.grid(row=4,column=0,sticky=W+E,pady=5)


root.mainloop()
