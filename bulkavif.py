J='disabled'
I='Start Conversion'
H=Exception
E=True
import tkinter as B
from tkinter import filedialog as D,messagebox as F,ttk as C
import os as A,threading as K
from PIL import Image
import pillow_avif
def L(source_folder,output_folder,quality,speed,log_callback):
	G=output_folder;D=source_folder;B=log_callback;M='.jpg','.jpeg','.png','.bmp','.tiff','.webp';I=0;J=0;B(f"Starting conversion...\nSource: {D}\nOutput: {G}\n")
	for(F,N,O)in A.walk(D):
		for C in O:
			if C.lower().endswith(M):
				P=A.path.join(F,C);K=A.path.relpath(F,D);L=A.path.join(G,K);A.makedirs(L,exist_ok=E);Q,N=A.path.splitext(C);R=A.path.join(L,f"{Q}.avif");B(f"Converting: {A.path.join(K,C)}")
				try:
					with Image.open(P)as S:S.save(R,format='AVIF',quality=quality,speed=speed)
					I+=1
				except H as T:B(f"  -> ERROR: Could not convert {C}. Reason: {T}");J+=1
			else:B(f"Skipping non-image file: {A.path.join(A.path.relpath(F,D),C)}")
	B(f"\n--- CONVERSION COMPLETE ---");B(f"Successfully converted: {I} file(s)");B(f"Skipped / Errored: {J} file(s)")
class M:
	def __init__(A,root):L='Accent.TButton';K='Browse...';H='10';A.root=root;A.root.title('Made By mukulshr1');A.root.geometry('700x550');A.root.minsize(600,450);A.style=C.Style(A.root);A.style.theme_use('clam');D=C.Frame(A.root,padding=H);D.pack(fill=B.X,padx=10,pady=5);C.Label(D,text='Source Folder:').grid(row=0,column=0,sticky=B.W,padx=5,pady=5);A.source_var=B.StringVar();A.source_entry=C.Entry(D,textvariable=A.source_var,width=60);A.source_entry.grid(row=0,column=1,sticky=B.EW,padx=5,pady=5);A.source_button=C.Button(D,text=K,command=A.select_source_dir);A.source_button.grid(row=0,column=2,padx=5,pady=5);C.Label(D,text='Output Folder:').grid(row=1,column=0,sticky=B.W,padx=5,pady=5);A.output_var=B.StringVar();A.output_entry=C.Entry(D,textvariable=A.output_var,width=60);A.output_entry.grid(row=1,column=1,sticky=B.EW,padx=5,pady=5);A.output_button=C.Button(D,text=K,command=A.select_output_dir);A.output_button.grid(row=1,column=2,padx=5,pady=5);D.columnconfigure(1,weight=1);F=C.Frame(A.root,padding=H);F.pack(fill=B.X,padx=10,pady=5);C.Label(F,text='AVIF Quality (0=Worst, 63=Best):').pack(side=B.LEFT,padx=5);A.quality_var=B.IntVar(value=20);A.quality_slider=C.Scale(F,from_=0,to=63,orient=B.HORIZONTAL,variable=A.quality_var,command=A.update_quality_label);A.quality_slider.pack(side=B.LEFT,fill=B.X,expand=E,padx=5);A.quality_label=C.Label(F,text=f"{A.quality_var.get()}",width=3);A.quality_label.pack(side=B.LEFT,padx=5);A.start_button=C.Button(A.root,text=I,command=A.start_conversion_thread,style=L);A.start_button.pack(pady=10,padx=20,fill=B.X);A.style.configure(L,font=('Helvetica',10,'bold'),foreground='white',background='#0078D7');G=C.LabelFrame(A.root,text='Log',padding=H);G.pack(fill=B.BOTH,expand=E,padx=10,pady=10);A.log_text=B.Text(G,wrap=B.WORD,height=10,state=B.DISABLED);A.log_text.pack(side=B.LEFT,fill=B.BOTH,expand=E);J=C.Scrollbar(G,orient=B.VERTICAL,command=A.log_text.yview);J.pack(side=B.RIGHT,fill=B.Y);A.log_text.config(yscrollcommand=J.set)
	def select_source_dir(B):
		A=D.askdirectory()
		if A:B.source_var.set(A)
	def select_output_dir(B):
		A=D.askdirectory()
		if A:B.output_var.set(A)
	def update_quality_label(A,value):A.quality_label.config(text=f"{int(float(value))}")
	def log_message(A,message):A.log_text.config(state=B.NORMAL);A.log_text.insert(B.END,message+'\n');A.log_text.see(B.END);A.log_text.config(state=B.DISABLED)
	def set_controls_state(A,state):
		if state==J:A.start_button.config(state=B.DISABLED,text='Converting...');A.source_button.config(state=B.DISABLED);A.output_button.config(state=B.DISABLED);A.quality_slider.config(state=B.DISABLED)
		else:A.start_button.config(state=B.NORMAL,text=I);A.source_button.config(state=B.NORMAL);A.output_button.config(state=B.NORMAL);A.quality_slider.config(state=B.NORMAL)
	def start_conversion_thread(A):
		G='Error';C=A.source_var.get();D=A.output_var.get()
		if not C or not D:F.showerror(G,'Please select both a source and an output folder.');return
		if C==D:F.showerror(G,'Source and output folders cannot be the same.');return
		A.log_text.config(state=B.NORMAL);A.log_text.delete(1.,B.END);A.log_text.config(state=B.DISABLED);A.set_controls_state(J);H=A.quality_var.get();I=K.Thread(target=A.run_conversion,args=(C,D,H),daemon=E);I.start()
	def run_conversion(A,source_dir,output_dir,quality):
		try:B=10;L(source_dir,output_dir,quality,B,A.thread_safe_log)
		except H as C:A.thread_safe_log(f"\n--- A CRITICAL ERROR OCCURRED ---");A.thread_safe_log(str(C))
		finally:A.root.after(0,A.set_controls_state,'normal')
	def thread_safe_log(A,message):A.root.after(0,A.log_message,message)
if __name__=='__main__':G=B.Tk();N=M(G);G.mainloop()
