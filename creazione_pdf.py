
import wx
import os
import imghdr
from reportlab.platypus import *
from reportlab.lib import colors
from text_box import rigo_1,rigo_2,rigo_3,rigo_4,rigo_5,rigo_6
from reportlab.pdfgen import canvas



class creazione_pdf(wx.Frame) :
	""""""

	def __init__(self):
		"""Constructor"""
		self.risultato=""
		wx.Frame.__init__(self,None,title="esempio",pos=(600,600))
		self.panello=wx.Panel(self,size=(600,600))
		self.panello.SetBackgroundColour("white")
		self.Rigo_1= rigo_1(self.panello, pos=(20,60))
		self.Rigo_1.set_contenuto("FRANCIS & CO.SRL")
		self.Rigo_2= rigo_2(self.panello, pos=(20,110))
		self.Rigo_2.set_contenuto("VIA FERRANTE,198")
		self.Rigo_3= rigo_3(self.panello, pos=(20,160))
		self.Rigo_3.set_contenuto("80146 NAPOLI ITALY")
		self.Rigo_4= rigo_4(self.panello, pos=(20,210))
		self.Rigo_4.set_contenuto("Tel. 081 530 3921")
		self.Rigo_5= rigo_5(self.panello, pos=(20,260))
		self.Rigo_5.set_contenuto("FAX +39 0815592812 - Email: info@salvatoresantoro.com")
		self.Rigo_6=rigo_6(self.panello, pos=(20,310))
		self.check_box1=wx.RadioButton(self.panello,label="sinistra", pos=(220,430))
		self.check_box1.Hide()
		self.check_box3=wx.RadioButton(self.panello,label="destra", pos=(290,430))
		self.check_box3.Hide()
		bottone=wx.Button(self.panello, label="Salva", pos =(20,350))
		bottone.Bind(wx.EVT_BUTTON,self.creazione_pdf)
		self.consiglio = wx.StaticText(self.panello, label="Scegli la grandezza del testo",pos=(300,20), size=(200,30))
		self.consiglia = wx.StaticText(self.panello, label="Dove vuoi inserire l'immagine",pos=(20,400), size=(200,30))
		wx.StaticText(self.panello,label="Clicca sul bottone 'Scegli' se vuoi inserire un immaggine", pos=(20,400), size=(300,30))
		self.bottone_seleziona=wx.Button(self.panello,label="Scegli", pos=(340, 400))
		self.bottone_seleziona.Bind(wx.EVT_BUTTON,self.seleziona_file)
		self.consiglia.Hide()
		misure = ["8", "12", "16", "20","40","60","80"]
		self.combo1 = wx.ComboBox(self.panello, choices=misure, style=wx.CB_READONLY, value="8",
		pos=(300,60), size=(60,90))
		self.combo2 = wx.ComboBox(self.panello, choices=misure, style=wx.CB_READONLY,value="8",
		pos=(300,110), size=(60,90))
		self.combo3 = wx.ComboBox(self.panello, choices=misure, style=wx.CB_READONLY,value="8",
		pos=(300,160), size=(60,90))
		self.combo4 = wx.ComboBox(self.panello, choices=misure, style=wx.CB_READONLY,value="8",
		pos=(300,210), size=(60,90))
		self.combo5 = wx.ComboBox(self.panello, choices=misure, style=wx.CB_READONLY,value="8",
		pos=(300,260), size=(60,90))
		self.combo6 = wx.ComboBox(self.panello, choices=misure, style=wx.CB_READONLY,value="8",
		pos=(300,310), size=(60,90))


		Font = ["Helvetica", "Helvetica-Bold", "Times-Roman","Times-Bold","Courier","Courier-Bold"]
		self.scelta_font1 = wx.ComboBox(self.panello, choices=Font, style=wx.CB_READONLY, value="Helvetica",
		pos=(380,60), size=(90,90))
		self.scelta_font2 = wx.ComboBox(self.panello, choices=Font, style=wx.CB_READONLY,value="Helvetica",
		pos=(380,110), size=(90,90))
		self.scelta_font3 = wx.ComboBox(self.panello, choices=Font, style=wx.CB_READONLY,value="Helvetica",
		pos=(380,160), size=(90,90))
		self.scelta_font4 = wx.ComboBox(self.panello, choices=Font, style=wx.CB_READONLY,value="Helvetica",
		pos=(380,210), size=(90,90))
		self.scelta_font5 = wx.ComboBox(self.panello, choices=Font, style=wx.CB_READONLY,value="Helvetica",
		pos=(380,260), size=(90,90))
		self.scelta_fontpie = wx.ComboBox(self.panello, choices=Font, style=wx.CB_READONLY,value="Helvetica",
		pos=(380,310), size=(90,90))
		



	def prendere_dati(self,evt):
		""""""
		self.valore1=self.Rigo_1.leggicontenuto()
		self.valore2=self.Rigo_2.leggicontenuto()
		self.valore3=self.Rigo_3.leggicontenuto()
		self.valore4=self.Rigo_4.leggicontenuto()
		self.valore5=self.Rigo_5.leggicontenuto()
		self.valorepie=self.Rigo_6.leggicontenuto()

	def seleziona_file(self,evt):
		""""""
		

		self.consiglia.Show()
		self.check_box1.Show()
		self.check_box3.Show()
		openFileDialog = wx.FileDialog(self.panello, "Open", "", "", "jpeg files (*.jpeg)|*.jpeg   \
		 |png files (*.png)|*.png|All files (*.*)|*.*'",wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
		openFileDialog.ShowModal()
		self.risultato=openFileDialog.GetPath()
		openFileDialog.Destroy()


	def scalaImmagine(self):
		""""""
		
		self.immagine = wx.Image(self.risultato, type=wx.BITMAP_TYPE_ANY)
		altezza_immagine=self.immagine.GetHeight()
		larghezza_immagine=self.immagine.GetWidth()

		if altezza_immagine<=90 and larghezza_immagine <=200:
			return self.immagine
		if altezza_immagine >90:
			Scala1=altezza_immagine/90
			altezza_immagine=altezza_immagine/Scala1
			larghezza_immagine=larghezza_immagine/Scala1
		if larghezza_immagine> 200:
			Scala2=larghezza_immagine/200
			altezza_immagine=altezza_immagine/Scala2
			larghezza_immagine=larghezza_immagine/Scala2
		img_scalata=self.immagine.Scale(larghezza_immagine,altezza_immagine,quality=wx.IMAGE_QUALITY_NORMAL)
		img_scalata.SaveFile("Logo_scalato.jpeg", wx.BITMAP_TYPE_JPEG)
		self.immagine = wx.Image("Logo_scalato.jpeg", type=wx.BITMAP_TYPE_ANY)
		return "Logo_scalato.jpeg"

	def creazione_pdf(self,event):
		""""""
		self.Seleziona_font()
		self.prendere_dati(event)
		self.visualizzaSelezione()
		Grandezza_primo=int(self.size1)
		Grandezza_secondo=int(self.size2)
		Grandezza_terzo=int(self.size3)
		Grandezza_quarto=int(self.size4)
		Grandezza_quinto=int(self.size5)
		Grandezza_pie=int(self.sizepie)
		
		can=canvas.Canvas("Azienda.pdf",pagesize=(595.27,841.89))
		Button_check=self.check_box1.GetValue()

		if Button_check == True and self.risultato != "": #sinistra
			
			x1=200
			x_start = 20 
			y_start = 720
			img=self.scalaImmagine()
			can.drawImage(img,x_start,y_start,width=self.immagine.GetWidth(),height=self.immagine.GetHeight(),preserveAspectRatio=False)
		elif Button_check == False and self.risultato != "":
			x1=30
			x_start =425
			y_start =720 
			img=self.scalaImmagine()
			can.drawImage(img,x_start,y_start,width=self.immagine.GetWidth(),height=self.immagine.GetHeight(),preserveAspectRatio=False)
		else:
			x1=30
			x_start =620
			y_start =720 

		y_testo = 810
		


		can.setFont(self.font1, Grandezza_primo)
		can.drawString(x1,y_testo,("%s"%(self.valore1)))
		
		y_testo-=self.calcolaSpazio(Grandezza_primo)
		can.setFont(self.font2, Grandezza_secondo)
		can.drawString(x1,y_testo,("%s"%(self.valore2)))
		
		y_testo-=self.calcolaSpazio(Grandezza_secondo)
		can.setFont(self.font3, Grandezza_terzo)
		can.drawString(x1,y_testo,("%s"%(self.valore3)))
		
		
		y_testo-=self.calcolaSpazio(Grandezza_terzo)
		can.setFont(self.font4, Grandezza_quarto)
		can.drawString(x1,y_testo,("%s"%(self.valore4)))
		
		y_testo-=self.calcolaSpazio(Grandezza_quarto)
		can.setFont(self.font5, Grandezza_quinto)
		can.drawString(x1,y_testo,("%s"%(self.valore5)))
		
		can.setFont(self.fontpie, Grandezza_pie)
		can.drawString(80,60,("%s"%(self.valorepie)))


		if self.risultato != "":
			img=self.scalaImmagine()
			can.drawImage(img,x_start,y_start,width=self.immagine.GetWidth(),height=self.immagine.GetHeight(),preserveAspectRatio=False)
		can.showPage()
		can.save() 
		os.startfile("Azienda.pdf")



	def visualizzaSelezione(self):
		""""""
		self.size1= self.combo1.GetValue()
		self.size2= self.combo2.GetValue()
		self.size3= self.combo3.GetValue()
		self.size4= self.combo4.GetValue()
		self.size5= self.combo5.GetValue()
		self.sizepie= self.combo6.GetValue()
	def calcolaSpazio(self,n):
		""""""
		x=n*10/8
		
		return x

	def Seleziona_font(self):
		""""""
		
		self.font1= self.scelta_font1.GetValue()
		self.font2= self.scelta_font2.GetValue()
		self.font3= self.scelta_font3.GetValue()
		self.font4= self.scelta_font4.GetValue()
		self.font5= self.scelta_font5.GetValue()
		self.fontpie= self.scelta_fontpie.GetValue()



""""
   Come incollare un immagine su un panello con try and execpt per evitare eventuali errori
   try:
			imagefile = risultato
			data = open(imagefile, "rb").read()
			mostra = cStringIO.StringIO(data)
			bmp = wx.BitmapFromImage( wx.ImageFromStream( mostra ))
			wx.StaticBitmap(, -1, bmp)
		except IOError:
			print "Image file %s not found" % imagefile
			raise SystemExit
"""
if __name__ == "__main__":

	app=wx.App()
	c=creazione_pdf()
	c.SetInitialSize()
	c.CenterOnScreen()
	c.Show()
	app.MainLoop()
