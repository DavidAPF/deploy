import openai
import flet
from flet import *

#epi = ["""cambios"""]

openai.api_key = "Api"

  
    
def main(page: Page):
    page.bgcolor=colors.BLACK
    #page.window_full_screen=True
    page.padding=20
    page.expand=True
    txt = Row(alignment=MainAxisAlignment.CENTER,controls=[Text(value="Chat-David",text_align="center",color=colors.WHITE,expand=True,size=40)])
    col = Column(expand=True,controls=[],auto_scroll=True,scroll="always")
    
    
    
    es = TextField(expand=True,multiline=True,color="white",border_color=colors.TRANSPARENT,border_radius=20,text_size=14,bgcolor=colors.GREY_700,height=70,label="Escribe aquí...")
    
    
    #Aqui va la pregunta
    def quest(page):
        est =(f" {es.value}")
        
        
        preg = openai.ChatCompletion.create(model="gpt-4-0613",messages=[{"role":"user", "content": est}])
                                            
                                            
                                           
        resp = preg.choices[0].message.content
        resp_mod = str(resp)
        
        estnew=str(est)
        
        
        user = Row(controls=[Text(f"David: {estnew}",color="white",expand=True,selectable=True,text_align="right",size=18)],alignment=MainAxisAlignment.END)
        gpt = Row(controls=[Text(f"Chat-IA: {resp_mod}",color="white",expand=True,selectable=True,text_align="left",size=18)],alignment=alignment.center_left)
        
        col.controls.append(user)
        col.controls.append(gpt)
        es.value=""
        col.update()
        
   
       
    
    
    but = IconButton(icon=icons.SEND,icon_color=colors.GREEN_500,icon_size=40,on_click=quest)
    ab = Row(controls=[es,but],alignment=MainAxisAlignment.SPACE_BETWEEN)
    
    page.add(txt,
             col,
             ab,
             )
    
flet.app(target=main, view=WEB_BROWSER)