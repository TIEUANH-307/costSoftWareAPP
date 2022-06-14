# -*- coding: utf-8 -*-
from __future__ import division
from tkinter import Tk, Frame, BOTH, Text, TOP, BOTH, X, N, LEFT
from tkinter.ttk import Button, Style
from tkinter import *



root = Tk()
root.geometry("800x600+300+100")


    
 
class Window(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.initUI()
  
    def initUI(self):
        self.parent.title("Ứng dụng hỗ trợ xác định chi phí phần mềm")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand=1)

        #add frame
        frame1 = Frame(self)
        frame1.pack(fill=X)

        #add label1
        label1 = Label(frame1, text="Ứng dụng hỗ trợ xác định chi phí phần mềm", font=('Tahoma', 18))
        label1.pack(side=TOP)

        label2 = Label(frame1, text="I. Tính điểm trường hợp sử dụng (use-case)", font=('Tahoma', 11))
        label2.pack(side=LEFT, padx=20)

        #add frame 2
        frame2 = Frame(self)
        frame2.pack(fill=X, padx=40)

        #TAW
        label3 = Label(frame2, text="1. Điểm Actor (TAW) được tính là: ", font=('Tahoma', 11))
        label3.grid(row=1, column=0)
        
      
        #diem can tinh TAW
        label4= Label(frame2, text = "", font=('Tahoma', 11))
        label4.grid(row=1, column=2)
        
        #TBF
        label5 = Label(frame2, text= "2. Điểm Use-case (TBF): ", font=('Tahoma', 11))
        label5.grid(row=1, column=3, padx=40)

        #diem can tinh TBF
        label6= Label(frame2, text = "", font=('Tahoma', 11))
        label6.grid(row=1, column=4)


        #UUCP
        label7= Label(frame2, text= "3.  Điểm UUCP = TAW + TBF =  ", font=('Tahoma', 11))
        label7.grid(row=2)

        #diem can tinh UUCP
        label8= Label(frame2, text= "", font=('Tahoma', 11))
        label8.grid(row=2, column=2)

        #TCF
        label9= Label(frame2, text= "4. Hệ số phức tạp KT - CN (TCF): ", font=('Tahoma', 11))
        label9.grid(row=3)
        

        #diem can tinh TCF
        label10= Label(frame2, text= "", font=('Tahoma', 11))
        label10.grid(row=3, column=2)


        #EF
        label11= Label(frame2, text= "5. Hệ số phức tạp môi trường (EF): ", font=('Tahoma',11))
        label11.grid(row=3, column=3, padx=40)
        #diem can tinh EF
        labelEFfill= Label(frame2, text= "", font=('Tahoma', 11))
        labelEFfill.grid(row=3, column=4)


        #AUCP
        label13= Label(frame2, text= "6. Điểm AUCP=UUCP x TCF x EF= ", font=('Tahoma',11))
        label13.grid(row=4)
        #diem can tinh AUCP
        label14= Label(frame2, text= "", font=('Tahoma', 11))
        label14.grid(row=4, column=2)



        #add frame 3
        frame3 = Frame(self)
        frame3.pack(fill=X, padx=25)

        #Thoi gian lao dong
        labelPtext = Label(frame3, text="II. Nội suy thời gian lao động (P): ", font=('Tahoma', 11))
        labelPtext.pack(side=LEFT)

        #diem tinh P
        labelP = Label(frame3, text= "", font=('Tahoma', 11))
        labelP.pack(side=LEFT, padx=10)

        #add frame 4
        frame4 = Frame(self)
        frame4.pack(fill=X, padx=25)

        #Gia tri no luc thuc te
        labelEtext = Label(frame4, text="III. Giá trị nỗ lực thực tế E = 10/6 x AUCP = ", font=('Tahoma', 11))
        labelEtext.pack(side=LEFT)

        #diem tinh E
        labelE = Label(frame4, text= "", font=('Tahoma', 11))
        labelE.pack(side=LEFT, padx=10)

        #add frame 5
        frame5 = Frame(self)
        frame5.pack(fill=X, padx=25)

        #Muc luong lao dong binh quan
        labelHtext = Label(frame5, text="IV. Mức lương lao động bình quân (H): ", font=('Tahoma', 11))
        labelHtext.pack(side=LEFT)

        #diem tinh H

        labelHcal = Label(frame5, text= "", font=('Tahoma', 11))
        labelHcal.pack(side=LEFT, padx=10)

        #add frame 6
        frame6 = Frame(self)
        frame6.pack(fill=X, padx=25)

        #Gia tri phan mem noi bo
        labelGtext = Label(frame6, text= "V. Giá trị phần mềm nội bộ G = 1.4 x E x P x H = ", font=('Tahoma', 11))
        labelGtext.pack(side=LEFT)

        #diem tinh G
        labelG = Label(frame6, text= "", font=('Tahoma', 11))
        labelG.pack(side=LEFT, padx=10)


        frame7 = Frame(self, relief=RAISED, borderwidth=1)
        frame7.pack(fill=X)

        

        def TAWCalculate(self):
            frame8 = Frame(self)
            frame8.pack(fill=X, padx=25)
            labelTAWhead = Label(frame8, text="Tính toán điểm các tác nhân tương tác (TAW)", font=('Tahoma', 14))
            labelTAWhead.pack(side=TOP)

            frame9 = Frame(self)
            frame9.pack(fill=X, padx=25)

            label01 = Label(frame9, text="Các loại tác nhân (Actor)", font=('Tahoma', 11))
            label01.grid(row=1, column=1)

            label11 = Label(frame9, text='1. Đơn giản', font=('Tahoma',11))
            label11.grid(row=2, column=1)

            label12 = Label(frame9, text='2. Trung bình', font=('Tahoma',11))
            label12.grid(row=3, column=1)

            label13 = Label(frame9, text='3. Phức tạp', font=('Tahoma',11))
            label13.grid(row=4, column=1)

            label02 = Label(frame9, text="Trọng số", font=('Tahoma', 11))
            label02.grid(row=1, column=2)

            label21 = Label(frame9, text='1', font=('Tahoma',11))
            label21.grid(row=2, column=2)

            label22 = Label(frame9, text='2', font=('Tahoma',11))
            label22.grid(row=3, column=2)

            label23 = Label(frame9, text='3', font=('Tahoma',11))
            label23.grid(row=4, column=2)

            label03 = Label(frame9, text="Số lượng", font=('Tahoma', 11))
            label03.grid(row=1, column=3)

            entrySL1 = Entry(frame9, width=5)
            entrySL1.grid(row=2, column=3)

            entrySL2 = Entry(frame9, width=5)
            entrySL2.grid(row=3, column=3)

            entrySL3 = Entry(frame9, width=5)
            entrySL3.grid(row=4, column=3)

        #hàm tính TAW
            def TAWCalculateOutPut():
                int1 = int(entrySL1.get())
                int2 = int(entrySL2.get())
                int3 = int(entrySL3.get())
                labelGiaTri.configure(text=str(int1 * 1 + int2 * 2 + int3 * 3))
                label4.configure(text=str(int1 * 1 + int2 * 2 + int3 * 3))


            btnTinhTAW = Button(frame9, width=5, text='Tính', command=TAWCalculateOutPut)
            btnTinhTAW.grid(row=2, column=5)

            labelTinh = Label(frame9, text='TAW = ', font=('Tahoma',11))
            labelTinh.grid(row=3, column=5)

            labelGiaTri = Label(frame9, text= "", font=('Tahoma', 11))
            labelGiaTri.grid(row=3, column=6)

        

        #hàm giao diện TBF
        def TBFCalculate(self):
            frame8 = Frame(self)
            frame8.pack(fill=X, padx=25)
            labelTBFhead = Label(frame8, text="Bảng tính toán điểm các trường hợp sử dụng TBF (TBF)", font=('Tahoma', 14))
            labelTBFhead.pack(side=TOP)

            frame9 = Frame(self)
            frame9.pack(fill=X, padx=25)

            label01 = Label(frame9, text="Loại", font=('Tahoma', 11))
            label01.grid(row=1, column=1)

            label11 = Label(frame9, text='B', font=('Tahoma',11))
            label11.grid(row=2, column=1)

            label12 = Label(frame9, text='M', font=('Tahoma',11))
            label12.grid(row=3, column=1)

            label13 = Label(frame9, text='T', font=('Tahoma',11))
            label13.grid(row=4, column=1)

            label02 = Label(frame9, text="Đơn giản", font=('Tahoma', 11))
            label02.grid(row=1, column=2)
            
            entrySLsimpleB = Entry(frame9, width=5)
            entrySLsimpleB.grid(row=2, column=2)

            entrySLsimpleM = Entry(frame9, width=5)
            entrySLsimpleM.grid(row=3, column=2)

            entrySLsimpleT = Entry(frame9, width=5)
            entrySLsimpleT.grid(row=4, column=2)

            label03 = Label(frame9, text="Trung bình", font=('Tahoma', 11))
            label03.grid(row=1, column=3)

            entrySLmediumB = Entry(frame9, width=5)
            entrySLmediumB.grid(row=2, column=3)

            entrySLmediumM = Entry(frame9, width=5)
            entrySLmediumM.grid(row=3, column=3)

            entrySLmediumT = Entry(frame9, width=5)
            entrySLmediumT.grid(row=4, column=3)

            label04 = Label(frame9, text="Phức tạp", font=('Tahoma', 11))
            label04.grid(row=1, column=4)

            entrySLcompB = Entry(frame9, width=5)
            entrySLcompB.grid(row=2, column=4)

            entrySLcompM = Entry(frame9, width=5)
            entrySLcompM.grid(row=3, column=4)

            entrySLcompT = Entry(frame9, width=5)
            entrySLcompT.grid(row=4, column=4)

        #hàm tính TBF
            def TBFCalculateOutPut():
                intSimple = [int(entrySLsimpleB.get()), int(entrySLsimpleM.get()), int(entrySLsimpleT.get())]
                intMedium = [int(entrySLmediumB.get()), int(entrySLmediumM.get()), int(entrySLmediumT.get())]
                intComp = [int(entrySLcompB.get()), int(entrySLcompM.get()), int(entrySLcompT.get())]
                giatriSimple = (intSimple[0] + intSimple[1] * 1.2 + intSimple[2] * 1.5) * 5
                giatriMedium = (intMedium[0] + intMedium[1] * 1.2 + intMedium[2] * 1.5) * 10
                giatriComp = (intComp[0] + intComp[1] * 1.2 + intComp[2] * 1.5) * 15
                giatri = giatriSimple + giatriMedium + giatriComp
                labelGiaTri.configure(text=giatri)
                label6.configure(text=giatri)



            btnTinhTAW = Button(frame9, width=5, text='Tính', command=TBFCalculateOutPut)
            btnTinhTAW.grid(row=2, column=5)

            labelTinh = Label(frame9, text='TBF = ', font=('Tahoma',11), width=10)
            labelTinh.grid(row=3, column=5)

            labelGiaTri = Label(frame9, text= "", font=('Tahoma', 11))
            labelGiaTri.grid(row=4, column=5)

        #hàm giao diện TCF
        def TCFCalculate(self):
            frame8 = Frame(self)
            frame8.pack(fill=X, padx=25)
            labelTCFhead = Label(frame8, text="Bảng tính toán hệ số phức tạp KT-CN", font=('Tahoma', 14))
            labelTCFhead.pack(side=TOP)

            frame9 = Frame(self)
            frame9.pack(fill=X, padx=25)

            #cột 1 - STT
            label01 = Label(frame9, text='TT', font=('Tahoma',11))
            label01.grid(row=1, column=1)

            label11 = Label(frame9, text='1', font=('Tahoma',11))
            label11.grid(row=2, column=1)

            label21 = Label(frame9, text='2', font=('Tahoma',11))
            label21.grid(row=3, column=1)

            label31 = Label(frame9, text='3', font=('Tahoma',11))
            label31.grid(row=4, column=1)

            label41 = Label(frame9, text='4', font=('Tahoma',11))
            label41.grid(row=5, column=1)

            label51 = Label(frame9, text='5', font=('Tahoma',11))
            label51.grid(row=6, column=1)

            label61 = Label(frame9, text='6', font=('Tahoma',11))
            label61.grid(row=7, column=1)

            label71 = Label(frame9, text='7', font=('Tahoma',11))
            label71.grid(row=8, column=1)

            label81 = Label(frame9, text='8', font=('Tahoma',11))
            label81.grid(row=9, column=1)

            label91 = Label(frame9, text='9', font=('Tahoma',11))
            label91.grid(row=10, column=1)

            label101 = Label(frame9, text='10', font=('Tahoma',11))
            label101.grid(row=11, column=1)

            label111 = Label(frame9, text='11', font=('Tahoma',11))
            label111.grid(row=12, column=1)

            label121 = Label(frame9, text='12', font=('Tahoma',11))
            label121.grid(row=13, column=1)

            label131 = Label(frame9, text='13', font=('Tahoma',11))
            label131.grid(row=14, column=1)

            #cột 2 - Các hệ số
            label02 = Label(frame9, text='Các hệ số', font=('Tahoma',11))
            label02.grid(row=1, column=2, sticky='w')

            label12 = Label(frame9, anchor="w",text='Hệ thống phân tán', font=('Tahoma',11))
            label12.grid(row=2, column=2, sticky='w')

            label22 = Label(frame9, anchor="w",text='Tính chất đáp ứng tức thời hoặc yêu cầu đảm bảo thông lượng', font=('Tahoma',11))
            label22.grid(row=3, column=2, sticky='w')

            label32 = Label(frame9, anchor="w",text='Hiệu quả sử dụng trực tuyến', font=('Tahoma',11))
            label32.grid(row=4, column=2, sticky='w')

            label42 = Label(frame9, text='Độ phức tạp của xử lý bên trong', font=('Tahoma',11))
            label42.grid(row=5, column=2, sticky='w')

            label52 = Label(frame9, text='Mã nguồn phải tái sử dụng được', font=('Tahoma',11))
            label52.grid(row=6, column=2, sticky='w')

            label62 = Label(frame9, text='Dễ cài đặt', font=('Tahoma',11))
            label62.grid(row=7, column=2, sticky='w')

            label72 = Label(frame9, text='Dễ sử sụng', font=('Tahoma',11))
            label72.grid(row=8, column=2, sticky='w')

            label82 = Label(frame9, text='Khả năng chuyển đổi', font=('Tahoma',11))
            label82.grid(row=9, column=2, sticky='w')

            label92 = Label(frame9, text='Khả năng dễ thay đổi', font=('Tahoma',11))
            label92.grid(row=10, column=2, sticky='w')

            label102 = Label(frame9, text='Sử dụng đồng thời', font=('Tahoma',11))
            label102.grid(row=11, column=2, sticky='w')

            label112 = Label(frame9, text='Có các tính năng bảo mật đặc biệt', font=('Tahoma',11))
            label112.grid(row=12, column=2, sticky='w')

            label122 = Label(frame9, text='Cung cấp truy nhập trực tiếp tới các phần mềm của hãng thứ ba', font=('Tahoma',11))
            label122.grid(row=13, column=2, sticky='w')

            label132 = Label(frame9, text='Yêu cầu phương tiện đào tạo đặc biệt cho người sử dụng', font=('Tahoma',11))
            label132.grid(row=14, column=2, sticky='w')

            #cột 3 - Trọng số
            label03 = Label(frame9, text='Trọng số', font=('Tahoma',11))
            label03.grid(row=1, column=3)

            label13 = Label(frame9, text='2', font=('Tahoma',11))
            label13.grid(row=2, column=3)

            label23 = Label(frame9, text='1', font=('Tahoma',11))
            label23.grid(row=3, column=3)

            label33 = Label(frame9, text='1', font=('Tahoma',11))
            label33.grid(row=4, column=3)

            label43 = Label(frame9, text='1', font=('Tahoma',11))
            label43.grid(row=5, column=3)

            label53 = Label(frame9, text='1', font=('Tahoma',11))
            label53.grid(row=6, column=3)

            label63 = Label(frame9, text='0.5', font=('Tahoma',11))
            label63.grid(row=7, column=3)

            label73 = Label(frame9, text='0.5', font=('Tahoma',11))
            label73.grid(row=8, column=3)

            label83 = Label(frame9, text='2', font=('Tahoma',11))
            label83.grid(row=9, column=3)

            label93 = Label(frame9, text='1', font=('Tahoma',11))
            label93.grid(row=10, column=3)

            label103 = Label(frame9, text='1', font=('Tahoma',11))
            label103.grid(row=11, column=3)

            label113 = Label(frame9, text='1', font=('Tahoma',11))
            label113.grid(row=12, column=3)

            label123 = Label(frame9, text='1', font=('Tahoma',11))
            label123.grid(row=13, column=3)

            label133 = Label(frame9, text='1', font=('Tahoma',11))
            label133.grid(row=14, column=3)

            #cột 4 - Giá trị xếp hạng
            label04 = Label(frame9, text='Giá trị xếp hạng', font=('Tahoma',11))
            label04.grid(row=1, column=4)

            entry14 = Entry(frame9, width=5)
            entry14.grid(row=2, column=4)
            
            entry24 = Entry(frame9, width=5)
            entry24.grid(row=3, column=4)

            entry34 = Entry(frame9, width=5)
            entry34.grid(row=4, column=4)

            entry44 = Entry(frame9, width=5)
            entry44.grid(row=5, column=4)

            entry54 = Entry(frame9, width=5)
            entry54.grid(row=6, column=4)

            entry64 = Entry(frame9, width=5)
            entry64.grid(row=7, column=4)

            entry74 = Entry(frame9, width=5)
            entry74.grid(row=8, column=4)

            entry84 = Entry(frame9, width=5)
            entry84.grid(row=9, column=4)

            entry94 = Entry(frame9, width=5)
            entry94.grid(row=10, column=4)

            entry104 = Entry(frame9, width=5)
            entry104.grid(row=11, column=4)

            entry114 = Entry(frame9, width=5)
            entry114.grid(row=12, column=4)

            entry124 = Entry(frame9, width=5)
            entry124.grid(row=13, column=4)

            entry134 = Entry(frame9, width=5)
            entry134.grid(row=14, column=4)

            def calculateTFW():
                listWeights = [2,1,1,1,1,0.5,0.5,2,1,1,1,1,1]
                float1 = float(entry14.get())
                float2 = float(entry24.get())
                float3 = float(entry34.get())
                float4 = float(entry44.get())
                float5 = float(entry54.get())
                float6 = float(entry64.get())
                float7 = float(entry74.get())
                float8 = float(entry84.get())
                float9 = float(entry94.get())
                float10 = float(entry104.get())
                float11 = float(entry114.get())
                float12 = float(entry124.get())
                float13 = float(entry134.get())

                floatList = [float1, float2, float3, float4, float5, float6, float7, float8, float9, float10, float11, 
                            float12, float13]
                TFW = 0
                for i in range(len(listWeights)):
                    TFW += listWeights[i] * floatList[i]
                
                TCF = 0.6 + (0.01 * TFW)
                labelValueTFW.configure(text=str(TFW))
                labelValueTCF.configure(text=str(TCF))
                label10.configure(text=str(TCF))
                

            btnTinhtext = Button(frame9, text='Tính', font=('Tahoma', 11), command=calculateTFW)
            btnTinhtext.grid(row=15, column=1)

            labelTFW = Label(frame9, text='Hệ số KT-CN (TFW) = ', font=('Tahoma',11))
            labelTFW.grid(row=15, column=2, sticky='w')

            labelValueTFW = Label(frame9, text='', font=('Tahoma',11))
            labelValueTFW.grid(row=15, column=3)

            labelTCF = Label(frame9, text='Hệ số phức tạp về KT - CN: TCF = 0.6 + (0.01 x TFW) = ', font=('Tahoma',11))
            labelTCF.grid(row=16, column=2, sticky='w')
            labelValueTCF = Label(frame9, text='', font=('Tahoma',11))
            labelValueTCF.grid(row=16, column=3)

        #hàm tính toán giá trị EF và P
        def calculateEF_P(self):
            frame8 = Frame(self)
            frame8.pack(fill=X, padx=25)
            labelTCFhead = Label(frame8, text="Tính toán hệ số phức tạp môi trường (EF) và nội suy thời gian lao động (P)", font=('Tahoma', 14))
            labelTCFhead.pack(side=TOP)

            frame9 = Frame(self)
            frame9.pack(fill=X, padx=25)

            #cột 1 - STT
            label01 = Label(frame9, text='TT', font=('Tahoma',11))
            label01.grid(row=1, column=1)

            label11 = Label(frame9, text='1', font=('Tahoma',11))
            label11.grid(row=2, column=1)

            label21 = Label(frame9, text='2', font=('Tahoma',11))
            label21.grid(row=3, column=1)

            label31 = Label(frame9, text='3', font=('Tahoma',11))
            label31.grid(row=4, column=1)

            label41 = Label(frame9, text='4', font=('Tahoma',11))
            label41.grid(row=5, column=1)

            label51 = Label(frame9, text='5', font=('Tahoma',11))
            label51.grid(row=6, column=1)

            label61 = Label(frame9, text='6', font=('Tahoma',11))
            label61.grid(row=7, column=1)

            label71 = Label(frame9, text='7', font=('Tahoma',11))
            label71.grid(row=8, column=1)

            label81 = Label(frame9, text='8', font=('Tahoma',11))
            label81.grid(row=9, column=1)

            #cột 2 - Các hệ số
            label02 = Label(frame9, text='Các hệ số', font=('Tahoma',11))
            label02.grid(row=1, column=2, sticky='w')

            label12 = Label(frame9, anchor="w",text="Áp dụng quy trình RUP và hiểu biết về RUP", font=('Tahoma',11))
            label12.grid(row=2, column=2, sticky='w')

            label22 = Label(frame9, anchor="w",text="Có kinh nghiệm về ứng dụng tương tự", font=('Tahoma',11))
            label22.grid(row=3, column=2, sticky='w')

            label32 = Label(frame9, anchor="w",text="Có kinh nghiệm về hướng đối tượng", font=('Tahoma',11))
            label32.grid(row=4, column=2, sticky='w')

            label42 = Label(frame9, text="Có khả năng lãnh đạo nhóm", font=('Tahoma',11))
            label42.grid(row=5, column=2, sticky='w')

            label52 = Label(frame9, text="Tính chất năng động", font=('Tahoma',11))
            label52.grid(row=6, column=2, sticky='w')

            label62 = Label(frame9, text='Độ ổn định của các yêu cầu', font=('Tahoma',11))
            label62.grid(row=7, column=2, sticky='w')

            label72 = Label(frame9, text="Sử dụng nhân viên làm bán thời gian", font=('Tahoma',11))
            label72.grid(row=8, column=2, sticky='w')

            label82 = Label(frame9, text="Dùng ngôn ngữ lập trình loại khó", font=('Tahoma',11))
            label82.grid(row=9, column=2, sticky='w')


            #cột 3 - Trọng số
            label03 = Label(frame9, text='Trọng số', font=('Tahoma',11))
            label03.grid(row=1, column=3)

            label13 = Label(frame9, text='1.5', font=('Tahoma',11))
            label13.grid(row=2, column=3)

            label23 = Label(frame9, text='0.5', font=('Tahoma',11))
            label23.grid(row=3, column=3)

            label33 = Label(frame9, text='1', font=('Tahoma',11))
            label33.grid(row=4, column=3)

            label43 = Label(frame9, text='0.5', font=('Tahoma',11))
            label43.grid(row=5, column=3)

            label53 = Label(frame9, text='1', font=('Tahoma',11))
            label53.grid(row=6, column=3)

            label63 = Label(frame9, text='2', font=('Tahoma',11))
            label63.grid(row=7, column=3)

            label73 = Label(frame9, text='-1', font=('Tahoma',11))
            label73.grid(row=8, column=3)

            label83 = Label(frame9, text='-1', font=('Tahoma',11))
            label83.grid(row=9, column=3)

            #cột 4 - Giá trị xếp hạng
            label04 = Label(frame9, text='Giá trị xếp hạng', font=('Tahoma',11))
            label04.grid(row=1, column=4)

            entry14 = Entry(frame9, width=5)
            entry14.grid(row=2, column=4)
            
            entry24 = Entry(frame9, width=5)
            entry24.grid(row=3, column=4)

            entry34 = Entry(frame9, width=5)
            entry34.grid(row=4, column=4)

            entry44 = Entry(frame9, width=5)
            entry44.grid(row=5, column=4)

            entry54 = Entry(frame9, width=5)
            entry54.grid(row=6, column=4)

            entry64 = Entry(frame9, width=5)
            entry64.grid(row=7, column=4)

            entry74 = Entry(frame9, width=5)
            entry74.grid(row=8, column=4)

            entry84 = Entry(frame9, width=5)
            entry84.grid(row=9, column=4)

            def calEFW():
                listWeights = [1.5,0.5,1,0.5,1,2,-1,-1]
                float1 = float(entry14.get())
                float2 = float(entry24.get())
                float3 = float(entry34.get())
                float4 = float(entry44.get())
                float5 = float(entry54.get())
                float6 = float(entry64.get())
                float7 = float(entry74.get())
                float8 = float(entry84.get())
                floatList = [float1, float2, float3, float4, float5, float6, float7, float8]
                EFW = 0
                for i in range(len(listWeights)):
                    EFW += listWeights[i] * floatList[i]

                ES = 0
                
                S_noisuy_ketqua = {
                    '<=0': 0,
                    '>0' : 0.05,
                    '>1' : 0.1,
                    '>2' : 0.6,
                    '>3' : 1
                }

                for i in range(len(listWeights)):
                    kq = listWeights[i] * floatList[i]
                    if kq <= 0:
                        ES += 0
                    elif kq <= 1:
                        ES += 0.05
                    elif kq <= 2:
                        ES += 0.1
                    elif kq <= 3:
                        ES+= 0.6
                    elif kq > 3:
                        ES += 1
                


                #ES = sum(S_noisuy)
                P_noisuy_ES = {
                    '<1': 48,
                    '>=1': 32,
                    '>=3': 20
                }
                P = 0

                if ES < 1:
                    P = 48
                elif ES < 3:
                    P = 32
                else:
                    P = 20

                EF = 1.4 + (-0.03 * EFW)

                labelValueEFW.configure(text=str(EFW))
                labelValueEF.configure(text=str(EF))
                labelValueES.configure(text=str(ES))
                labelValueP.configure(text=str(P))

                labelEFfill.configure(text=str(EF))
                labelP.configure(text=str(P))

        

            btnTinhtext = Button(frame9, text='Tính', font=('Tahoma', 11), command=calEFW)
            btnTinhtext.grid(row=10, column=1)

            labelEFW = Label(frame9, text="Hệ số tác động môi trường và nhóm làm việc (EFW): ", font=('Tahoma',11))
            labelEFW.grid(row=10, column=2, sticky='w')
            labelValueEFW = Label(frame9, text='', font=('Tahoma',11))
            labelValueEFW.grid(row=10, column=3)

            labelEF = Label(frame9, text="Hệ số phức tạp về môi trường EF = 1.4 + (-0.03 x EFW) =", font=('Tahoma',11))
            labelEF.grid(row=11, column=2, sticky='w')
            labelValueEF = Label(frame9, text='', font=('Tahoma',11))
            labelValueEF.grid(row=11, column=3)

            labelES = Label(frame9, text="Độ ổn định kinh nghiệm (ES): ", font=('Tahoma',11))
            labelES.grid(row=12, column=2, sticky='w')
            labelValueES = Label(frame9, text='', font=('Tahoma',11))
            labelValueES.grid(row=12, column=3)

            labelPtext = Label(frame9, text="Nội suy thời gian lao động (P): ", font=('Tahoma',11))
            labelPtext.grid(row=13, column=2, sticky='w')
            labelValueP = Label(frame9, text='', font=('Tahoma',11))
            labelValueP.grid(row=13, column=3)

        #hàm giao diện H
        def calculateH(self):
            frame8 = Frame(self)
            frame8.pack(fill=X, padx=25)
            labelTCFhead = Label(frame8, text="Bảng tính toán hệ số phức tạp KT-CN", font=('Tahoma', 14))
            labelTCFhead.pack(side=TOP)

            frame9 = Frame(self)
            frame9.pack(fill=X, padx=25)

            #cột 1 - STT
            label01 = Label(frame9, text='TT', font=('Tahoma',11))
            label01.grid(row=1, column=1)

            label11 = Label(frame9, text='1', font=('Tahoma',11))
            label11.grid(row=2, column=1)

            label21 = Label(frame9, text='2', font=('Tahoma',11))
            label21.grid(row=3, column=1)

            label31 = Label(frame9, text='3', font=('Tahoma',11))
            label31.grid(row=4, column=1)

            label41 = Label(frame9, text='4', font=('Tahoma',11))
            label41.grid(row=5, column=1)

            label51 = Label(frame9, text='5', font=('Tahoma',11))
            label51.grid(row=6, column=1)


            #cột 2 -'Mức lương/tháng (đồng)'
            label02 = Label(frame9, text='Mức lương/tháng (đồng)', font=('Tahoma',11))
            label02.grid(row=1, column=2, sticky='w')

            entry12 = Entry(frame9, width=10)
            entry12.grid(row=2, column=2)
            
            entry22 = Entry(frame9, width=10)
            entry22.grid(row=3, column=2)

            entry32 = Entry(frame9, width=10)
            entry32.grid(row=4, column=2)

            entry42 = Entry(frame9, width=10)
            entry42.grid(row=5, column=2)

            entry52 = Entry(frame9, width=10)
            entry52.grid(row=6, column=2)


            #cột 3 - Trọng số
            label03 = Label(frame9, text='Số lượng cán bộ', font=('Tahoma',11))
            label03.grid(row=1, column=3)

            entry13 = Entry(frame9, width=10)
            entry13.grid(row=2, column=3)
            
            entry23 = Entry(frame9, width=10)
            entry23.grid(row=3, column=3)

            entry33 = Entry(frame9, width=10)
            entry33.grid(row=4, column=3)

            entry43 = Entry(frame9, width=10)
            entry43.grid(row=5, column=3)

            entry53 = Entry(frame9, width=10)
            entry53.grid(row=6, column=3)


            def calculateH():
                float1 = float(entry12.get())
                float2 = float(entry22.get())
                float3 = float(entry32.get())
                float4 = float(entry42.get())
                float5 = float(entry52.get())
                float6 = float(entry13.get())
                float7 = float(entry23.get())
                float8 = float(entry33.get())
                float9 = float(entry43.get())
                float10 = float(entry53.get())

                floatListLuong = [float1, float2, float3, float4, float5]
                floatListCanbo = [float6, float7, float8, float9, float10]
                TongLuongThang = 0
                for i in range(len(floatListLuong)):
                    TongLuongThang += floatListLuong[i] * floatListCanbo[i]
                
                LuongBQNguoi_thang = TongLuongThang/(sum(floatListCanbo)) 
                H = (LuongBQNguoi_thang/26) / 8
                labelValueTongLuong.configure(text=str(TongLuongThang))
                labelValueLuongBinhQuan.configure(text=str(LuongBQNguoi_thang))
                labelValueH.configure(text=str(H))
                labelHcal.configure(text=str(H))
                

            btnTinhtext = Button(frame9, text='Tính', font=('Tahoma', 11), command=calculateH)
            btnTinhtext.grid(row=7, column=1)

            labelTongLuong = Label(frame9, text='Tổng chi lương/tháng		 = ', font=('Tahoma',11))
            labelTongLuong.grid(row=7, column=2, sticky='w')

            labelValueTongLuong = Label(frame9, text='', font=('Tahoma',11))
            labelValueTongLuong.grid(row=7, column=3)

            labelLuongBQ = Label(frame9, text='Mực lương bình quân/người/tháng = ', font=('Tahoma',11))
            labelLuongBQ.grid(row=8, column=2, sticky='w')
            labelValueLuongBinhQuan = Label(frame9, text='', font=('Tahoma',11))
            labelValueLuongBinhQuan.grid(row=8, column=3)

            labelLuongH = Label(frame9, text='H = ', font=('Tahoma',11))
            labelLuongH.grid(row=9, column=2, sticky='w')
            labelValueH = Label(frame9, text='', font=('Tahoma',11))
            labelValueH.grid(row=9, column=3)

        #hàm tính toán giá trị EF và P


        #hàm mở cửa số TBF
        def openNewWindowTBF():
            newWindow = Toplevel(root)
            newWindow.title("New Window")
 
            newWindow.geometry("400x400+300+300")

            TBFCalculate(self=newWindow)
 
    
        #Hàm mở cửa số TAW
        def openNewWindowTAW():
            newWindow = Toplevel(root)
            newWindow.title("New Window")
 
            newWindow.geometry("400x400+300+300")

            TAWCalculate(self=newWindow)

        #Hàm mở cửa số TCF
        def openNewWindowTCF():
            newWindow = Toplevel(root)
            newWindow.title("New Window")
 
            newWindow.geometry("800x500+300+300")

            TCFCalculate(self=newWindow)

        #Hàm mở cửa sổ tính EF và P
        def openNewWindowEF_P():
            newWindow = Toplevel(root)
            newWindow.title("New Window")
 
            newWindow.geometry("800x500+300+300")

            calculateEF_P(self=newWindow)

        #Hàm mở cửa sổ H
        def openNewWindowH():
            newWindow = Toplevel(root)
            newWindow.title("New Window")
 
            newWindow.geometry("800x500+300+300")

            calculateH(self=newWindow)


        def Tinh():
                UUCP = float(label4.cget("text")) + float(label6.cget("text"))
                label8.configure(text=str(UUCP))
                AUCP = UUCP * float(label10.cget("text")) * float(labelEFfill.cget("text"))
                label14.configure(text=str(AUCP))
                E = float(10/6 * AUCP)
                labelE.configure(text=str(E))
                G = float(labelHcal.cget("text")) * 1.4 * E * float(labelP.cget("text"))
                labelG.configure(text=str(G))

        






        TAWButton = Button(frame7, text="TAW", command=openNewWindowTAW)
        TAWButton.pack(side=LEFT, padx=5, pady=5)
        TBFButton = Button(frame7, text="TBF", command=openNewWindowTBF)
        TBFButton.pack(side=LEFT)
        TCFButton = Button(frame7, text="TCF", command=openNewWindowTCF)
        TCFButton.pack(side=LEFT, padx=5, pady=5)
        EFButton = Button(frame7, text="EF", command=openNewWindowEF_P)
        EFButton.pack(side=LEFT)
        HButton = Button(frame7, text="H", command=openNewWindowH)
        HButton.pack(side=LEFT)
        # TAWCalculate()
        # TBFCalculate()
         #Nút Tính
        btnMain = Button(frame6, text="Tính", width=5, command=Tinh)
        btnMain.pack(side=LEFT, padx=40)




        
app = Window(root)
root.mainloop()