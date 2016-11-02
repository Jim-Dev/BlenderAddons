    #
#The MIT License (MIT)
#
#Copyright (c) 2014 ishidourou
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.
#
#(参考日本語訳：http://sourceforge.jp/projects/opensource/wiki/licenses%2FMIT_licenseより）
#
#Copyright (c) 2014 ishidourou
#
#以下に定める条件に従い、本ソフトウェアおよび関連文書のファイル（以下「ソフトウェア」）
#の複製を取得するすべての人に対し、ソフトウェアを無制限に扱うことを無償で許可します。
#これには、ソフトウェアの複製を使用、複写、変更、結合、掲載、頒布、サブライセンス、
#および/または販売する権利、およびソフトウェアを提供する相手に同じことを許可する権利も
#無制限に含まれます。
#
#上記の著作権表示および本許諾表示を、ソフトウェアのすべての複製または重要な部分に記載
#するものとします。
#
#ソフトウェアは「現状のまま」で、明示であるか暗黙であるかを問わず、何らの保証もなく
#提供されます。ここでいう保証とは、商品性、特定の目的への適合性、および権利非侵害に
#ついての保証も含みますが、それに限定されるものではありません。 作者または著作権者は、
#契約行為、不法行為、またはそれ以外であろうと、ソフトウェアに起因または関連し、あるいは
#ソフトウェアの使用またはその他の扱いによって生じる一切の請求、損害、その他の義務に
#ついて何らの責任も負わないものとします。
#
#
#####################################
# Bone Modeling Helper2 (BMH2) 
#     <Multi-lingual>
#          v.2.12
#  (c)ishidourou 2014
#####################################

#!BPY
import bpy
import re

from bpy.props import *

bl_info = {
    "name": "Bmh2",
    "author": "ishidourou",
    "version": (2, 1),
    "blender": (2, 65, 0),
    "location": "View3D > Toolbar and View3D",
    "description": "Bmh2",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": 'Rigging'}

# message=(English,Japanese,French,Spanish,Portuguese,Russian,Chinese(Traditional),Arabic,German,Italian,Korean,Turkish,Chinese(Simplified),Hindi,Indonesian,Dutch)
class mes():
    title=("Bone Modeling Helper 2.1","ボーンモデリングヘルパー 2.1","Hueso Modeling Helper 2.1","Os Modélisation Helper 2.1","Osso Modelagem Helper 2.1","Кость Моделирование Помощник 2.1","骨建模助手 2.1","العظام النمذجة مساعد 2.1","Knochen-Modeling-Helfer 2.1","Bone Modeling Helper 2.1","뼈 모델링 도우미 2.1","Kemik Modelleme Yardımcısı 2.1","骨建模助手 2.1","अस्थि मॉडलिंग हेल्पर 2.1","Tulang Modeling Helper 2.1","Bone Modeling Helper 2.1")
    subtitle1=("=== For Bone ===","=== ボーン関連 ===","Para objetos de hueso:","Pour objet d'os:","Para objeto óssea:","Для объекта Bone:","骨對象：","العظام:","Für Bone-Objekt:","per osso oggetto:","뼈 개체 :","kemik obje için:","骨对象：","हड्डी वस्तु के लिए:","untuk objek tulang:","voor bot-object:")
    subtitle2=("=== For Mesh ===","=== メッシュ関連 ===","Por objeto de malla:","Pour objet Mesh:","Para objeto Mesh:","Для Mesh объекта:","為網格對象：","مش:","Für Gitterobjekt:","per oggetto mesh:","메쉬 개체 :","örgü nesne için:","为网格对象：","मेष वस्तु के लिए:","untuk objek mesh:","voor netobject:")
    subtitle3=("Add Mirror Modifier:","ミラーモディファイアツール","Agregar espejo modificador:","Ajouter un miroir modificateur:","Adicionar espelho Modifier:","Добавить Mirror Модификатор:","添加鏡面修飾：","اضافة مرآة التعديل:","Hinzufügen Spiegel-Modifier:","Aggiungi mirror modificatore:","거울 수정 추가 :","Ayna değiştirici ekle:","添加镜面修饰：","दर्पण संशोधक करें:","Tambahkan mirror modifier:","Voeg mirror modifier:")
    btn01=("Create Bones from Selected Edges","選択辺からボーンを作成","Crear Huesos de malla seleccionada","Créer Bones sélectionnée de maille","Criar Bones selecionada de Malha","Создание Кости от Выбранный Mesh","從選定的邊創建骨骼","خلق العظام من مش مختارة","Erstellen Sie Knochen von ausgewählten Kanten","Crea Ossa dai bordi selezionati","선택된 가장자리에서 뼈를 만들기","Seçilen kenarlardan Bones oluşturun","从选定的边创建骨骼","चयनित किनारों से हड्डियों बनाएँ","Buat Bones dari tepi yang dipilih","Maak Beenderen van geselecteerde randen")
    btn02a=("Connect Bones","ボーンを接続","Conecte Bones","Connectez Bones","Conecte Bones","Подключите Bones","連骨頭","العظام الاتصال","Verbinden Bones","Collegare Ossa","뼈를 연결","Bones bağlayın","连骨头","हड्डियों को जोड़ने","Hubungkan Bones","aansluiten Bones")
    btn02b=("Unconnect Bones","ボーンを分離","Bones Unconnect","Bones Unconnect","Ossos Unconnect","Unconnect Кости","單獨的骨頭","العظام منفصلة","Bones separaten","Ossa separati","별도의 뼈","ayrı Bones","单独的骨头","अलग हड्डियों","Bones terpisah","aparte Bones")
    btn03=("Create Selected Mirror Bones","選択ミラーボーン作成","Crear Mirror Bones","Créer Miroir Bones","Criar Espelho Bones","Создание зеркальных Bones","建立鏡像骨頭","خلق مرآة العظام","Erstellen Sie Spiegel Knochen","Crea Specchio Ossa","거울 뼈를 만들기","Ayna Bones Oluştur","建立镜像骨头","मिरर हड्डियों बनाएँ","Buat Cermin Bones","Maak Mirror Bones")
    mir_label=("Create Mirror Bones","一括ミラーボーン作成","Create Mirror Bones","Create Mirror Bones","Create Mirror Bones","Create Mirror Bones","Create Mirror Bones","Create Mirror Bones","Create Mirror Bones","Create Mirror Bones","Create Mirror Bones","Create Mirror Bones","Create Mirror Bones","Create Mirror Bones","Create Mirror Bones","Create Mirror Bones")
    mir_bl_btn=("< Right to Left","← 右から左へ","<Delete Left Bones","<Delete Left Bones","<Delete Left Bones","<Delete Left Bones","<Delete Left Bones","<Delete Left Bones","<Delete Left Bones","<Delete Left Bones","<Delete Left Bones","<Delete Left Bones","<Delete Left Bones","<Delete Left Bones","<Delete Left Bones","<Delete Left Bones")
    mir_br_btn=("Left to Right >","左から右へ →","Delete Right Bones>","Delete Right Bones>","Delete Right Bones>","Delete Right Bones>","Delete Right Bones>","Delete Right Bones>","Delete Right Bones>","Delete Right Bones>","Delete Right Bones>","Delete Right Bones>","Delete Right Bones>","Delete Right Bones>","Delete Right Bones>","Delete Right Bones>")
    btn07=("Rename Bones","ボーン名を変更","Cambiar el nombre de los huesos","renommer Bones","renomeie Bones","Переименовать Bones","重命名骨頭","إعادة تسمية العظام","Benennen Bones","rinominare Ossa","뼈의 이름을 바꿉니다","Bones yeniden adlandırma","重命名骨头","हड्डियों का नाम बदलें","Ubah nama Bones","hernoemen Bones")
    btn04=("Create Bevel Curve","ベベルカーブを作成","Crear Bevel Curve","Créer biseau Curve","Criar Curve Bevel","Создание Bevel Curve","創建斜角曲線","خلق شطبة المنحنى","Erstellen Sie Abschrägungskurve","Crea curva Bevel","경사 곡선 만들기","Konik Eğrisi Oluşturma","创建斜角曲线","बेवल वक्र बनाने","Buat Bevel Curve","Creëer Bevel Curve")
    btn05=("Convert to Mesh & Join","メッシュに変換して結合","Convertir en malla y únase","Convertir en Mesh & Join","Converter para Malha & Join","Преобразовать в Mesh & Регистрация","轉換為網狀和合併","بتحويل إلى مش وتاريخ","Convert to Maschen& Join","Conversione in Mesh & Combina","메쉬 및 결합으로 변환","Mesh & Kombine dönüştürme","转换为网格和合并","मेष और कम्बाइन के साथ परिवर्तित","Convert to Mesh & Combine","Converteren naar Mesh & Combineer")
    btn06a=("< Right to Left","← 右から左へ","<De derecha a izquierda","<Droite à gauche","<Direita para a esquerda","<Справа налево","<從右到左","<اليمين إلى اليسار","<Von rechts nach links","<Da destra a sinistra","<오른쪽에서 왼쪽으로","<Sağdan Sola","<从右到左","<छोड़ दिया सही","<Kanan ke Kiri","<Van rechts naar links")
    btn06b=("Left to Right >","左から右へ →","De izquierda a derecha>","De gauche à droite>","Da esquerda para a direita>","Слева направо>","左到右>","من اليسار إلى اليمين>","Von links nach rechts>","Da sinistra a destra>","왼쪽에서 오른쪽>","Sağa sola>","左到右>","दाएँ से बाएँ>","Kiri ke Kanan>","Van links naar rechts>")

    opt_title = ("=== Option ===","=== オプション ===","=== Option ===","=== Option ===","=== Option ===","=== Option ===","=== Option ===","=== Option ===","=== Option ===","=== Option ===","=== Option ===","=== Option ===","=== Option ===","=== Option ===","=== Option ===","=== Option ===")
    opt_btn1 = ("Create Edges from Selected Bones","選択ボーンから辺を作成","Create Edges from Selected Bones","Create Edges from Selected Bones","Create Edges from Selected Bones","Create Edges from Selected Bones","Create Edges from Selected Bones","Create Edges from Selected Bones","Create Edges from Selected Bones","Create Edges from Selected Bones","Create Edges from Selected Bones","Create Edges from Selected Bones","Create Edges from Selected Bones","Create Edges from Selected Bones","Create Edges from Selected Bones","Create Edges from Selected Bones")
    opt_btn2 = ("Select Linked Bones","リンクボーンを選択","Select Linked Bones","Select Linked Bones","Select Linked Bones","Select Linked Bones","Select Linked Bones","Select Linked Bones","Select Linked Bones","Select Linked Bones","Select Linked Bones","Select Linked Bones","Select Linked Bones","Select Linked Bones","Select Linked Bones","Select Linked Bones")
    linkrenum_btn = ("Renumber Linked Bones","リンクボーン番号修正","Renumber Bones","Renumber Bones","Renumber Bones","Renumber Bones","Renumber Bones","Renumber Bones","Renumber Bones","Renumber Bones","Renumber Bones","Renumber Bones","Renumber Bones","Renumber Bones","Renumber Bones","Renumber Bones")

    rmd = ("Not RemDoubles","重複頂点を削除しない","Not RemDoubles","Not RemDoubles","Not RemDoubles","Not RemDoubles","Not RemDoubles","Not RemDoubles","Not RemDoubles","Not RemDoubles","Not RemDoubles","Not RemDoubles","Not RemDoubles","Not RemDoubles","Not RemDoubles","Not RemDoubles")
    blinked = ("Linked","リンク","Linked","Linked","Linked","Linked","Linked","Linked","Linked","Linked","Linked","Linked","Linked","Linked","Linked","Linked")
    bconnect = ("Not Connect","接続しない","Not Connect","Not Connect","Not Connect","Not Connect","Not Connect","Not Connect","Not Connect","Not Connect","Not Connect","Not Connect","Not Connect","Not Connect","Not Connect","Not Connect")

    dlg01=("Ngon","断面の頂点数","Ngon","Ngon","Ngon","Ngon","恩貢","Ngon","Ngon","Ngon","Ngon","Ngon","恩贡","ngon","Ngon","Ngon")
    modname=("Ngon","ミラー","Ngon","Ngon","Ngon","Ngon","恩貢","Ngon","Ngon","Ngon","Ngon","Ngon","恩贡","ngon","Ngon","Ngon")
    warning=("Warning","ウォーニング","advertencia","avertissement","aviso","предупреждение","警告","تحذير","Warnung","Avvertenza","경고","uyarı","警告","चेतावनी","peringatan","waarschuwing")
    select_mesh=("Please Select Mesh Object.","メッシュオブジェクトを選択してください","Seleccione Mesh Objeto.","S'il vous plaît Choisir Mesh objet.","Selecione malha objeto.","Выберите Mesh Object.","請選擇網格對象。","يرجى تحديد كائن مش.","Bitte wählen Gitterobjekt.","Selezionare oggetto mesh.","메쉬 개체를 선택하십시오.","Kafes nesnesini seçin Lütfen.","请选择网格对象。","मेष वस्तु का चयन करें.","Silakan Pilih objek mesh.","Selecteer netobject.")
    select_mesh_curve=("Please Select Mesh or Curve Object.","メッシュかカーブオブジェクトを選択してください","Seleccione Mesh o Curva de objetos.","S'il vous plaît Choisir Mesh ou objet courbe.","Selecione malha ou Curva objeto.","Выберите Mesh или Curve Object.","請選擇網狀或曲線對象。","الرجاء الإختيار مش أو كائن المنحنى.","Bitte wählen Netz oder Kurvenobjekt.","Seleziona mesh o oggetto curva.","메쉬 또는 곡선 개체를 선택하십시오.","Örgü veya eğri nesne Seçiniz.","请选择网格或曲线对象。","मेष या वक्र वस्तु का चयन करें.","Silakan Pilih mesh atau objek kurva.","Selecteer gaas of curve object.")
    select_curve=("Please Select Curve Object.","カーブオブジェクトを選択してください","Seleccione Curva de objetos.","S'il vous plaît Choisir l'objet de la courbe.","Selecione Curve objeto.","Выберите Curve Object.","請選擇曲線對象。","يرجى تحديد كائن المنحنى.","Bitte wählen Kurvenobjekt.","Selezionare oggetto curva.","곡선 개체를 선택하십시오.","Eğri nesne seçin Lütfen.","请选择曲线对象。","वक्र वस्तु का चयन करें.","Silakan Pilih objek kurva.","Selecteer curve object.")
    select_edge=("Please Select Edges.","辺を選択してください","Seleccione Bordes.","S'il vous plaît Choisir bords.","Selecione Edges.","Выберите Края.","請選擇邊緣。","الرجاء الإختيار الحواف.","Bitte wählen Kanten.","Selezionare spigolo.","모서리를 선택하십시오.","Kenarı seçin Lütfen.","请选择边缘。","बढ़त का चयन करें.","Silakan Pilih tepi.","Selecteer de rand.")
    select_armature=("Please Select Armature","アーマチュアを選択してください","Seleccione la armadura","S'il vous plaît Choisir Armature","Selecione Armação","Выберите Арматура","請選擇電樞","الرجاء الإختيار حديد التسليح","Bitte wählen Armature","Si prega di selezionare Armature","전기자를 선택하세요","Armatür seçiniz","请选择电枢","आर्मेचर का चयन करें","Silakan pilih Amature","Selecteer Armature")
    edit_armature=("The mode was changed.Please Select Bones","編集モードに変更。対象ボーンを選択してください","El modo fue cambiado. Seleccione Bones","Le mode a été changé. S'il vous plaît Choisir Bones","O modo foi alterado. Selecione Bones","Режим была изменена. Выберите Bones","該模式被改變。請選擇骨頭","تم تغيير الوضع. الرجاء الإختيار العظام","Der Modus geändert wurde. Bitte wählen Bones","La modalità è stata cambiata. Seleziona ossa","모드가 변경되었습니다. 뼈를 선택하세요","Modu değiştirildi. Kemikleri Seçiniz","该模式被改变。请选择骨头","मोड बदल गया था. हड्डियों का चयन करें कृपया","Modus berubah. Silakan Pilih tulang","De wijze werd veranderd. Selecteer botten")
    edit_edges=("The mode was changed.Please Select Edges.","編集モードに変更。辺を選択してください","El modo fue cambiado. Seleccione Bordes.","Le mode a été changé. S'il vous plaît Choisir bords.","O modo foi alterado. Selecione Edges.","Режим была изменена. Выберите Края.","該模式被改變。請選擇邊緣。","تم تغيير الوضع. الرجاء الإختيار الحواف.","Der Modus geändert wurde. Bitte wählen Kanten.","La modalità è stata cambiata. Selezionare spigolo.","모드가 변경되었습니다. 모서리를 선택하십시오.","Modu değiştirildi. Kenarı seçin Lütfen.","该模式被改变。请选择边缘。","मोड बदल गया था. बढ़त का चयन करें.","Modus berubah. Silakan Pilih tepi.","De wijze werd veranderd. Selecteer de rand.")
    linkrenum=("Please select only one bone at the tip.","先端のボーンを一本だけ選択してください","Please select only one bone at the tip.","Please select only one bone at the tip.","Please select only one bone at the tip.","Please select only one bone at the tip.","Please select only one bone at the tip.","Please select only one bone at the tip.","Please select only one bone at the tip.","Please select only one bone at the tip.","Please select only one bone at the tip.","Please select only one bone at the tip.","Please select only one bone at the tip.","Please select only one bone at the tip.","Please select only one bone at the tip.","Please select only one bone at the tip.")

    #========= for bone rename =========

    trns = ("Translate into","翻訳","traducir","traduire","traduzir","переводить","翻譯","ترجم","übersetzen","tradurre","번역","çevirmek","翻译","अनुवाद करना","menterjemahkan","vertalen")
    str = ("Input String:","文字列入力:","Cuerdas de entrada:","Cordes d'entrée:","Cordas de entrada:","Входные строки:","輸入字符串：","سلاسل الإدخال","Eingangs Saiten:","Stringhe di ingresso:","입력 문자열 :","Giriş Strings:","输入字符串：","इनपुट तार:","Strings masukan:","Input Strings:")

    rendata = (
    #--------- control (top)-------
(("Control(top):","コントローラ(前方):","Controller ( frontal) :","Contrôleur (avant) :","Controller ( frente ) :","Контроллер (передние):","控制器（前）：","تحكم ( الجبهة):","Controller ( vorn):","Controller ( anteriore) :","컨트롤러 ( 전방 ) :","Kontrolör (ön ) :","控制器（前）：","नियंत्रक ( सामने ) :","Controller ( depan) :","Controller (voor) :"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("IK_","IK_","IK_","IK_","IK_","IK_","IK_","IK_","IK_","IK_","IK_","IK_","IK_","IK_","IK_","IK_"),
("Controller_","コントローラ_","_ Controller","contrôleur _","Controlador _","контроллер _","控制器_","تحكم _","Controller- _","controllore _","컨트롤러 _","kontrolör _","控制器_","नियंत्रक _","kontroler _","controller _"),
("Constraint_","コンストレイント_","Restricción _","Contrainte _","Restrição _","Ограничение _","約束_","القيد _","Constraint _","Vincolo _","구속 조건 _","Kısıtlama _","约束_","बाधा _","Kendala _","Constraint _"),
("Target_","ターゲット_","Objetivo _","cible _","alvo _","Цель _","目標_","استهداف _","Ziel _","obiettivo _","대상 _","_ hedef","目标_","_ लक्षित करें","targetkan _","Target _"),
("Pole_","ポール_","Paul _","Paul _","Paul _","Павел _","保羅_","بول _","Paul _","Paul _","폴 _","Paul _","保罗_","पॉल _","Paul _","Paul _"),
("PoleTarget_","ポールターゲット_","Paul objetivo _","Paul cible _","Alvo Paul _","Павел целевой _","保羅的目標_","بول الهدف _","Paul Ziel _","Paul obiettivo _","폴 대상 _","Paul hedef _","保罗的目标_","पॉल लक्ष्य _","Paul Target _","Paul doel _"),
("Point_of_gaze_","注視点_","Nota perspectiva _","Remarque perspective _","Nota perspectiva _","Примечание перспективу _","注意視角_","ملاحظة منظور _","Hinweis Perspektive _","Nota prospettiva _","참고 관점 _","_ Perspektif Not","注意视角_","_ परिप्रेक्ष्य नोट","Catatan perspektif _","Opmerking perspectief _"),
("Root_Bone","ルートボーン","hueso Root","racine os","óssea Root","Корневая кость","根骨","العظام الجذر","Wurzelknochen","Root osso","루트 번","kök kemik","根骨","जड़ हड्डी","tulang akar","Root bot"),
("Root","ルート","raíz","racine","raiz","корень","根","جذر","Wurzel","radice","루트","kök","根","जड़","akar","wortel"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-")),
#------------body---------
(("BodyParts:","胴体:","Cuerpo:","corps:","corpo :","Кузов:","身體：","الجسم :","Body:","corpo :","동체 :","gövde :","身体：","शरीर:","tubuh :","body :"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("Head","頭","cabeza","tête","cabeça","руководитель","頭","رئيس","Kopf","testa","머리","kafa","头","सिर","kepala","hoofd"),
("Hair","髪","pelo","cheveux","cabelo","волосы","發","شعر","Haar","capelli","머리","saç","发","बाल","rambut","haar"),
("Face","顔","cara","face","cara","лицо","臉","وجه","Gesicht","faccia","얼굴","yüz","脸","चेहरा","wajah","gezicht"),
("Neck","首","cuello","cou","pescoço","шея","頸部","العنق","Hals","collo","목","boyun","颈部","गरदन","leher","nek"),
("Shoulder","肩","hombro","épaule","ombro","плечо","肩","كتف","Schulter","spalla","어깨","omuz","肩","कंधा","bahu","schouder"),
("Clavicle","鎖骨","clavícula","clavicule","clavícula","ключица","鎖骨","ترقوة","Schlüsselbein","clavicola","쇄골","klavikula","锁骨","हंसली","tulang selangka","sleutelbeen"),
("Breast","胸","pecho","sein","peito","грудь","乳房","ثدي","Brust","seno","가슴","meme","乳房","स्तन","payudara","borst"),
("Mammary","乳房","pecho","sein","peito","грудь","乳房","ثدي","Brust","seno","유방","meme","乳房","स्तन","payudara","borst"),
("Nipple","乳首","pezón","mamelon","mamilo","ниппель","乳頭","حلمة الثدي","Nippel","capezzolo","젖꼭지","meme","乳头","चुसनी","puting susu","tepel"),
("Belly","腹","vientre","ventre","barriga","живот","肚","بطن","Bauch","pancia","배","göbek","肚","पेट","perut","buik"),
("Body","胴","cuerpo","corps","corpo","тело","體","هيئة","Körper","corpo","몸통","vücut","体","शरीर","tubuh","lichaam"),
("Waist","腰","cadera","hanche","quadril","бедро","臀部","ورك","Hüfte","anca","허리","kalça","臀部","कमर","panggul","heup"),
("Ass","尻","culo","cul","bunda","задница","屁股","حمار","Arsch","culo","엉덩이","göt","屁股","गधा","pantat","ezel"),
("Hip","臀部","nalgas","fesses","nádegas","ягодицы","臀部","ردفان","Gesäß","natiche","엉덩이","kalça","臀部","नितम्ब","pantat","zitvlak"),
("Root","ルート","raíz","racine","raiz","корень","根","جذر","Wurzel","radice","루트","kök","根","जड़","akar","wortel"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-")),
#------------Arm---------
(("ArmParts:","腕:","Brazo :","Armez :","Arme :","Вооружитесь :","手臂：","الذراع :","Arm :","braccio :","팔 :","Arm :","手臂：","शाखा:","lengan :","arm :"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("Arm","腕","brazo","bras","braço","рука","臂","ذراع","Arm","braccio","팔","kol","臂","बांह","lengan","arm"),
("Elbow","肘","codo","coude","cotovelo","локоть","彎頭","كوع","Ellbogen","gomito","팔꿈치","dirsek","弯头","कोहनी","siku","elleboog"),
("Upper_arm","上腕","brazo","bras","braços","Плечи","膀臂","العضد","Oberarm","braccio","상완","üst kol","膀臂","ऊपरी बांह","lengan atas","bovenarm"),
("Lower_arm","下腕","Bajo el brazo","bras inférieur","Abaixe o braço","Нижний рычаг","下臂","الذراع السفلى","Unterarm","braccio inferiore","팔뚝","alt kol","下臂","कम हाथ","lengan bawah","onderarm"),
("Forearm","前腕","antebrazo","avant bras","antebraço","предплечье","前臂","ساعد","Unterarm","avambraccio","팔뚝","kolun ön kısmı","前臂","प्रकोष्ठ","lengan bawah","onderarm"),
("Large_biceps","力瘤","grandes bíceps","grandes biceps","grandes bíceps","Большие бицепсы","大二頭肌","العضلة ذات الرأسين الكبيرة","Große Bizeps","grandi bicipiti","알통","büyük pazı","大二头肌","बड़े मछलियां","bisep besar","grote biceps"),
("Large_biceps","力こぶ","bíceps","biceps","bíceps","бицепс","肱二頭肌","العضلة ذات الرأسين","Bizeps","bicipite","알통","biceps","肱二头肌","द्विशिरस्क","bisep","biceps"),
("Hand","手","mano","main","mão","рука","手","يد","Hand","mano","손","el","手","हाथ","tangan","hand"),
("Wrist","手首","muñeca","poignet","pulso","запястье","腕","معصم","Handgelenk","polso","손목","bilek","腕","कलाई","pergelangan tangan","pols"),
("Palm","手のひら","palma","paume","palma","пальма","手掌","كف","Palme","palma","손바닥","palmiye","手掌","हथेली","kelapa sawit","palm"),
("Palm","掌","palma","paume","palma","пальма","手掌","كف","Palme","palma","손바닥","palmiye","手掌","हथेली","kelapa sawit","palm"),
("Back_of_thehand","手の甲","parte posterior de la mano","dos de la main","dorso da mão","тыльная сторона руки","手背","ظهر اليد","Zurück von der Hand","dorso della mano","손등","geriel","手背","पीछे हाथ का","kembali tangan","rug van de hand"),
("Finger","指","dedo","doigt","dedo","палец","手指","إصبع","Finger","dito","손가락","parmak","手指","उंगली","jari","vinger"),
("Thumb","親指","pulgar","pouce","polegar","большой палец руки","拇指","إبهام اليد","Daumen","pollice","엄지","başparmak","拇指","अंगूठा","jempol","duim"),
("Index_finger","人差し指","dedo índice","index","indicador","указательный палец","食指","السبابة","Zeigefinger","indice","집게 손가락","işaret parmağı","食指","तर्जनी","jari telunjuk","wijsvinger"),
("Middle_finger","中指","dedo del corazón","majeur","dedo médio","средний палец","中指","الاصبع الوسطى","Mittelfinger","dito medio","중지","orta parmak","中指","बीच की उँगली","jari tengah","middelvinger"),
("Ring_finger","薬指","dedo anular","Annulaire","dedo anular","Безымянный палец","戒指","إصبع الخاتم","Ringfinger","anulare","약지","yüzük parmağı","戒指","अनामिका","jari manis","ringvinger"),
("Little_finger","小指","dedo meñique","petit doigt","dedinho","мизинец","小指","الأصبع الصغير","Kleiner Finger","mignolo","새끼 손가락","serçe parmak","小指","कनिष्ठा","jari kelingking","pink"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-")),
#------------Foot---------
(("FootParts:","足:","Pies:","pieds :","Pés :","Ноги :","腳：","قدم :","Füße:","piedi:","다리 :","Ayaklar :","脚：","पैर:","kaki:","voeten :"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("Foot","足","pie","pied","pé","фут","腳","قدم","Fuß","piede","다리","ayak","脚","पैर","kaki","voet"),
("Thigh","太股","muslo","cuisse","coxa","бедро","大腿","فخذ","Schenkel","coscia","허벅지","uyluk","大腿","जांघ","paha","dij"),
("Thigh","太もも","Los muslos","les cuisses","as coxas","бедра","大腿","الفخذين","die Schenkel","le cosce","허벅지","uyluk","大腿","जांघों","paha","de dijen"),
("Knee","膝","rodilla","genou","joelho","колено","膝蓋","ركبة","Knie","ginocchio","무릎","diz","膝盖","घुटना","lutut","knie"),
("Knee","ひざ","rodilla","genou","joelho","колено","膝蓋","ركبة","Knie","ginocchio","무릎","diz","膝盖","घुटना","lutut","knie"),
("Shin","脛","espinilla","tibia","canela","голень","脛","قصبة","Schienbein","stinco","정강이","incik","胫","पिंडली","garas","scheenbeen"),
("Shank","すね","espinilla","tibia","canela","голень","脛","قصبة","Schienbein","stinco","정강이","incik","胫","पिंडली","garas","scheenbeen"),
("Calf","ふくらはぎ","ternero","veau","bezerro","теленок","小牛","عجل","Kalb","vitello","장딴지","buzağı","小牛","बछड़ा","betis","kalf"),
("Ankle","足首","tobillo","cheville","tornozelo","лодыжка","腳踝","الكاحل","Knöchel","caviglia","발목","ayak bileği","脚踝","टखना","pergelangan kaki","enkel"),
("Malleolus","踝","tobillo","cheville","tornozelo","лодыжка","腳踝","الكاحل","Knöchel","caviglia","踝","ayak bileği","脚踝","टखना","pergelangan kaki","enkel"),
("Malleolus","くるぶし","tobillo","cheville","tornozelo","лодыжка","腳踝","الكاحل","Knöchel","caviglia","발목","ayak bileği","脚踝","टखना","pergelangan kaki","enkel"),
("Sole_of_the_foot","足裏","planta del pie","plante du pied","sola do pé","подошвы ноги","腳的鞋底","باطن القدم","Fußsohle","pianta del piede","발바닥","ayak tabanı","脚的鞋底","पैर की एकमात्र","telapak kaki","zool van de voet"),
("Heel","踵","tacón","talon","calcanhar","каблук","腳跟","كعب","Ferse","tacco","뒤꿈치","topuk","脚跟","एड़ी","tumit","hiel"),
("Heel","かかと","tacón","talon","calcanhar","каблук","腳跟","كعب","Ferse","tacco","발 뒤꿈치","topuk","脚跟","एड़ी","tumit","hiel"),
("Toe","つま先","dedo del pie","orteil","dedo do pé","носок","腳趾","اصبع القدم","Zeh","punta","발가락","ayak parmağı","脚趾","पैर की अंगुली","kaki","teen"),
("Top_of_the_foot","足の甲","La parte superior del pie","Le dessus du pied","A parte superior do pé","В верхней части стопы","腳的頂端","الجزء العلوي من القدم","Die Oberseite des Fußes","La parte superiore del piede","발등","Ayağın üst","脚的顶端","पैर के ऊपर","Bagian atas kaki","De bovenkant van de voet"),
("Arch_of_a_foot","土踏まず","Arco de un pie","arc d'un pied","Arco de um pé","Арка ноги","腳心","قوس القدم","Arch von einem Fuß","arco di un piede","흙 밟지 않고","bir ayağın kemer","脚心","एक पैर के आर्क","Arch of kaki","boog van een voet"),
("Finger","指","dedo","doigt","dedo","палец","手指","إصبع","Finger","dito","손가락","parmak","手指","उंगली","jari","vinger"),
("Thumb","親指","pulgar","pouce","polegar","большой палец руки","拇指","إبهام اليد","Daumen","pollice","엄지","başparmak","拇指","अंगूठा","jempol","duim"),
("Index_finger","人差し指","dedo índice","index","indicador","указательный палец","食指","السبابة","Zeigefinger","indice","집게 손가락","işaret parmağı","食指","तर्जनी","jari telunjuk","wijsvinger"),
("Middle_finger","中指","dedo del corazón","majeur","dedo médio","средний палец","中指","الاصبع الوسطى","Mittelfinger","dito medio","중지","orta parmak","中指","बीच की उँगली","jari tengah","middelvinger"),
("Ring_finger","薬指","dedo anular","Annulaire","dedo anular","Безымянный палец","戒指","إصبع الخاتم","Ringfinger","anulare","약지","yüzük parmağı","戒指","अनामिका","jari manis","ringvinger"),
("Little_finger","小指","dedo meñique","petit doigt","dedinho","мизинец","小指","الأصبع الصغير","Kleiner Finger","mignolo","새끼 손가락","serçe parmak","小指","कनिष्ठा","jari kelingking","pink"),
("Forefoot","前足","Parte delantera del pie","avant-pied","antepé","передняя нога или лапа","前腳","الأمامية","Vorfuß","zampa anteriore","앞발","önayak","前脚","अगली टांग","kaki depan","voorpoten"),
("Hind_leg","後ろ足","pata posterior","patte arrière","perna Hind","задняя нога","後腿","الساق الخلفية","Hinterbein","zampa posteriore","뒷다리","arka ayak","后腿","हिंद पैर","kaki belakang","achterpoot"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-")),
#---headparts--------
(("HeadParts:","頭部:","Cabeza :","chef :","cabeça :","Руководитель:","頭部：","الرأس:","Kopf:","Sede:","머리 :","Başkanı:","头部：","सिर:","kepala :","hoofd:"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("Eyebrows","眉","ceja","sourcil","sobrancelha","бровь","眉","حاجب العين","Augenbraue","sopracciglio","눈썹","kaş","眉","भौं","alis","wenkbrauw"),
("Eyelash","まつ毛","pestañas","cils","pestanas","ресницы","睫毛","الرموش","Wimpern","ciglio","속눈썹","kirpikler","睫毛","eyelashes","Eyelashes","wimpers"),
("Eyelid","まぶた","párpado","paupière","pálpebra","веко","眼皮","جفن","Augenlid","palpebra","눈꺼풀","gözkapağı","眼皮","पलक","kelopak mata","ooglid"),
("Eye","目","ojo","œil","olho","глаз","眼","عين","Auge","occhio","눈","göz","眼","आंख","mata","oog"),
("Eyeball","眼球","ojo","œil","olho","глаз","眼","عين","Auge","occhio","안구","göz","眼","आंख","mata","oog"),
("Pupil","瞳","alumno","élève","aluno","ученик","瞳孔","تلميذ","Schüler","allievo","학생","öğrenci","瞳孔","शिष्य","murid","leerling"),
("Iris","虹彩","iris","iris","íris","радужная оболочка","鳶尾","قزحية","Iris","iris","홍채","iris","鸢尾","आइरिस","selaput pelangi","iris"),
("Line_of_sight","視線","La línea de visión","ligne de mire","Linha de visão","линия визирования","視線","خط الأفق","Blickrichtung","linea di vista","시선","görüş mesafesi","视线","दृष्टि की लाइन","Line of sight","vizierlijn"),
("Ear","耳","oído","oreille","ouvido","ухо","耳","إذن","Ohr","orecchio","귀","kulak","耳","कान","telinga","oor"),
("Nose","鼻","nariz","nez","nariz","нос","鼻子","أنف","Nase","naso","코","burun","鼻子","नाक","hidung","neus"),
("Cheek","頬","mejilla","joue","bochecha","щека","臉頰","الخد","Wange","guancia","뺨","yanak","脸颊","गाल","pipi","wang"),
("Mouth","口","boca","bouche","boca","рот","口","فم","Mund","bocca","입","ağız","口","मुंह","mulut","mond"),
("Lips","唇","labios","lèvres","lábios","Губы","唇妝","شفاه","Lippen","labbra","입술","dudaklar","唇妆","होंठ","bibir","Lips"),
("Mouth_Corner","口角","Esquina de la boca","coin de la bouche","Canto da boca","Уголок рта","口的角落","زاوية الفم","Mundwinkel","angolo della bocca","구각","ağız köşe","口的角落","मुंह के कोने","sudut mulut","mondhoek"),
("Tooth","歯","diente","dent","dente","зуб","牙齒","سن","Zahn","dente","축소","diş","牙齿","दांत","gigi","tand"),
("Tongue","舌","lengua","langue","língua","язык","舌頭","اللسان","Zunge","lingua","혀","dil","舌头","जीभ","lidah","tong"),
("Jaw","あご","lengüeta","barbillon","farpa","колючка","倒鉤","شوكة","Widerhaken","barbiglio","턱","diken","倒钩","कंटिया","duri","weerhaak"),
("AdamsApple","喉仏","nuez de Adán","la pomme d' Adam","pomo de Adão","кадык","喉結","تفاحة آدم","Adamsapfel","pomo d'Adamo","결후","Adem elması","喉结","टेंटुआ","jakun","adamsappel"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-")),
#---Hair--------
(("Hair:","毛髪:","Cabello :","cheveux :","Cabelo :","Волосы на голове:","頭髮：","الشعر :","hair:","capelli :","모발 :","Saç :","头发：","बाल:","rambut :","haar:"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("Hair","毛","pelo","cheveux","cabelo","волосы","發","شعر","Haar","capelli","머리","saç","发","बाल","rambut","haar"),
("Hair","髪","pelo","cheveux","cabelo","волосы","發","شعر","Haar","capelli","머리","saç","发","बाल","rambut","haar"),
("Tassel","房","borla","gland","borla","кисточка","流蘇","شرابة","Quaste","nappa","방","püskül","流苏","लटकन","rumbai","kwast"),
("Bangs","前髪","flequillos","frange","franja","челка","前劉海","شعر الناصية","Pony","frangia","앞머리","kâkül","前刘海","बैंग्स","poni","pony"),
("Back_hair","後ろ髪","pelo posterior","cheveux en arrière","cabelo Preso","Вернуться волосы","背毛","الشعر مرة أخرى","Zurück Haar","capelli indietro","뒷머리","geri saç","背毛","वापस बाल","rambut kembali","terug haar"),
("Pig_tails","おさげ","cola de cerdo","queues de porc","rabo de porco","Свинья хвосты","豬尾巴","ذيول الخنازير","Pig Tails","code di maiale","땋은","domuz kuyrukları","猪尾巴","सुअर पूंछ","ekor babi","staartjes"),
("Braid","三つ編み","trenza","galon","trança","коса","編織","جديلة","Zopf","treccia","머리띠","örgü","编织","चोटी","kepang","vlecht"),
("Twin_tail","ツインテール","cola doble","Lits queue","cauda gêmeo","Твин хвост","雙尾","ذيل التوأم","Twin Schwanz","Doppia coda","트윈 테일","ikiz kuyruk","双尾","जुड़वां पूंछ","Twin ekor","Twin tail"),
("Ponytai","ポニーテール","Cola de caballo","Queue de cheval","rabo de cavalo","хвост","馬尾巴","ذيل الحصان","Pferdeschwanz","Coda di cavallo","포니 테일","at kuyruğu","马尾巴","चोटी","ekor kuda","paardenstaart"),
("Bobbed","おかっぱ","bobbed","bobbed","balançava","стриженый","剪短","تمايل","wippte","caschetto","단발","kısa kesilmiş","剪短","बाल काटा हुआ","yg dipotong pendek","kortgeknipt"),
("Bun","巻き髪","bollo","chignon","coque","булочка","包子","كعكة","Brötchen","ciambella","곱슬 머리","topuz","包子","बन","sanggul","Bun"),
("Curly_hair","カーリーヘア","El pelo rizado","Les cheveux bouclés","Os cabelos cacheados","вьющиеся волосы","捲髮","الشعر المجعد","lockiges Haar","capelli ricci","곱슬 머리","kıvırcık saç","卷发","घुंघराले बाल","rambut keriting","krulhaar"),
("Kinky_hair","縮れ毛","Kinky pelo","cheveux crépus","Kinky cabelo","Kinky волос","毛淫","شعر غريب","krauses Haar","Kinky capelli","곱슬 머리","Kinky saç","毛淫","किंकी बाल","rambut keriting","kroeshaar"),
("Afro","アフロヘア","Afro","Afro","afro","афро","非洲","الأفرو","Afro","Afro","아후로헤아","afro","非洲","एफ्रो","Afro","Afro"),
("Long_Hair","ロングヘア","Cabello largo","cheveux longs","Cabelo Comprido","Длинные волосы","長毛","الشعر الطويل","Langes Haar","capelli lunghi","긴 머리","uzun Saç","长毛","लंबे बाल","rambut Panjang","lang haar"),
("Short_hair","ショートヘア","El pelo corto","Les cheveux courts","O cabelo curto","Короткие волосы","短發","الشعر القصير","Kurze Haare","capelli corti","쇼트 헤어","kısa saç","短发","छोटे बाल","rambut pendek","kort haar"),
("Toupees","カツラ","peluca","perruque","peruca","парик","假髮","شعر مستعار","Perücke","parrucca","가발","peruk","假发","उपकेश","rambut palsu","pruik"),
("Wig","ウイッグ","peluca","perruque","peruca","парик","假髮","شعر مستعار","Perücke","parrucca","위그","peruk","假发","उपकेश","rambut palsu","pruik"),
("Beard","髭","barba","barbe","barba","борода","鬍鬚","لحية","Bart","barba","수염","sakal","胡须","दाढ़ी","jenggot","baard"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-")),
#---------Muscle------
(("MuscleParts:","筋肉:","músculo:","muscle :","Muscle :","мышцы :","肌肉：","العضلات :","Muskel :","Muscle :","근육 :","kas :","肌肉：","स्नायु :","otot :","spier :"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("Frontalis_muscle","前頭筋","músculo frontal","muscle frontal","músculo Frontal","лобной мышцы","額肌","العضلات الجبهي","frontalis Muskel","frontalis muscolare","이마 근육","frontal kas","额肌","ललाटीय पेशी","otot frontalis","frontalis spier"),
("Orbicularis_oculi","眼輪筋","orbicular de los párpados","orbiculaire","orbicular","Orbicularis глазного","眼輪匝肌","العين الدويرية","orbicularis oculi","orbicularis oculi","眼輪筋","orbikularis","眼轮匝肌","Orbicularis ओकुली","orbicularis oculi","orbicularis oculi"),
("Orbicularis_oris","口輪筋","Orbicular de los labios","Orbiculaire","Orbicular","Orbicularis Oris","口輪匝肌","الفم الدويرية","Orbicularis oris","Orbicularis oris","재갈 관계","Orbicularis oris","口轮匝肌","Orbicularis श्वास","Orbicularis oris","Orbicularis oris"),
("Sternocleidomastoid","胸鎖乳突筋","esternocleidomastoideo","sternocleidomastoid","Sternocleidomastoid","грудинно-ключично-сосцевидный","胸鎖乳突肌","القصية الترقوية الخشائية","Kopfwender","sternocleidomastoideo","흉쇄突筋","sternocleidomastoid","胸锁乳突肌","sternocleidomastoid","sternokleidomastoid","sternocleidomastoid"),
("Deltoid","三角筋","deltoides","deltoïde","deltóide","дельтовидный","三角肌","العضلة الدالية","Deltamuskel","deltoide","삼각근","üç köşeli","三角肌","तिकोना","berbentuk delta","deltoid"),
("Pectoralis_major_muscle","大胸筋","Músculo pectoral mayor","Muscle grand pectoral","Músculo peitoral maior","Большая грудная мышца","胸大肌","العضلة الصدرية الكبرى","Großen Brustmuskel","Muscolo grande pettorale","대흉근","Pektoralis major kas","胸大肌","Pectoralis प्रमुख मांसपेशी","Pectoralis otot besar","Grote borstspier"),
("Rectus","腹直筋","Recto","Rectus","Reto","Прямой мускул","直肌","المستقيمة","Rectus","Retto","배 곧 줄기","Rektus","直肌","Rectus","Rektus","Rectus"),
("External_oblique_muscle","外腹斜筋","Músculo oblicuo externo","Muscle oblique externe","Músculo oblíquo externo","Наружной косой мышцы","腹外斜肌","العضلة المائلة الخارجية","Externe obliquus","Muscolo obliquo esterno","외부 복사근","Dış oblik kas","腹外斜肌","बाहरी तिरछा मांसपेशी","Otot oblik eksternal","Externe schuine spier"),
("Trapezius_muscle","僧帽筋","Músculo trapecio","Muscle trapèze","Músculo trapézio","Трапециевидной мышцы","斜方肌","العضلات شبه المنحرفة","Trapezmuskel","Muscolo trapezio","승모근","Trapez kas","斜方肌","Trapezius मांसपेशी","Otot trapezius","Trapezius"),
("Latissimus_dorsi","広背筋","dorsal ancho","grand dorsal","grande dorsal","широчайшие мышцы спины","背闊肌","الظهرية العريضة","latissimus","gran dorsale","광 등골","latissimus dorsi","背阔肌","latissimus dorsi","latisimus dorsi","latissimusdorsi"),
("Triceps","上腕三頭筋","Tríceps","Triceps","Tricípite","Трицепс","肱三頭肌","ثلاثية الرؤوس","Trizeps","Tricipiti","삼두근","Üç başlı kas","肱三头肌","त्रिशिस्क","Triceps","Triceps"),
("Biceps","上腕二頭筋","Bíceps","Biceps","Bíceps","Бицепс","肱二頭肌","العضلة ذات الرأسين","Bizeps","Bicipite","팔뚝","Biceps","肱二头肌","द्विशिरस्क","Bisep","Biceps"),
("Brachioradialis","腕橈骨筋","Brachioradialis","Supinateur","Braquiorradial","Плечелучевой","肱橈","العضدية","Oberarm","Brachioradialis","팔 요골 근","Brakioradialis","肱桡","Brachioradialis","Brakioradialis","Brachioradialis"),
("Total_extensor_digitorum","総指伸筋","digitorum total extensor","total extenseur des doigts","digitorum total extensor","Всего разгибатель","總伸趾","مجموع أصابع اليد الباسطة","insgesamt extensor digitorum","totale delle dita estensore","총指伸筋","Toplam ekstansör digitorum","总伸趾","कुल extensor digitorum","Jumlah ekstensor digitorum","Totaal extensor digitorum"),
("Extensor_carpi_ulnaris","尺側手根伸筋","Extensor cubital del carpo","Extenseur ulnaire du carpe","Extensor ulnar do carpo","Локтевого разгибателя запястья","尺側腕伸肌","الباسطة الزندية للرسغ","Extensor carpi ulnaris","Estensore ulnare del carpo","긴 쪽 손목 관절 신근","Ekstansör carpi ulnaris","尺侧腕伸肌","Extensor मणिबंध ulnaris","Ekstensor karpi ulnaris","Extensor carpi ulnaris"),
("Flexor_carpi_radialis","橈側手根屈筋","Flexor radial del carpo","Palmaire","Flexor radial do carpo","Flexor Карпи лучевой","橈側腕屈肌","الكعبري الرسغي المثنية","Flexor carpi radialis","Flessore radiale del carpo","橈側손목 뼈 굴근","Fleksör carpi radialis","桡侧腕屈肌","Flexor मणिबंध radialis","Fleksor karpi radialis","Flexor carpi radialis"),
("Extensor_retinaculum","伸筋支帯","retináculo extensor","extenseur ligament","extensor retinaculum","Экстензорных удерживатель","伸肌","الباسطة القيد","Extensor Retinaculum","retinacolo degli estensori","신근支帯","ekstansör retinakulum","伸肌","extensor retinaculum","ekstensor retinaculum","extensor retinaculum"),
("Iliopsoas","腸腰筋","iliopsoas","iliopsoas","Iliopsoas","Iliopsoas","髂腰肌","العضلة القطنية","iliopsoas","ileopsoas","장요근","iliopsoas","髂腰肌","श्रोणिफलक तथा कटिलम्बिका संबंधी","iliopsoas","iliopsoas"),
("Gluteus_maximus","大臀筋","Glúteo mayor","Fessier","Glúteo máximo","Большая ягодичная мышца","臀大肌","الألوية الكبيرة","Gluteus maximus","Grande gluteo","대둔근","Gluteus maximus","臀大肌","बाँधो","Gluteus maximus","Bilspier"),
("Quadriceps","大腿四頭筋","Cuadríceps","Quadriceps","Quadríceps","Четырехглавая мышца","股四頭肌","عضلات الفخذ","Quadrizeps","Quadricipiti","대퇴사 두근","Quadriceps","股四头肌","चतुशिरस्क","Quadriceps","Quadriceps"),
("Biceps_femoris","大腿二頭筋","Bíceps femoral","Biceps crural","Bíceps femoral","Двуглавой мышцы бедра","股二頭肌","الفخذية ذات الرأسين","Bizeps femoris","Bicipite femorale","대퇴 이두근","Biceps femoris","股二头肌","मछलियां ग्रीवा","Bisep femoris","Biceps femoris"),
("Sartorius","縫工筋","sartorio","Sartorius","músculo da coxa","портняжная мышца","賽多利斯","سارتوريوس","Sartorius","Sartorius","縫工筋","Sartorius","赛多利斯","Sartorius","Sartorius","Sartorius"),
("Patellar_ligament","膝蓋靭帯","ligamento patelar","ligament rotulien","O ligamento patelar","связки коленной чашечки","髕韌帶","الرباط الرضفي","Patellarsehne","legamento rotuleo","슬개 인대","patellar ligament","髌韧带","patellar बंधन","ligamen patela","patella ligament"),
("Triceps_surae","下腿三頭筋","Tríceps sural","Triceps sural","Tríceps sural","Трицепс голени","小腿三頭肌","ثلاثية الرؤوس الربلية","Triceps surae","Tricipite surale","하퇴 삼두근","Triceps surae","小腿三头肌","Triceps surae","Trisep surae","Triceps surae"),
("Gastrocnemius","腓腹筋","gastrocnemius","gastrocnemius","gastrocnêmio","икроножная мышца","腓腸肌","الساق","Gastrocnemius","gastrocnemio","비복근","gastrokinemius","腓肠肌","gastrocnemius","gastrocnemius","gastrocnemius"),
("Tibialis_anterior_muscle","前脛骨筋","Músculo tibial anterior","Muscle tibial antérieur","Músculo tibial anterior","Передней большеберцовой мышцы","脛骨前肌","العضلات الظنبوبي الأمامي","Tibialis anterior","Muscolo tibiale anteriore","전 경골근","Tibialis anterior kas","胫骨前肌","Tibialis पूर्वकाल मांसपेशी","Otot tibialis anterior","Tibialis anterior"),
("Extensor_digitorum_longus","長指伸筋","Extensor largo de los dedos","long extenseur des orteils","extensor longo dos dedos","пальцев мышцы","趾長伸肌","الباسطة للأصابع الطويلة","Extensor digitorum longus","estensore lungo delle dita","長指신근","ekstansör digitorum longus","趾长伸肌","extensor digitorum longus","ekstensor digitorum longus","extensor digitorum longus"),
("Soleus_muscle","ヒラメ筋","músculo sóleo","muscle soléaire","músculo sóleo","камбаловидной мышцы","比目魚肌","العضلات النعلية","Soleusmuskel","muscolo soleo","넙치 근육","Soleus kas","比目鱼肌","soleus पेशी","otot soleus","soleusspier"),
("Semitendinosus","半腱様筋","Semitendinosus","Demi-tendineux","Semitendíneo","Полусухожильной","半腱肌","الوترية","Semitendinosus","Semitendinoso","반 힘줄 모양 근","Semitendinosus","半腱肌","Semitendinosus","Semitendinosus","Semitendinosus"),
("Semimembranosus_muscle","半膜様筋","Músculo semimembranoso","Muscle semi-membraneux","Músculo semimembranoso","Полуперепончатой ​​мышцы","半膜肌","العضلات الغشائية النصف","M. semimembranosus","Muscolo semimembranoso","반 막 에 의해서 근육","Semimembranosus kas","半膜肌","Semimembranosus पेशी","Otot semimembranosus","Semimembranosus spier"),
("Achilles_tendon","アキレス腱","tendón de Aquiles","tendon d'Achille","tendão de Aquiles '","Ахиллес сухожилие","跟腱","أخيل وتر","Achillessehne","Achille ' tendine","아킬레스","Aşil tendonu","跟腱","एड़ी की नस","Achilles ' tendon","achillespees"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-")),
#---------Bones------
(("BonesParts:","骨:","hueso:","Bone:","Bone:","Кость :","骨：","العظم :","Bone:","Bone :","뼈 :","kemik :","骨：","हड्डी:","tulang:","Bone :"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("Bone","骨","hueso","os","osso","кость","骨","عظم","Knochen","osso","뼈","kemik","骨","हड्डी","tulang","bot"),
("Spine","背骨","espina","colonne vertébrale","coluna","позвоночник","脊柱","العمود الفقري","Rücken","spina dorsale","척추","omurga","脊柱","रीढ़","tulang belakang","wervelkolom"),
("Rib","肋骨","costilla","nervure","costela","ребро","肋骨","ضلع","Rippe","costola","늑골","kaburga","肋骨","पुसली","tulang rusuk","rib"),
("Nasal_bone","鼻骨","hueso nasal","os nasal","do osso nasal","носовая кость","鼻骨","عظم الأنف","Nasenbein","osso nasale","코뼈","nazal kemik","鼻骨","नाक की हड्डी","tulang hidung","neusbeen"),
("Cheekbones","頬骨","Pómulos","pommettes","Maçãs do rosto","Скулы","顴骨","عظام","Wangenknochen","zigomi","광대뼈","elmacık kemikleri","颧骨","cheekbones","tulang pipi","jukbeenderen"),
("Skull","頭蓋骨","cráneo","crâne","crânio","череп","頭骨","جمجمة","Schädel","cranio","두개골","kafatası","头骨","खोपड़ी","tengkorak","schedel"),
("Cervical","頚椎","cervical","cervical","cervical","шейный","頸椎","عنقي","zervikal","cervicale","경추","boyun","颈椎","सरवाइकल","serviks","hals-"),
("Clavicle","鎖骨","clavícula","clavicule","clavícula","ключица","鎖骨","ترقوة","Schlüsselbein","clavicola","쇄골","klavikula","锁骨","हंसली","tulang selangka","sleutelbeen"),
("Mandible","下顎骨","mandíbula","mandibule","mandíbula","нижняя челюсть","下顎","الفك الأسفل","Unterkiefer","mandibola","하악골","çene kemiği","下颚","जबड़ा","rahang bawah","kaak"),
("Manubrium","胸骨柄","manubrio","manubrium","manúbrio","рукоятка","柄","قبضة","manubrium","manubrio","흉골 무늬","manubrium","柄","Manubrium","manubrium","manubrium"),
("Sternum","胸骨","esternón","sternum","esterno","грудина","胸骨","عبوس","Sternum","sterno","흉골","göğüs kemiği","胸骨","उरोस्थि","tulang dada","borstbeen"),
("Scapula","肩甲骨","escápula","omoplate","omoplata","лопатка","肩胛骨","العظم الكتفي","Schulterblatt","scapola","견갑골","skapula","肩胛骨","कंधे की हड्डी","tulang belikat","schouderblad"),
("Thoracic_vertebra","胸椎","vértebra torácica","vertèbre thoracique","vértebra torácica","грудного позвонка","胸椎","الفقرات الصدرية","Brustwirbel","vertebra toracica","흉추","torasik vertebra","胸椎","छाती रोगों बांस","vertebra Thoracic","borstwervel"),
("Lumbar_spine","腰椎","columna lumbar","rachis lombaire","coluna lombar","Поясничный отдел позвоночника","腰椎","العمود الفقري القطني","Lendenwirbelsäule","lombare della colonna vertebrale","요추","lomber omurga","腰椎","काठ का रीढ़","tulang belakang lumbal","lumbale wervelkolom"),
("Sacrum","仙骨","sacro","sacrum","sacro","крестец","骶骨","العجز","Kreuzbein","sacro","천골","sakrum","骶骨","त्रिकास्थि","tulang kelangkang","heiligbeen"),
("Coccyx","尾てい骨","cóccix","coccyx","cóccix","копчик","尾骨","العصعص","Steißbein","coccige","꼬리뼈","koksiks","尾骨","कोक्सीक्स","tulang sulbi","stuitbeen"),
("Pelvis","骨盤","pelvis","bassin","pélvis","таз","骨盆","حوض","Becken","pelvi","골반","pelvis","骨盆","श्रोणि","panggul","bekken"),
("Humerus","上腕骨","húmero","humérus","úmero","плечевая кость","肱","عظم العضد","Oberarmknochen","omero","상완골","kol kemiği","肱","प्रगंडिका","humerus","opperarmbeen"),
("Radius","橈骨","radio","rayon","raio","радиус","半徑","نصف القطر","Radius","raggio","요골","yarıçap","半径","त्रिज्या","radius","radius"),
("Ulna","尺骨","cubito","cubitus","cúbito","локтевая кость","尺骨","عظم الزند","Elle","ulna","척골","dirsek kemiği","尺骨","कुहनी की हड्डी","tulang hasta","ellepijp"),
("Carpal","手根骨","carpiano","carpien","carpiano","кистевой","腕","الرسغي","Handwurzel-","carpale","手根骨","karpal","腕","कलाई का","yg berhubung dgn tangan","carpaal"),
("Metacarpal_bone","中手骨","hueso metacarpiano","métacarpien","metacarpo","пястной кости","掌骨","عظم المشط","Mittelhandknochen","osso metacarpale","손바닥 뼈","metakarpus","掌骨","करभिकास्थिक हड्डी","tulang metakarpal","middenhandsbeentje"),
("Phalange","指骨","falange","phalange","falange","фаланстер","指骨","الكتائب","Phalange","falange","손가락 뼈","parmak kemiği","指骨","अँगुली का पोर","ruas","vingerkootje"),
("Femur","大腿骨","fémur","fémur","fêmur","бедренная кость","股骨","عظم الفخذ","Femur","femore","대퇴골","uyluk","股骨","जांध की हड्डी","tulang paha","dijbeen"),
("Patella","膝蓋骨","rótula","rotule","patela","надколенник","髕骨","العظم المتحرك في رأس الركبة","Patella","patella","슬개골","dizkapağı","髌骨","वुटने की चक्की","tempurung lutut","knieschijf"),
("Tibia","脛骨","tibia","tibia","tíbia","берцовая кость","脛骨","التيبية مزمار قديم","Tibia","tibia","경골","kaval kemiği","胫骨","टिबिअ","tulang kering","scheenbeen"),
("Fibula","腓骨","peroné","fibule","fíbula","фибула","腓骨","مشبك","Fibula","perone","비골","fibula","腓骨","बहिर्जंघिका","tulang betis","fibula"),
("Tarsal","足根骨","tarsal","tarsien","tarsal","предплюсневой","跗","عظم الكعب","tarsal","tarsale","足根骨","ayak bileği ile ilgili","跗","टखने की हड्डियों का","tarsal","tarsale"),
("Metatarsal","中足骨","Metatarsiano","Métatarsien","Metatarso","Плюсневой","蹠骨","مشط القدم","Mittelfuß-","Metatarso","중족골","Metatarsal","跖骨","प्रपदिकीय","Metatarsal","Middenvoetsbeentje"),
("Honemoto_bushi","骨基節","Honemoto -bushi","Honemoto -bushi","Honemoto - bushi","Honemoto -буси","Honemoto -武士","Honemoto - البوشي","Honemoto - bushi","Honemoto - bushi","骨基節","Honemoto - bushi","Honemoto -武士","Honemoto - Bushi","Honemoto - Bushi","Honemoto - Bushi"),
("RootBone","ルートボーン","hueso Root","racine os","óssea Root","Корневая кость","根骨","العظام الجذر","Wurzelknochen","Root osso","루트 번","kök kemik","根骨","जड़ हड्डी","tulang akar","Root bot"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-")),
#---------Mechanic1------
(("Mechanic:","メカニック1:","Mecánico 1 :","Mécanique 1 :","Mecânico 1:","Механика 1 :","機修工1 ：","ميكانيكي 1 :","Mechanic 1:","Meccanico 1 :","메카닉 1 :","Mekanik 1 :","机修工1 ：","मैकेनिक 1:","Mechanic 1 :","Mechanic 1 :"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("Airplane","飛行機","avión","avion","avião","самолет","飛機","طائرة","Flugzeug","aereo","비행기","uçak","飞机","हवाई जहाज","pesawat terbang","vliegtuig"),
("Propeller","プロペラ","hélice","hélice","hélice","пропеллер","螺旋槳","المروحة","Propeller","elica","프로펠러","pervane","螺旋桨","प्रोपेलर","baling-baling","propeller"),
("Propeller_shaft","プロペラシャフト","árbol de transmisión","arbre d'hélice","eixo de hélice","вал карданный","螺旋槳軸","ذراع التوصيل","Kardanwelle","albero dell'elica","프로펠러 샤프트","pervane şaftı","螺旋桨轴","प्रोपेलर शाफ्ट","poros baling-baling","schroefas"),
("Noze_Gear","ノーズギア","Nozugia","Nozugia","Nozugia","Nozugia","Nozugia","Nozugia","Nozugia","Nozugia","노즈기아","Nozugia","Nozugia","Nozugia","Nozugia","Nozugia"),
("Landing_Gear","ランディングギア","Tren de aterrizaje","Train d'atterrissage","Trem de Pouso","шасси","起落架","الهبوط","Fahrwerk","Landing Gear","랜딩 기어","iniş takımı","起落架","रक्षात्मक कपड़ा","Landing Gear","landingsgestel"),
("Gear_door","ギア扉","de puertas de tren","porte engins","porta engrenagem","Шестерня двери","起落架艙門","الباب والعتاد","Fahrwerksklappen","porta Gear","기어 문","dişli kapı","起落架舱门","गियर दरवाजा","pintu gigi","Gear deur"),
("Flap","フラップ","solapa","rabat","aba","заслонка","拍打","رفرف","Klappe","patta","플랩","kapak","拍打","फ्लैप","tutup","klep"),
("Aileron","エルロン","alerón","aileron","ailerom","элерон","副翼","موازنة الطائرة","Querruder","alettone","에일러론","kanatçık","副翼","हवाई जहाज़ के पीछे की ओर की पतवार","kemudi guling","aileron"),
("Ladder","ラダー","escalera","échelle","escada","лестница","階梯","سلم","Leiter","scala","래더","merdiven","阶梯","सीढ़ी","tangga","ladder"),
("Trim_tab","トリムタブ","aleta de compensación","Coupez onglet","compensador","Триммер","修剪標籤","التبويب تقليم","Registerkarte Trim","scheda Trim","손질 탭","sekmesini Trim","修剪标签","टैब छाँटो","Potong tab","Trim tab"),
("Elevator","エレベータ","elevador","ascenseur","Elevador","Лифт","電梯","مصعد","Fahrstuhl","Ascensore","엘리베이터","Asansör","电梯","लिफ़्ट","lift","lift"),
("Trim_tab","トリムタブ","aleta de compensación","Coupez onglet","compensador","Триммер","修剪標籤","التبويب تقليم","Registerkarte Trim","scheda Trim","손질 탭","sekmesini Trim","修剪标签","टैब छाँटो","Potong tab","Trim tab"),
("Canard","カナード","bulo","canard","mentira","утка","卡納德","إشاعة كاذبة","Ente","canard","카나드","asılsız haber","卡纳德","बेबुनियाद ख़बर","desas-desus","Canard"),
("Alignment","照準","alineación","alignement","alinhamento","выравнивание","校準","المحاذاة","Ausrichtung","allineamento","조준","hiza","校准","संरेखण","penjajaran","opstelling"),
("Vernier","バーニア","vernier","vernier","vernônio","нониус","游標","الورنية مقياس الكسور","Vernier","verniero","버니어","verniyer","游标","वर्नियर","Vernier","nonius"),
("Rotor","ローター","rotor","rotor","rotor","ротор","轉子","دوار","Rotor","rotore","로터","rotor","转子","रोटर","rotor","rotor"),
("Main_Rotor","メインローター","rotor principal","rotor principal","rotor principal","несущий винт","主旋翼","الدوار الرئيسي","Hauptrotor","main Rotor","메인 로터","ana Rotor","主旋翼","मुख्य रोटर","Main Rotor","Main Rotor"),
("Tail_Rotor","テールローター","rotor de cola","rotor de queue","rotor de cauda","хвостового ротора","尾旋翼","الذيل الدوار","Heckrotor","rotore di coda","테일 로터","kuyruk Rotor","尾旋翼","पूंछ रोटर","Tail Rotor","Tail Rotor"),
("Chain_gun","チェーンガン","pistola de cadena","pistolet de la chaîne","arma cadeia","Сеть пистолет","鏈炮","سلسلة بندقية","Kettenkanone","gun catena","기관총","zincir gun","链炮","श्रृंखला बंदूक","gun rantai","chain gun"),
("Hinge","ヒンジ","bisagra","charnière","dobradiça","петля","合頁","مفصل","Scharnier","cerniera","경첩","menteşe","合页","काज","engsel","scharnier"),
("Shaft","シャフト","eje","arbre","Shaft","вал","軸","رمح","Welle","albero","샤프트","şaft","轴","शाफ़्ट","batang","schacht"),
("Rocket","ロケット","cohete","fusée","foguete","ракета","火箭","صاروخ","Rakete","razzo","로켓","roket","火箭","राकेट","roket","raket"),
("Rocket","ロケット弾","cohete","fusée","foguete","ракета","火箭","صاروخ","Rakete","razzo","로켓탄","roket","火箭","राकेट","roket","raket"),
("Missile","ミサイル","misil","missile","míssil","ракета","導彈","صاروخ","Rakete","missile","미사일","füze","导弹","मिसाइल","misil","raket"),
("Chaff","チャフ","paja","balle","palha","мякина","糠","قش","Spreu","pula","채프","saman","糠","फूस","sekam","kaf"),
("Car","自動車","coche","voiture","carro","автомобиль","汽車","سيارة","Auto","auto","자동차","araba","汽车","कार","mobil","auto"),
("Front_wheel","前輪","rueda delantera","roue avant","roda dianteira","Переднее колесо","前輪","العجلة الأمامية","Vorderrad","ruota anteriore","전륜","ön tekerlek","前轮","सामने पहिया","roda depan","voorwiel"),
("Rear_wheel","後輪","rueda trasera","roue arrière","roda traseira","Заднее колесо","後輪","العجلات الخلفية","Hinterrad","ruota posteriore","후륜","arka tekerlek","后轮","रियर पहिया","roda belakang","achterwiel"),
("Handle","ハンドル","manejar","traiter","manusear","обрабатывать","處理","مقبض","Griff","ansa","핸들","işlemek","处理","संभालना","menangani","handvat"),
("Steering","ステアリング","gobierno","pilotage","Direcção","рулевое управление","操舵","توجيه","Lenkung","sterzo","스티어링","yönetim","操舵","स्टीयरिंग","pengemudian","stuurinrichting"),
("Wiper","ワイパー","limpiaparabrisas","essuie-glace","limpador","стеклоочиститель","雨刮器","ممسحة","Wischer","Wiper","와이퍼","silecek","雨刮器","वाइपर","penghapus","ruitewisser"),
("Crank","クランク","manivela","manivelle","manivela","рукоятка","曲柄","كرنك","Crank","Crank","크랭크","krank","曲柄","क्रैंक","engkol","zwengel"),
("Valve","バルブ","válvula","vanne","válvula","клапан","閥","صمام","Ventil","valvola","밸브","valf","阀","वाल्व","katup","ventiel"),
("Key","キー","clave","clé","chave","ключ","關鍵","مفتاح","Schlüssel","chiave","키","anahtar","关键","कुंजी","kunci","sleutel"),
("Brake","ブレーキ","freno","frein","freio","тормоз","制動","فرامل","Bremse","freno","브레이크","fren","制动","ब्रेक","rem","rem"),
("Emergency_brake","サイドブレーキ","freno de emergencia","freinage d'urgence","freio de emergência","Стоп-кран","應急剎車","فرملة الطوارئ","Notbremse","freno di emergenza","사이드 브레이크","acil freni","应急刹车","आपातकालीन ब्रेक","rem darurat","Noodrem"),
("Accelerator","アクセル","acelerador","accélérateur","acelerador","ускоритель","加速器","مسرع","Beschleuniger","acceleratore","액셀","hızlandırıcı","加速器","त्वरक","akselerator","versneller"),
("Turn_signal","ウインカー","señal de vuelta","clignotant","sinal de volta","поворотник","拐彎信號","إشارة الدوران","Blinklicht","Girare segnale","윙커","dönüş sinyali","拐弯信号","मुड़ने का सिगनल","lampu sen","knipperlicht"),
("Shift_knob","シフトノブ","pomo de cambio","bouton Shift","alavanca de câmbio","рукоятка рычага переключения передач","排檔頭","تحول مقبض الباب","Schaltknauf","pomello del cambio","시프트 노브","vites topuzu","排档头","शिफ्ट घुंडी","shift knob","pookknop"),
("Selector","セレクター","selector","sélecteur","seletor","селектор","選擇","منتقى","Wähler","selettore","선택기","seçici","选择","चयनकर्ता","Selector","keuzeschakelaar"),
("Trunk","トランク","tronco","tronc","tronco","ствол","樹幹","جذع","Stamm","tronco","트렁크","gövde","树干","ट्रंक","batang","romp"),
("Door","ドア","puerta","porte","porta","дверь","門","باب","Tür","porta","문","kapı","门","दरवाजा","pintu","deur"),
("Mirror","ミラー","espejo","miroir","espelho","зеркало","鏡子","مرآة","Spiegel","specchio","거울","ayna","镜子","दर्पण","cermin","spiegel"),
("Rearview_mirror","バックミラー","espejo retrovisor","rétroviseur","espelho retrovisor","зеркало заднего вида","後視鏡","مرآة الرؤية الخلفية","Rückspiegel","specchietto retrovisore","백미러","dikiz aynası","后视镜","रियरव्यू मिरर","kaca spion","achteruitkijkspiegel"),
("Muffler","マフラー","silenciador","silencieux","silencioso","глушитель","消聲器","كاتم الصوت","Schalldämpfer","silenziatore","머플러","susturucu","消声器","मफलर","knalpot","geluiddemper"),
("Wheel","ホイール","rueda","roue","roda","колесо","輪","عجلة","Rad","ruota","휠","tekerlek","轮","पहिया","roda","wiel"),
("Tire","タイヤ","neumático","pneu","pneu","шина","胎","إطار العجلة","Reifen","pneumatico","타이어","lastik","胎","टायर","ban","band"),
("Light","ライト","luz","lumière","luz","свет","光","ضوء","Licht","luce","라이트","ışık","光","प्रकाश","cahaya","licht"),
("Suspension","サスペンション","suspensión","suspension","suspensão","подвеска","懸掛","تعليق","Suspension","sospensione","서스펜션","süspansiyon","悬挂","निलंबन","penangguhan","schorsing"),
("Antenna","アンテナ","antena","antenne","antena","антенна","天線","هوائي","Antenne","antenna","안테나","anten","天线","ऐन्टेना","antena","antenne"),
("Engine","エンジン","motor","moteur","motor","двигатель","發動機","محرك","Motor","motore","엔진","motor","发动机","इंजन","mesin","motor"),
("Crankshaft","クランクシャフト","cigüeñal","vilebrequin","virabrequim","коленчатый вал","曲軸","العمود المرفقي","Kurbelwelle","albero a gomiti","크랭크 샤프트","krank Mili","曲轴","क्रैंकशाफ्ट","poros engkol","krukas"),
("Piston","ピストン","pistón","piston","pistão","поршень","活塞","مكبس","Kolben","pistone","피스톤","piston","活塞","पिस्टन","seher","zuiger"),
("Valve","バルブ","válvula","vanne","válvula","клапан","閥","صمام","Ventil","valvola","밸브","valf","阀","वाल्व","katup","ventiel"),
("Camshaft","カムシャフト","árbol de levas","arbre à cames","Camshaft","распределительный вал","凸輪軸","عمود الحدبات","Nockenwelle","albero a camme","캠 샤프트","Eksantrik Mili","凸轮轴","कैंषफ़्ट","camshaft","nokkenas"),
("Rocker_arm_shaft","ロッカーアームシャフト","Eje de balancín","Arbre de culbuteurs","Eixo Rocker braço","Ось коромысла","搖臂軸","ذراع الكرسي الهزاز رمح","Kipphebelwelle","Albero del bilanciere","로커 암 샤프트","Külbütör mili","摇臂轴","घुमाव हाथ शाफ्ट","Poros rocker arm","Tuimelaaras"),
("Flywheel","フライホイール","volante","volant","pêndulo","маховик","飛輪","دولاب الموازنة","Schwungrad","volano","플라이휠","volan","飞轮","चक्का","roda gila","vliegwiel"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-")),
#---------Mechanic2------
(("Mechanic2:","メカニック2:","Mecánico 2 :","Mécanique 2 :","Mecânico 2:","Механика 2 :","機械師2 ：","ميكانيكي 2 :","Mechanic 2:","Mechanic 2 :","메카닉 2 :","Mekanik 2 :","机械师2 ：","मैकेनिक 2:","Mechanic 2 :","Mechanic 2 :"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("Tank","戦車","tanque","réservoir","tanque","бак","坦克","خزان","Tank","serbatoio","전차","tank","坦克","टैंक","tangki","tank"),
("Searchlight","サーチライト","reflector","projecteur","holofote","прожектор","探照燈","كشاف","Suchscheinwerfer","Searchlight","탐조등","ışıldak","探照灯","खोज - दीप","lampu sorot","zoeklicht"),
("Drive_wheel","駆動輪","wheel Drive","la roue d'entraînement","roda da movimentação","Ведущее колесо","驅動輪","الدفع الرباعي","Antriebsrad","ruote motrici","구동륜","tahrik tekerleği","驱动轮","ड्राइव पहिया","roda penggerak","aandrijfwiel"),
("Drive_sprocket","起動輪","piñón","pignon d'entraînement","Dirija pinhão","Ведущая звездочка","驅動鏈輪","محرك ضرس","Fahren Kettenrad","pignone","기동 고리","dişlisini sürücü","驱动链轮","sprocket ड्राइव","mendorong sproket","aandrijfkettingwiel"),
("Track_roller","転輪","rodamiento de oruga","galet","rolo da trilha","трек ролик","履帶支重輪","الأسطوانة المسار","Laufrollen","rotella","전륜","Makaralı","履带支重轮","ट्रैक रोलर","track roller","Rupsbandbescherming"),
("Turret","砲塔","torreta","tourelle","torre","турель","砲塔","برج","Türmchen","torretta","포탑","taret","炮塔","बुर्ज","kubah","torentje"),
("Cupola","キューポラ","cúpula","coupole","cúpula","купол","沖天爐","قبة","Kuppel","cupola","큐폴라","kubbe","冲天炉","गुंबज","kubah","koepel"),
("Hatch","ハッチ","escotilla","trappe","escotilha","люк","孵化","فقس","Luke","boccaporto","해치","kapak","孵化","पक्षियों के बच्चे","menetas","luik"),
("Periscope","ペリスコープ","periscopio","périscope","periscópio","перископ","潛望鏡","بيريسكوب","Periskop","periscopio","잠망경","periskop","潜望镜","पेरिस्कोप","periskop","periscoop"),
("Visor","バイザー","visera","visière","viseira","козырек","帽舌","قناع","Visier","visiera","관리자","güneşlik","帽舌","टोपी का छज्जा","kedok","vizier"),
("Gun_barrel","砲身","barril de arma","canon","cano da arma","ствол пушки","輪管","بندقية برميل","Gun Barrel","gun barrel","포신","namlu","轮管","नाल","laras senapan","geweerloop"),
("Machine_gun","機関銃","ametralladora","Machine gun","Metralhadora","пулемет","機槍","مدفع رشاش","Maschinengewehr","machine gun","기관총","makineli tüfek","机枪","मशीनगन","senapan mesin","machinegeweer"),
("Caterpillar","キャタピラ","oruga","chenille","lagarta","гусеница","毛蟲","تراكتور","Raupe","bruco","캐터필러","tırtıl","毛虫","कमला","ulat","rups"),
("Crawler_track","履帯","oruga","Chenille","rasto","Гусеничная","履帶","المسار الزاحف","Raupenfahrwerk","cingolo","리","Paletli parça","履带","ट्रेक ट्रैक","crawler track","rupswielstel"),
("Smoke_disk_char_Dja","スモークディスチャーヂャー","Char disco Smoke Dja","Fumée disque omble Dja","Disco de fumaça de char Dja","Дым диск символ Джа","煙炭盤Dja保護","شار القرص الدخان دجا","Smoke Platte char Dja","Disco Smoke char Dja","스모크 디스 시 지ャ","Duman Disk karakter Dja","烟炭盘Dja保护","धुआँ डिस्क चार Dja","Asap disk yang arang Dja","Rook schijf char Dja"),
("Smoke_grenade_launchers","発煙弾発射機","Lanzagranadas de humo","Lance-grenades fumigènes","Lançadores de granadas de fumaça","Дым гранатометы","煙榴彈發射器","قاذفات قنابل الدخان","Rauchgranatwerfer","Fumogeni granata","연막탄 발사기","Duman bombaatar","烟榴弹发射器","स्मोक ग्रेनेड लांचर","Peluncur granat asap","Rook granaatwerpers"),
("Bicycle","自転車","bicicleta","vélo","bicicleta","велосипед","自行車","دراجة","Fahrrad","bicicletta","자전거","bisiklet","自行车","साइकिल","sepeda","fiets"),
("Saddle","サドル","silla de montar","selle","sela","седло","鞍","سرج","Sattel","sella","안장","eyer","鞍","काठी","sadel","zadel"),
("Chain","チェーン","cadena","chaîne","cadeia","цепь","鏈","سلسلة","Kette","catena","체인","zincir","链","श्रृंखला","rantai","keten"),
("Rear_brake","リアブレーキ","freno trasero","frein arrière","travão traseiro","задний тормоз","後制動","الفرامل الخلفية","Bremse hinten","freno posteriore","리어 브레이크","arka fren","后制动","रियर ब्रेक","rem belakang","achterrem"),
("Front_brake","フロントブレーキ","freno delantero","frein avant","travão dianteiro","Передние тормоза","前制動","الفرامل الأمامية","Vorderradbremse","freno anteriore","프론트 브레이크","ön fren","前制动","सामने ब्रेक","rem depan","voorrem"),
("Rear_derailleur","リアディレイラー","Cambio trasero","dérailleur arrière","desviador traseiro","задний переключатель","後撥鏈器","derailleur الخلفية","Schaltwerk","deragliatore posteriore","뒷 변속기","arka değiştirici","后拨链器","पीछे derailleur","derailleur belakang","achterderailleur"),
("Transmission","変速機","transmisión","transmission","transmissão","передача","傳輸","انتقال","Übertragung","trasmissione","변속기","transmisyon","传输","पारेषण","transmisi","transmissie"),
("Ship","船","barco","Ship","navio","корабль","船","سفينة","Schiffs","nave","배","gemi","船","जहाज","kapal","schip"),
("Rudder","舵","timón","gouvernail","leme","руль","舵","الموجه","Ruder","timone","방향타","dümen","舵","पतवार","kemudi","roer"),
("Ikari","碇","Ikari","Ikari","Ikari","Икари","碇","إيكاري","Ikari","Ikari","이카리","ikari","碇","Ikari","Ikari","Ikari"),
("Sail","帆","vela","voile","vela","парус","帆","الشراع","Sail","Vela","항해","yelken","帆","पाल","berlayar","zeil"),
("Mast","マスト","mástil","mât","mastro","мачта","桅","سارية","Mast","albero","마스트","direk","桅","मस्तूल","tiang kapal","mast"),
("Radar","レーダー","radar","radar","radar","радар","雷達","رادار","Radar","radar","레이더","radar","雷达","राडार","radar","radar"),
("Turret","砲塔","torreta","tourelle","torre","турель","砲塔","برج","Türmchen","torretta","포탑","taret","炮塔","बुर्ज","kubah","torentje"),
("Rotating_turret","回転砲塔","torreta giratoria","tourelle rotative","Girando turret","вращающейся башне","旋轉砲塔","برج الدورية","Drehturm","torretta girevole","회전 포탑","döner taret","旋转炮塔","घूर्णन बुर्ज","rotating turret","roterende torentje"),
("Main_gun","主砲","arma principal","arme principale","principal arma","Главная пистолет","主砲","السلاح الرئيسي","Hauptkanone","cannone principale","주포","ana silah","主炮","मुख्य बंदूक","meriam utama","belangrijkste wapen"),
("Vice_gun","副砲","Vice arma","vice pistolet","vice- gun","вице пистолет","副槍","نائب بندقية","Vize Pistole","Vice gun","부포","Başkan gun","副枪","वाइस बंदूक","Wakil gun","vice pistool"),
("High-angle_gun","高角砲","arma de alto ángulo","Haute - angle canon","arma de alta ângulo","Высокий угол пушки","高角炮","بندقية عالية زاوية","High-Angle- Pistole","high-angolo gun","고각 포","Yüksek açılı gun","高角炮","उच्च कोण बंदूक","gun tinggi angle","high -angle gun"),
("Anti-aircraft_gun","高射砲","arma antiaéreo","canon anti-aérien","arma anti-aérea","Зенитная пушка","高射砲","مدفع مضاد للطائرات","Flugabwehrkanone","cannone antiaereo","고사포","uçaksavar silahı","高射炮","विमान - वेधी तोप","gun anti-pesawat","luchtafweergeschut"),
("Propeller_shaft","推進軸","árbol de transmisión","arbre d'hélice","eixo de hélice","вал карданный","螺旋槳軸","ذراع التوصيل","Kardanwelle","albero dell'elica","추진축","pervane şaftı","螺旋桨轴","प्रोपेलर शाफ्ट","poros baling-baling","schroefas"),
("Waterproof_door","防水扉","puerta estanca","porte étanche","porta à prova d'água","Водонепроницаемый двери","防水門","باب للماء","Wasserdichte Tür","sportello impermeabile","방수 문","Su geçirmez kapı","防水门","निविड़ अंधकार दरवाजा","Waterproof pintu","waterdichte deur"),
("Weathervane","風見","Veleta","girouette","Cata","Флюгер","風向標","دوارة","Wetterfahne","banderuola","풍향계","rüzgargülü","风向标","Weathervane","Weathervane","windwijzer"),
("Elevator","エレベーター","elevador","ascenseur","Elevador","Лифт","電梯","مصعد","Fahrstuhl","Ascensore","엘리베이터","Asansör","电梯","लिफ़्ट","lift","lift"),
("Lift","リフト","ascensor","soulever","elevador","лифт","電梯","رفع","Aufzug","sollevamento","리프트","asansör","电梯","लिफ्ट","angkat","lift"),
("Electric_train","電車","tren eléctrico","train électrique","trem elétrico","электропоезд","電動火車","قطار كهربائي","Elektrische Eisenbahn","Trenino elettrico","기차","elektrikli tren","电动火车","इलेक्ट्रिक ट्रेन","kereta listrik","elektrische trein"),
("Strap","つり革","correa","sangle","cinta","ремень","背帶","حزام","Gurt","cinghia","손잡이","kayış","背带","पट्टा","tali pengikat","riem"),
("Pantograph","パンタグラフ","pantógrafo","pantographe","pantógrafo","пантограф","受電弓","المنساخ أداة للنسخ","Pantograph","pantografo","팬터그래프","pantograf","受电弓","किसी भी नाप का नक्शा इत्यादि खींचने का यंत्र","pantograph","pantograaf"),
("Entrance_door","入口扉","puerta de entrada","porte d'entrée","porta de entrada","Входная дверь","大門","باب المدخل","Eingangstür","porta d'ingresso","입구 문","giriş kapısı","大门","प्रवेश द्वार","pintu masuk","ingangsdeur"),
("Exit_door","出口扉","puerta de salida","porte de sortie","porta de saída","Выход дверь","出口門","باب الخروج","Ausgangstür","uscita","출구 문","çıkış kapısı","出口门","निकास द्वार","keluar pintu","uitgangsdeur"),
("Truck","台車","camión","camion","caminhão","грузовик","卡車","شاحنة","LKW","camion","카트","kamyon","卡车","ट्रक","truk","vrachtwagen"),
("Bogie_frame","台車枠","bastidor del bogie","châssis de bogie","bogie quadro","рама тележки","轉向架構架","التصويب الإطار","Drehgestellrahmen","Bogie cornice","대차 프레임","boji çerçeve","转向架构架","बोगी फ्रेम","bingkai bogie","draaistel"),
("Master_controller","マスターコントローラー","El controlador maestro","Le contrôleur maître","O controlador Master","главный контроллер","主控制器","وحدة تحكم رئيسية","Master-Steuerung","controllo Master","마스터 컨트롤러","master kontrolör","主控制器","मास्टर नियंत्रक","Guru kontroler","master controller"),
("Mascon","マスコン","mascon","mascon","mascon","Mascon","質量瘤","Mascon","Mascon","mascon","매스 콘","Mascon","质量瘤","मैस्कॉन","Mascon","mascon"),
("Direct_controller","ダイレクトコントローラー","controlador directo","contrôleur direct","controlador direto","Прямая контроллер","直接控制器","تحكم مباشر","Direkte Steuerung","controllo diretto","직접 컨트롤러","doğrudan denetleyici","直接控制器","सीधी नियंत्रक","kontroler Direct","direct controller"),
("Brake_cylinder","ブレーキシリンダー","cilindro de freno","cylindre de frein","cilindro de freio","тормозной цилиндр","制動缸","اسطوانة الفرامل","Bremszylinder","cilindro del freno","브레이크 실린더","fren silindiri","制动缸","ब्रेक सिलेंडर","rem silinder","remcilinder"),
("Return_spring","戻しバネ","Muelle de retorno","Retour printemps","mola de retorno","Вернуться пружину","回位彈簧","عودة الربيع","Die Rückstellfeder","molla di ritorno","리턴 스프링","Dönüş bahar","回位弹簧","वसंत लौटें","kembali musim semi","terug voorjaar"),
("Pillow_spring","枕バネ","primavera Pillow","Oreiller printemps","primavera Pillow","Подушка весной","枕彈簧","الربيع سادة","Kissen Feder","primavera Pillow","베개 용수철","yastık bahar","枕弹簧","तकिया वसंत","bantal musim semi","kussen voorjaar"),
("Axle_spring","軸バネ","primavera Eje","essieu printemps","mola Eixo","мост весной","車軸彈簧","المحور الربيع","Achsfeder","primavera Axle","축 스프링","aks bahar","车轴弹簧","एक्सल वसंत","Axle semi","as voorjaar"),
("Driving_wheel","動輪","rueda motriz","roue motrice","roda motriz","Ведущее колесо","驅動輪","عجلة القيادة","Antriebsrad","ruota motrice","동륜","işletme tekeri","驱动轮","प्रधान पहिया","mengemudi roda","aandrijfwiel"),
("Coupler","連結器","acoplador","coupleur","acoplador","сцепка","耦合器","مقرنة","Koppel","accoppiatore","까탈","çoğaltıcı","耦合器","युग्मक","alat prerangkai","koppeling"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-")),
#---------Mechanic3------
(("Mechanic3:","メカニック3:","Mechanic 3 :","Mécanicien 3 :","Mecânico 3:","Механика 3 :","機械師3 ：","ميكانيكي 3 :","Mechanic 3:","Mechanic 3 :","메카닉 3 :","Mekanik 3 :","机械师3 ：","मैकेनिक 3:","Mechanic 3 :","Mechanic 3 :"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("Gun","銃","pistola","pistolet","pistola","пистолет","槍","بندقية","Pistole","pistola","총","tabanca","枪","बंदूक","pistol","geweer"),
("Handgun","拳銃","pistola","pistolet","arma curta","пистолет","手槍","مسدس","Handwaffe","pistola","권총","tabanca","手枪","handgun","pistol","pistool"),
("Rifle","ライフル銃","rifle","fusil","rifle","винтовка","步槍","بندقية","Gewehr","fucile","소총","tüfek","步枪","राइफल","senapan","geweer"),
("Slide","スライド","diapositiva","Glisser","slide","слайд","滑","انخفاض","Slide","Presentazione","슬라이드","slayt","滑","स्लाइड","meluncur","glijbaan"),
("Slide_stop","スライドストップ","Deslice parada","Faites glisser arrêt","Deslize parada","Слайд -стоп","滑動停止","الشريحة توقف","Schieben Anschlag","Far scorrere arresto","슬라이드 스톱","dur kaydırın","滑动停止","स्टॉप स्लाइड","Slide berhenti","Schuif stop"),
("Barrel","銃身","barril","baril","barril","баррель","桶","برميل","Fass","barile","총신","varil","桶","बैरल","barel","vat"),
("Barrel","バレル","barril","baril","barril","баррель","桶","برميل","Fass","barile","배럴","varil","桶","बैरल","barel","vat"),
("Firing_pin","撃針","El percutor","percuteur","percutor","боек","撞針","القادح","Schlagbolzen","percussore","격침","pin Atış","撞针","पिन फायरिंग","Memecat pin","vuurpen"),
("Magazine_release_button","マガジンリリースボタン","Botón de liberación de la revista","Bouton de dégagement","Botão de liberação da Revista","Защелка магазина","雜誌釋放按鈕","زر تحرير مجلة","Magazin Auslöseknopf","Pulsante di rilascio Magazine","잡지 릴리스 버튼","Dergi açma düğmesi","杂志释放按钮","पत्रिका रिलीज बटन","Tombol pelepas Magazine","Magazine ontgrendelingsknop"),
("Magazine","マガジン","revista","magazine","revista","журнал","雜誌","مجلة","Magazin","rivista","매거진","dergi","杂志","पत्रिका","majalah","tijdschrift"),
("Magazine","弾倉","revista","magazine","revista","журнал","雜誌","مجلة","Magazin","rivista","탄창","dergi","杂志","पत्रिका","majalah","tijdschrift"),
("Trigger","トリガー","gatillo","trigger","gatilho","триггер","觸發","الزناد","Trigger-","trigger","트리거","tetik","触发","ट्रिगर","pelatuk","trekker"),
("Hammer","撃鉄","martillo","marteau","martelo","молоток","錘","مطرقة","Hammer","martello","격철","çekiç","锤","हथौड़ा","palu","hamer"),
("Hammer","ハンマー","martillo","marteau","martelo","молоток","錘","مطرقة","Hammer","martello","망치","çekiç","锤","हथौड़ा","palu","hamer"),
("Spring_plug","スプリングプラグ","enchufe de Primavera","fiche de printemps","plugue da Primavera","Весна плагин","Spring插件","المكونات الربيع","Federstecker","spina Primavera","스프링 플러그","bahar fiş","Spring插件","स्प्रिंग प्लग","musim semi steker","veerplug"),
("Recoil_spring","リコイルスプリング","Muelle recuperador","Un ressort de rappel","primavera Recoil","Возвратная пружина","复進簧","نكص الربيع","Recoil Feder","molla di recupero","리코일 스프링","geri tepme bahar","复进簧","हटना वसंत","Recoil musim semi","terugstootveer"),
("Spring_guide","スプリングガイド","guía del muelle","guide de printemps","guia de Primavera","Направляющая пружины","彈簧導","دليل الربيع","Die Federführung","guida Primavera","스프링 가이드","Spring kılavuzu","弹簧导","स्प्रिंग गाइड","panduan musim semi","veergeleider"),
("Safety_lever","セーフティーレバー","palanca de seguridad","levier de sécurité","alavanca de segurança","рычаг безопасности","保險桿","رافعة السلامة","Sicherheitshebel","leva di sicurezza","안전 레버","emniyet kolu","保险杆","सुरक्षा लीवर","tuas Keselamatan","veiligheidshendeltje"),
("Ejector_rod","エジェクターロッド","la varilla de expulsión","tige d'éjection","haste ejetor","Эжектор стержень","頂桿","القاذف قضيب","Auswurfstange","asta di espulsione","이젝터 로드","İtici çubuk","顶杆","बेदखलदार रॉड","rod ejector","uitwerpstaaf"),
("Thumb-piece","サムピース","Pulgar pieza","poucier","thumb -piece","Большой палец частей","拇指件","الإبهام من قطعة و","Thumb - Stück","Thumb - piece","사무삐스","thumb - parça","拇指件","अँगूठा टुकड़ा","Thumb -piece","thumb - stuk"),
("Latch","ラッチ","pestillo","loquet","trinco","защелка","閂","مزلاج","Latch","Fermo","래치","mandal","闩","कुंडी","grendel","klink"),
("Cylinder","シリンダー","cilindro","cylindre","cilindro","цилиндр","氣缸","أسطوانة","Zylinder","cilindro","실린더","silindir","气缸","बेलन","silinder","cilinder"),
("Grip","グリップ","apretón","poignée","aperto","рукоятка","握","قبضة","Griff","presa","그립","kavrama","握","पकड़","pegangan","greep"),
("Bullet","弾丸","bala","balle","bala","пуля","子彈","رصاصة","Kugel","pallottola","총알","kurşun","子弹","गोली","peluru","kogel"),
("Cartridge","薬莢","cartucho","cartouche","cartucho","картридж","盒式磁帶","خرطوشة","Patrone","cartuccia","탄피","kartuş","盒式磁带","कारतूस","peluru","patroon"),
("Cartridge","カートリッジ","cartucho","cartouche","cartucho","картридж","盒式磁帶","خرطوشة","Patrone","cartuccia","카트리지","kartuş","盒式磁带","कारतूस","peluru","patroon"),
("Ammunition","弾薬","munición","munitions","munição","боеприпасы","彈藥","ذخيرة","Munition","cartucce","탄약","cephane","弹药","गोला बारूद","amunisi","munitie"),
("Lever","レバー","palanca","levier","alavanca","рычаг","槓桿","رافعة","Hebel","leva","레버","manivela","杠杆","लीवर","tuas","hefboom"),
("Axis","軸","eje","axe","eixo","ось","軸","محور","Achse","asse","축","eksen","轴","धुरी","sumbu","as"),
("Axis_of_rotation","回転軸","Eje de rotación","axe de rotation","eixo de rotação","ось вращения","旋轉軸","محور الدوران","Drehachse","asse di rotazione","회전축","dönme ekseni","旋转轴","रोटेशन की धुरी","sumbu rotasi","rotatieas"),
("Slider","スライダー","Deslizador","curseur","Slider","ползунок","滑塊","المنزلق","Slider","Slider","슬라이더","Slider","滑块","स्लाइडर","slider","schuif"),
("Switch","スイッチ","interruptor","commutateur","interruptor","переключатель","開關","تحول","Schalter","interruttore","스위치","şalter","开关","स्विच","saklar","schakelaar"),
("Knob","つまみ","perilla","bouton","botão","ручка","把手","مقبض الباب","Knopf","manopola","안주","topuz","把手","दस्ता","kenop","knop"),
("Hinge","ヒンジ","bisagra","charnière","dobradiça","петля","合頁","مفصل","Scharnier","cerniera","경첩","menteşe","合页","काज","engsel","scharnier"),
("Spring","バネ","primavera","printemps","primavera","весна","春天","ربيع","Frühling","primavera","스프링","bahar","春天","वसंत","musim semi","voorjaar"),
("Bolt","ボルト","tornillo","boulon","parafuso","болт","螺栓","صاعقة","Bolzen","bullone","볼트","cıvata","螺栓","पेंच","baut","bout"),
("Nut","ナット","tuerca","écrou","noz","гайка","堅果","جوز","Nuss","dado","너트","somun","坚果","अखरोट","kacang","moer"),
("Screw","ねじ","tornillo","hélice","parafuso","винт","螺絲釘","برغي","Schraube","vite","나사","vida","螺丝钉","स्क्रू","sekrup","schroef"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-")),
#---------Extra------
(("Extra:","エキストラ:","adicional:","supplémentaire:","extra:","Дополнительно:","額外：","إضافية :","Extra:","extra :","엑스트라 :","ekstra :","额外：","अतिरिक्त :","extra:","extra:"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("Flag","旗","bandera","drapeau","bandeira","флаг","旗","علم","Flagge","bandiera","깃발","bayrak","旗","झंडा","bendera","vlag"),
("Skirt","スカート","falda","jupe","saia","юбка","裙子","تنورة","Rock","gonna","스커트","etek","裙子","स्कर्ट","rok","rok"),
("Frill","フリル","volante","volant","babado","оборка","荷葉邊","هدب","Rüsche","fronzolo","프릴","fırfır","荷叶边","झालर","embel-embel","ruche"),
("Sleeve","袖","manga","manche","manga","рукав","套","كم","Ärmel","manicotto","소매","kol","套","आस्तीन","lengan","huls"),
("Collar","襟","collar","collier","colarinho","воротник","領","طوق","Kragen","collare","칼라","yaka","领","कालर","kerah","kraag"),
("Tie","ネクタイ","Tie","cravate","Laço","Наконечник","領帶","التعادل","Krawatte","Tie","넥타이","kravat","领带","टाई","Tie","tie"),
("Muffler","マフラー","silenciador","silencieux","silencioso","глушитель","消聲器","كاتم الصوت","Schalldämpfer","silenziatore","머플러","susturucu","消声器","मफलर","knalpot","geluiddemper"),
("Hat","帽子","sombrero","chapeau","chapéu","шляпа","帽子","قبعة","Hut","cappello","모자","şapka","帽子","टोपी","topi","hoed"),
("Glasses","メガネ","gafas","lunettes","óculos","очки","眼鏡","نظارات","Brille","occhiali","안경","gözlük","眼镜","चश्मा","kacamata","bril"),
("Tail","尾","cola","queue","cauda","хвост","尾","ذيل","Schwanz","coda","꼬리","kuyruk","尾","पूंछ","ekor","staart"),
("Stem","茎","tallo","tige","haste","стебель","幹","جذع","Stem","Stem","줄기","kök","干","तना","batang","stengel"),
("Flower","花","flor","fleur","flor","цветок","花","زهرة","Blume","fiore","꽃","çiçek","花","फूल","bunga","bloem"),
("Branch","枝","rama","branche","ramo","филиал","支","فرع","Zweig","ramo","가지","şube","支","शाखा","cabang","tak"),
("Rope","縄","cuerda","corde","corda","веревка","繩","حبل","Seil","corda","줄","halat","绳","रस्सी","tali","touw"),
("String","紐","cadena","chaîne","corda","строка","串","سلسلة","Schnur","stringa","끈","dizi","串","स्ट्रिंग","tali","snaar"),
("Curtain","カーテン","cortina","rideau","cortina","занавес","窗簾","ستارة","Vorhang","tenda","커튼","perde","窗帘","पर्दा","tirai","gordijn"),
("Feather","羽","pluma","plume","pena","перо","羽毛","ريشة","Feder","piuma","날개","tüy","羽毛","पंख","bulu","veer"),
("Wing","翼","ala","aile","asa","крыло","翼","جناح","Flügel","ala","날개","kanat","翼","पंख","sayap","vleugel"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-")),
#---------control(bottom)------
(("Control(bottom):","コントローラ(後方):","Controller (hacia atrás) :","Contrôleur ( arrière) :","Controller ( para trás) :","Контроллер (назад) :","控制器（向後） ：","تحكم ( الخلف ) :","Controller ( rückwärts) :","Controller ( indietro) :","컨트롤러 ( 후방 ) :","Denetleyici ( geriye ) :","控制器（向后） ：","नियंत्रक ( पिछड़े ) :","Controller ( mundur ) :","Controller ( achteruit) :"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("_IK","_IK","_IK","_IK","_IK","_IK","_IK","_IK","_IK","_IK","_IK","_IK","_IK","_IK","_IK","_IK"),
("_Controller","_コントローラ","_ Controller","_ contrôleur","_ Controlador","_ контроллер","_控制器","_ المراقب","_ -Controller","_ controller","_ 컨트롤러","_ Denetleyicisi","_控制器","_ नियंत्रक","_ Pengontrol","_ Controller"),
("_Constraint","_コンストレイント","_ Restricción","_ Contrainte","_ Restrição","_ Ограничения","_約束","_ القيد","_ Constraint","_ Vincolo","_ 구속 조건","_ Kısıtlama","_约束","_ बाधा","_ Kendala","_ Constraint"),
("_Target","_ターゲット","_ Target","_ cible","_ Alvo","_ Целевая","_目標","_ الهدف","_ Ziel","_ target","_ 대상","_ Hedef","_目标","_ लक्ष्य","_ Sasaran","_ Doel"),
("_Pole","_ポール","_ Paul","_ Paul","_ Paul","_ Павел","保羅_","_ بول","_ Paul","_ Paul","_ 폴","_ Paul","保罗_","_ पॉल","_ Paul","_ Paul"),
("_PoleTarget","_ポールターゲット","_ Meta Paul","_ Cible Paul","_ Alvo Paul","_ Павел цель","_保目標","_ بول الهدف","_ Paul Ziel","_ Bersaglio Paul","_ 폴 대상","_ Paul hedef","_保目标","_ पॉल लक्ष्य","_ Target Paul","_ Paul doel"),
("_Point_of_gaze","_注視点","_ Punto Gazing","_ Point de Contemplant","_ Ponto Gazing","_ Глядя точка","_注視點","_ نقطة التحديق","_ Blickpunkt","_ Punto Gazing","_ 주 시점","_ Gazing noktası","_注视点","_ अन्यमनस्कता बिंदु","_ Titik Gazing","_ Starend punt"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-")),
#---------LR------
(("LR:","LR:","LR:","LR:","LR:","LR:","LR:","LR:","LR:","LR:","LR:","LR:","LR:","LR:","LR:","LR:"),
("-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"),
(".L",".L",".L",".L",".L",".L",".L",".L",".L",".L",".L",".L",".L",".L",".L",".L"),
(".R",".R",".R",".R",".R",".R",".R",".R",".R",".R",".R",".R",".R",".R",".R",".R")),
#--------- Language -------
(("English","英語","Inglés","Anglais","Inglês","английский","英語","الإنجليزية","Englisch","inglese","영어","İngilizce","英語","अंग्रेज़ी ","Inggris","Engels"),
("Japanese","日本語","japonés","japonais","japonês","японский","日本","اليابانية","Japanisch","giapponese","일본어","Japon","日本語","जापानी","Jepang","Japanse"),
("Spanish","スペイン語","español","espagnol","espanhol","испанский","西班牙人","الأسبانية","Spanisch","spagnolo","스페인어","İspanyolca","スペイン語","स्पेनिश","Spanyol","Spaans"),
("French","フランス語","francés","français","francês","французский","法國人","فرنسي","Französisch","francese","프랑스어","Fransız","フランス語","फ्रेंच","Perancis","Frans"),
("Portuguese","ポルトガル語","portugués","Portugais","português","португальский","葡萄牙","البرتغالية","Portugiesisch","portoghese","포르투갈어","Portekizce","ポルトガル語","पुर्तगाली","Portugis","Portugees"),
("Russian","ロシア語","ruso","russe","russo","русский","俄","الروسية","Russisch","russo","러시아어","Rus","ロシア語","रूसी","Rusia","Russisch"),
("Chinese(Trad)","中国語（繁体）","Chino(trad)","Chinois(Trad)","Chinês(trad)","Китайский(традиционный)","中國（繁體）","الصينية(التقليدية)","Chinesisch(trad)","Cinese(Trad)","중국어(번체)","Çince(Geleneksel)","中国語（繁体）","चीनी(पारंपरिक)","Cina(Trad)","Chinees(trad)"),
("Arabic","アラビア語","árabe","arabe","árabe","арабский","阿拉伯語","العربية","Arabisch","arabo","아라비아어","Arapça","アラビア語","अरबीभाषा","Arab","Arabisch"),
("German","ドイツ語","alemán","allemand","alemão","немецкий","德語","ألماني","Deutsch","tedesco","독일어","Almanca","ドイツ語","जर्मन","Jerman","Duits"),
("Italian","イタリア語","italiano","italien","italiano","итальянский","意大利人","الإيطالي","Italienisch","italiano","이탈리아어","İtalyan","イタリア語","इतालवी","Italia","Italiaans"),
("Korean","韓国語","coreano","coréen","coreano","корейский","韓國","كوري","Koreanisch","coreano","한국어","Kore","韓国語","कोरियाई","Korea","Koreaans"),
("Turkish","トルコ語","turco","turc","turco","турецкий","土耳其","التركية","Türkisch","turco","터키어","Türk","トルコ語","तुर्की","Turki","Turks"),
("Chinese(Simplified)","中国語（簡体）","Chino(simplificado)","Chinois(simplifié)","Chinês(simplificado)","Китайский(упрощенный)","中國（簡體）","الصينية(المبسطة)","Chinesisch(vereinfacht)","Cinese(semplificato)","중국어(간체)","Çince(Basitleştirilmiş)","中国語（簡体）","चीनी(सरल)","Cina(Modern)","Chinees(vereenvoudigd)"),
("Hindi","ヒンディー語","hindi","hindi","hindi","хинди","印地文","الهندية","Hindi","hindi","힌디어","Hintçe","ヒンディー語","हिंदी","Hindi","Hindi"),
("Indonesian","インドネシア語","indonesio","indonésien","indonésio","индонезийский","印度尼西亞","الأندونيسية","Indonesier","indonesiano","인도네시아어","Endonezya","インドネシア語","इन्डोनेशियाई","Indonesia","Indonesisch"),
("Dutch","オランダ語","holandés","néerlandais","holandês","голландский","荷蘭人","هولندي","Holländisch","olandese","네덜란드어","Hollandalı","オランダ語","डच","Belanda","Nederlands")))

def lang():
    lngn = ('en_US','ja_JP','es','fr_FR','pt_BR','ru_RU','zh_TW','ar_EG','de_DE','it_IT','ko_KR','tr_TR','zh_CN','hi_IN','id_ID','nl_NL')
    system = bpy.context.user_preferences.system
    ct = 0
    if system.use_international_fonts:
        for i in lngn:
            if system.language == lngn[ct]:
                return ct
            ct += 1
    return 0

#    Menu in tools region
class Bmh2Panel(bpy.types.Panel):
    lng = lang()
    bl_category = "Tools"
    bl_label = mes.title[lng]
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
 
    def draw(self, context):
        obj = context.object

        lng = lang()
        layout = self.layout
        col = layout.column(align=True)

        col.label(text=mes.subtitle1[lng])
        self.layout.operator("create.bones")
        row = layout.row()
        row.prop(obj, "Bconnect", text=mes.bconnect[lang()])
 
        col = layout.column(align=True)
        row = col.row(align=True)
        row.operator("connect.bones",text=mes.btn02a[lng])
        row.operator("unconnect.bones",text=mes.btn02b[lng])
        
        self.layout.operator("create.mirrorbones")
 
        #col = layout.column(align=True)

        col = layout.column(align=True)
        col.label(text=mes.mir_label[lng])
        row = col.row(align=True)
        row.operator("mir.bonesl",text=mes.mir_bl_btn[lng])
        row.operator("mir.bonesr",text=mes.mir_br_btn[lng])

        self.layout.operator("bone.rename")

        col = layout.column(align=True)
        col.label(text=mes.subtitle2[lng])
        self.layout.operator("create.bevelcurve")
        self.layout.operator("conv.join")

        col = layout.column(align=True)
        col.label(text=mes.subtitle3[lng])
        row = col.row(align=True)
        row.operator("add.mmxbmh",text=mes.btn06a[lng])
        row.operator("add.mm_xbmh",text=mes.btn06b[lng])
        
        col = layout.column(align=True)
        col.label(text=mes.opt_title[lng])
        self.layout.operator("bone2.edge")
        row = layout.row()
        row.prop(obj, "Remdb", text=mes.rmd[lang()])
        layout.operator("sb.linked")
        layout.operator("link.renum")
               

#---- Error Dialog ----

bmh2mes = 'Please Select Edges.'
class ErrorDialog(bpy.types.Operator):
    bl_idname = "bmh2_error.dialog"
    bl_label = mes.warning[lang()]
    bl_options = {'REGISTER'}

    my_message = 'warnig'       
    def execute(self, context):
        print(self.my_message)
        return{'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def draw(self, context):
        global bmh2mes
        self.layout.label(bmh2mes)

def error(message):
    global bmh2mes
    bmh2mes = message
    bpy.ops.bmh2_error.dialog('INVOKE_DEFAULT')
        
#---- main ------

def createArmature(loc,eindex,vpos):
    bpy.ops.object.add(type='ARMATURE',enter_editmode=True,location=loc)
    ob = bpy.context.object
    ob.show_x_ray = True
    amt = ob.data

    ct = 0
    for i in eindex:
        bone = amt.edit_bones.new('bone')
        bone.head = vpos[eindex[ct][0]]
        bone.tail = vpos[eindex[ct][1]]
        ct += 1
    bpy.ops.armature.select_all(action='SELECT')
    bpy.ops.object.mode_set(mode='EDIT')
    return ob

class CreateBones(bpy.types.Operator):
    bl_idname = "create.bones"
    bl_label = mes.btn01[lang()]
    bl_options = {'REGISTER','UNDO'}

    def execute(self, context):
        
        connect = bpy.context.object.Bconnect 
        obj = bpy.context.active_object
        if obj.type != 'MESH':
            error(mes.select_mesh[lang()])
            return{'FINISHED'}

        vtdat = []
        egdat = []
        pos = []
        cobj = bpy.context.object
        cloc = cobj.location
        mesh = cobj.data
        vts = mesh.vertices
        eds = mesh.edges

        bpy.ops.object.mode_set(mode='OBJECT')
        for i in vts:
            pos.append(i.co.x)
            pos.append(i.co.y)
            pos.append(i.co.z)
            vtdat.append(pos)
            pos = []

        for i in eds:
            if i.select:
                pos.append(i.vertices[0])
                pos.append(i.vertices[1])
                egdat.append(pos)
                pos = []

        if len(egdat) < 1:
            error(mes.select_edge[lang()])
            bpy.ops.object.mode_set(mode='EDIT')
            return{'FINISHED'}

        createArmature(cloc,egdat,vtdat)
        if not connect:
            connectbones(True)
        
        bpy.ops.object.mode_set(mode='OBJECT')
        return{'FINISHED'}

#---------- ConnectBones -------------

def connectbones(mode):
    cobj = bpy.context.object
    amt = cobj.data
    bones = amt.edit_bones
    
    bpy.ops.object.mode_set(mode='EDIT')
    
    for i in bones:
        if i.select:
            for ii in bones:
                if i != ii:
                    if i.head == ii.tail:
                        i.parent = ii
                        i.use_connect = mode
                    

    return 1

def amtcheck():
    obj = bpy.context.active_object
    if obj.type != 'ARMATURE':
        error(mes.select_armature[lang()])
        return False
    if bpy.context.mode != 'EDIT_ARMATURE':
        bpy.ops.object.mode_set(mode='EDIT')
        error(mes.edit_armature[lang()])
        return False
    return True   

class ConnectBones(bpy.types.Operator):
    bl_idname = "connect.bones"
    bl_label = mes.btn02a[lang()]
    bl_options = {'REGISTER','UNDO'}

    def execute(self, context):

        if amtcheck():
            connectbones(True)        
            #bpy.ops.armature.calculate_roll(type='Y')

        return{'FINISHED'}

class UnconnectBones(bpy.types.Operator):
    bl_idname = "unconnect.bones"
    bl_label = mes.btn02b[lang()]
    bl_options = {'REGISTER','UNDO'}

    def execute(self, context):

        if amtcheck():
            connectbones(False)        

        return{'FINISHED'}

#---------- Create Mirror Bones -------------

def create_mb(str_L,str_R):
    cobj = bpy.context.object
    amt = cobj.data
    bones = amt.edit_bones
    
    bpy.ops.object.mode_set(mode='EDIT')
    sbones = []
 
    for i in bones:
        if i.select:
            if i.tail.x == 0 and i.head.x == 0:
                i.select = False
                i.select_head = False
                i.select_tail = False

    for i in bones:
        if i.select:
            i.name = i.name.replace(".L.","")
            i.name = i.name.replace(".R.","")
            i.name = i.name.replace(".","")
            if i.head.x > 0 or i.tail.x > 0:
                if i.name.rfind(str_L) == -1:
                    i.name += str_L
            elif i.head.x < 0 or i.tail.x < 0:
                if i.name.rfind(str_R) == -1:
                    i.name += str_R

    bpy.ops.object.editmode_toggle()
    bpy.ops.view3d.snap_cursor_to_selected()
    bpy.ops.object.editmode_toggle()

    pivot = bpy.context.space_data.pivot_point
    bpy.context.space_data.pivot_point = 'CURSOR'

    bpy.ops.armature.duplicate_move()
    bpy.ops.transform.resize(value=(-1, 1, 1), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.context.space_data.pivot_point = pivot

    cobj = bpy.context.object
    amt = cobj.data
    bones = amt.edit_bones
 
    str_Ld = str_L+'.001'
    str_Rd = str_R+'.001'

    for i in bones:
        if i.select:
            if i.name.rfind(str_Ld) != -1:
                i.name = i.name.replace(str_Ld,str_R,1)
            if i.name.rfind(str_Rd) != -1:
                i.name = i.name.replace(str_Rd,str_L,1)
            if i.parent:
                if i.name.rfind(str_L) != -1:
                    i.parent = bpy.context.object.data.edit_bones[i.parent.name.replace(str_R,str_L,1)]
                if i.name.rfind(str_R) != -1:
                    i.parent = bpy.context.object.data.edit_bones[i.parent.name.replace(str_L,str_R,1)]

    #bpy.ops.armature.calculate_roll(type='Y')
    return 1

class CreateMirrorBones(bpy.types.Operator):
    bl_idname = "create.mirrorbones"
    bl_label = mes.btn03[lang()]
    bl_options = {'REGISTER','UNDO'}

    def execute(self, context):

        str_L = '.L'
        str_R = '.R'
        
        obj = bpy.context.active_object
        if obj.type != 'ARMATURE':
            error(mes.select_armature[lang()])
            return{'FINISHED'}
        if bpy.context.mode != 'EDIT_ARMATURE':
            bpy.ops.object.mode_set(mode='EDIT')
            error(mes.edit_armature[lang()])
            return{'FINISHED'}

        create_mb(str_L,str_R)        
        return{'FINISHED'}

#---------- delete bones ---------------

def bone_select(bone,value):
    bone.select = value
    bone.select_head = value
    bone.select_tail = value

def delete_bones(delside):
    cobj = bpy.context.object
    amt = cobj.data
    bones = amt.edit_bones

    xm = bpy.context.object.data.use_mirror_x
    bpy.context.object.data.use_mirror_x = False


    for i in bones:
        bone_select(i,True)
        if i.head.x == 0:
            bone_select(i,False)
        elif delside == 'LEFT':
            if i.head.x > 0:
                bone_select(i,False)
        else:
            if i.head.x < 0:
                bone_select(i,False)
    bpy.ops.armature.delete()
    bpy.ops.armature.select_all(action='SELECT')

    for i in bones:
        if i.name.endswith(".L"):
            i.name = i.name.strip(".L")
        if i.name.endswith(".R"):
            i.name = i.name.strip(".R")
            
    create_mb('.L','.R')        
    bpy.context.object.data.use_mirror_x = xm

    return 0

class MirBonesL(bpy.types.Operator):
    bl_idname = "mir.bonesl"
    bl_label = mes.mir_bl_btn[lang()]
    bl_options = {'REGISTER','UNDO'}

    def execute(self, context):
        obj = bpy.context.active_object
        if obj.type != 'ARMATURE':
            error(mes.select_armature[lang()])
            return{'FINISHED'}
        if bpy.context.mode != 'EDIT_ARMATURE':
            bpy.ops.object.mode_set(mode='EDIT')
            error(mes.edit_armature[lang()])
            return{'FINISHED'}

        delete_bones('LEFT')    
        return{'FINISHED'}

class MirBonesR(bpy.types.Operator):
    bl_idname = "mir.bonesr"
    bl_label = mes.mir_br_btn[lang()]
    bl_options = {'REGISTER','UNDO'}

    def execute(self, context):
        obj = bpy.context.active_object
        if obj.type != 'ARMATURE':
            error(mes.select_armature[lang()])
            return{'FINISHED'}
        if bpy.context.mode != 'EDIT_ARMATURE':
            bpy.ops.object.mode_set(mode='EDIT')
            error(mes.edit_armature[lang()])
            return{'FINISHED'}

        delete_bones('RIGHT')    
        return{'FINISHED'}

#------------- bone rename -----------------

class BoneRename(bpy.types.Operator):
    lg = lang()
    bl_idname = "bone.rename"
    bl_label = mes.btn07[lg]
    bl_options = {'REGISTER'}

    my_ctt = EnumProperty(
        name = mes.rendata[0][0][lg],
        items = [
                 ('1',mes.rendata[0][1][lg],'1'),
                 ('2',mes.rendata[0][2][lg],'2'),
                 ('3',mes.rendata[0][3][lg],'3'),
                 ('4',mes.rendata[0][4][lg],'4'),
                 ('5',mes.rendata[0][5][lg],'5'),
                 ('6',mes.rendata[0][6][lg],'6'),
                 ('7',mes.rendata[0][7][lg],'7'),
                 ('8',mes.rendata[0][8][lg],'8'),
                 ('9',mes.rendata[0][9][lg],'9'),
                 ('10',mes.rendata[0][10][lg],'10'),
                 ('11',mes.rendata[0][11][lg],'11'),
                 ('12',mes.rendata[0][12][lg],'12'),
                 ('13',mes.rendata[0][13][lg],'13'),
                 ('14',mes.rendata[0][14][lg],'14'),
                 ('15',mes.rendata[0][15][lg],'15'),
                 ('16',mes.rendata[0][16][lg],'16'),
                 ('17',mes.rendata[0][17][lg],'17'),
                 ('18',mes.rendata[0][18][lg],'18'),
                 ('19',mes.rendata[0][19][lg],'19'),
                 ('20',mes.rendata[0][20][lg],'20'),
                 ('21',mes.rendata[0][21][lg],'21')],
                  default = '1')

    my_bdy = EnumProperty(
        name = mes.rendata[1][0][lg],
        items = [
                 ('1',mes.rendata[1][1][lg],'1'),
                 ('2',mes.rendata[1][2][lg],'2'),
                 ('3',mes.rendata[1][3][lg],'3'),
                 ('4',mes.rendata[1][4][lg],'4'),
                 ('5',mes.rendata[1][5][lg],'5'),
                 ('6',mes.rendata[1][6][lg],'6'),
                 ('7',mes.rendata[1][7][lg],'7'),
                 ('8',mes.rendata[1][8][lg],'8'),
                 ('9',mes.rendata[1][9][lg],'9'),
                 ('10',mes.rendata[1][10][lg],'10'),
                 ('11',mes.rendata[1][11][lg],'11'),
                 ('12',mes.rendata[1][12][lg],'12'),
                 ('13',mes.rendata[1][13][lg],'13'),
                 ('14',mes.rendata[1][14][lg],'14'),
                 ('15',mes.rendata[1][15][lg],'15'),
                 ('16',mes.rendata[1][16][lg],'16'),
                 ('17',mes.rendata[1][17][lg],'17'),
                 ('18',mes.rendata[1][18][lg],'18'),
                 ('19',mes.rendata[1][19][lg],'19'),
                 ('20',mes.rendata[1][20][lg],'20'),
                 ('21',mes.rendata[1][21][lg],'21'),
                 ('22',mes.rendata[1][22][lg],'22'),
                 ('23',mes.rendata[1][23][lg],'23'),
                 ('24',mes.rendata[1][24][lg],'24'),
                 ('25',mes.rendata[1][25][lg],'25')],
                 default = '1')

    my_arm = EnumProperty(
        name = mes.rendata[2][0][lg],
        items = [
                 ('1',mes.rendata[2][1][lg],'1'),
                 ('2',mes.rendata[2][2][lg],'2'),
                 ('3',mes.rendata[2][3][lg],'3'),
                 ('4',mes.rendata[2][4][lg],'4'),
                 ('5',mes.rendata[2][5][lg],'5'),
                 ('6',mes.rendata[2][6][lg],'6'),
                 ('7',mes.rendata[2][7][lg],'7'),
                 ('8',mes.rendata[2][8][lg],'8'),
                 ('9',mes.rendata[2][9][lg],'9'),
                 ('10',mes.rendata[2][10][lg],'10'),
                 ('11',mes.rendata[2][11][lg],'11'),
                 ('12',mes.rendata[2][12][lg],'12'),
                 ('13',mes.rendata[2][13][lg],'13'),
                 ('14',mes.rendata[2][14][lg],'14'),
                 ('15',mes.rendata[2][15][lg],'15'),
                 ('16',mes.rendata[2][16][lg],'16'),
                 ('17',mes.rendata[2][17][lg],'17'),
                 ('18',mes.rendata[2][18][lg],'18'),
                 ('19',mes.rendata[2][19][lg],'19'),
                 ('20',mes.rendata[2][20][lg],'20'),
                 ('21',mes.rendata[2][21][lg],'21'),
                 ('22',mes.rendata[2][22][lg],'22'),
                 ('23',mes.rendata[2][23][lg],'23'),
                 ('24',mes.rendata[2][24][lg],'24'),
                 ('25',mes.rendata[2][25][lg],'25')],
                 default = '1')

    my_foot = EnumProperty(
        name = mes.rendata[3][0][lg],
        items = [
                 ('1',mes.rendata[3][1][lg],'1'),
                 ('2',mes.rendata[3][2][lg],'2'),
                 ('3',mes.rendata[3][3][lg],'3'),
                 ('4',mes.rendata[3][4][lg],'4'),
                 ('5',mes.rendata[3][5][lg],'5'),
                 ('6',mes.rendata[3][6][lg],'6'),
                 ('7',mes.rendata[3][7][lg],'7'),
                 ('8',mes.rendata[3][8][lg],'8'),
                 ('9',mes.rendata[3][9][lg],'9'),
                 ('10',mes.rendata[3][10][lg],'10'),
                 ('11',mes.rendata[3][11][lg],'11'),
                 ('12',mes.rendata[3][12][lg],'12'),
                 ('13',mes.rendata[3][13][lg],'13'),
                 ('14',mes.rendata[3][14][lg],'14'),
                 ('15',mes.rendata[3][15][lg],'15'),
                 ('16',mes.rendata[3][16][lg],'16'),
                 ('17',mes.rendata[3][17][lg],'17'),
                 ('18',mes.rendata[3][18][lg],'18'),
                 ('19',mes.rendata[3][19][lg],'19'),
                 ('20',mes.rendata[3][20][lg],'20'),
                 ('21',mes.rendata[3][21][lg],'21'),
                 ('22',mes.rendata[3][22][lg],'22'),
                 ('23',mes.rendata[3][23][lg],'23'),
                 ('24',mes.rendata[3][24][lg],'24'),
                 ('25',mes.rendata[3][25][lg],'25'),
                 ('26',mes.rendata[3][26][lg],'26'),
                 ('27',mes.rendata[3][27][lg],'27'),
                 ('28',mes.rendata[3][28][lg],'28'),
                 ('29',mes.rendata[3][29][lg],'29'),
                 ('30',mes.rendata[3][30][lg],'30'),
                 ('31',mes.rendata[3][31][lg],'31'),
                 ('32',mes.rendata[3][32][lg],'32'),
                 ('33',mes.rendata[3][33][lg],'33'),
                 ('34',mes.rendata[3][34][lg],'34')],
                 default = '1')

    my_hp = EnumProperty(
        name = mes.rendata[4][0][lg],
        items = [
                 ('1',mes.rendata[4][1][lg],'1'),
                 ('2',mes.rendata[4][2][lg],'2'),
                 ('3',mes.rendata[4][3][lg],'3'),
                 ('4',mes.rendata[4][4][lg],'4'),
                 ('5',mes.rendata[4][5][lg],'5'),
                 ('6',mes.rendata[4][6][lg],'6'),
                 ('7',mes.rendata[4][7][lg],'7'),
                 ('8',mes.rendata[4][8][lg],'8'),
                 ('9',mes.rendata[4][9][lg],'9'),
                 ('10',mes.rendata[4][10][lg],'10'),
                 ('11',mes.rendata[4][11][lg],'11'),
                 ('12',mes.rendata[4][12][lg],'12'),
                 ('13',mes.rendata[4][13][lg],'13'),
                 ('14',mes.rendata[4][14][lg],'14'),
                 ('15',mes.rendata[4][15][lg],'15'),
                 ('16',mes.rendata[4][16][lg],'16'),
                 ('17',mes.rendata[4][17][lg],'17'),
                 ('18',mes.rendata[4][18][lg],'18'),
                 ('19',mes.rendata[4][19][lg],'19'),
                 ('20',mes.rendata[4][20][lg],'20'),
                 ('21',mes.rendata[4][21][lg],'21'),
                 ('22',mes.rendata[4][22][lg],'22')],
                 default = '1')


    my_hair = EnumProperty(
        name = mes.rendata[5][0][lg],
        items = [
                 ('1',mes.rendata[5][1][lg],'1'),
                 ('2',mes.rendata[5][2][lg],'2'),
                 ('3',mes.rendata[5][3][lg],'3'),
                 ('4',mes.rendata[5][4][lg],'4'),
                 ('5',mes.rendata[5][5][lg],'5'),
                 ('6',mes.rendata[5][6][lg],'6'),
                 ('7',mes.rendata[5][7][lg],'7'),
                 ('8',mes.rendata[5][8][lg],'8'),
                 ('9',mes.rendata[5][9][lg],'9'),
                 ('10',mes.rendata[5][10][lg],'10'),
                 ('11',mes.rendata[5][11][lg],'11'),
                 ('12',mes.rendata[5][12][lg],'12'),
                 ('13',mes.rendata[5][13][lg],'13'),
                 ('14',mes.rendata[5][14][lg],'14'),
                 ('15',mes.rendata[5][15][lg],'15'),
                 ('16',mes.rendata[5][16][lg],'16'),
                 ('17',mes.rendata[5][17][lg],'17'),
                 ('18',mes.rendata[5][18][lg],'18'),
                 ('19',mes.rendata[5][19][lg],'19'),
                 ('20',mes.rendata[5][20][lg],'20'),
                 ('21',mes.rendata[5][21][lg],'21'),
                 ('22',mes.rendata[5][22][lg],'22'),
                 ('23',mes.rendata[5][23][lg],'23'),
                 ('24',mes.rendata[5][24][lg],'24')],
                 default = '1')

    my_msl = EnumProperty(
        name = mes.rendata[6][0][lg],
        items = [
                 ('1',mes.rendata[6][1][lg],'1'),
                 ('2',mes.rendata[6][2][lg],'2'),
                 ('3',mes.rendata[6][3][lg],'3'),
                 ('4',mes.rendata[6][4][lg],'4'),
                 ('5',mes.rendata[6][5][lg],'5'),
                 ('6',mes.rendata[6][6][lg],'6'),
                 ('7',mes.rendata[6][7][lg],'7'),
                 ('8',mes.rendata[6][8][lg],'8'),
                 ('9',mes.rendata[6][9][lg],'9'),
                 ('10',mes.rendata[6][10][lg],'10'),
                 ('11',mes.rendata[6][11][lg],'11'),
                 ('12',mes.rendata[6][12][lg],'12'),
                 ('13',mes.rendata[6][13][lg],'13'),
                 ('14',mes.rendata[6][14][lg],'14'),
                 ('15',mes.rendata[6][15][lg],'15'),
                 ('16',mes.rendata[6][16][lg],'16'),
                 ('17',mes.rendata[6][17][lg],'17'),
                 ('18',mes.rendata[6][18][lg],'18'),
                 ('19',mes.rendata[6][19][lg],'19'),
                 ('20',mes.rendata[6][20][lg],'20'),
                 ('21',mes.rendata[6][21][lg],'21'),
                 ('22',mes.rendata[6][22][lg],'22'),
                 ('23',mes.rendata[6][23][lg],'23'),
                 ('24',mes.rendata[6][24][lg],'24'),
                 ('25',mes.rendata[6][25][lg],'25'),
                 ('26',mes.rendata[6][26][lg],'26'),
                 ('27',mes.rendata[6][27][lg],'27'),
                 ('28',mes.rendata[6][28][lg],'28'),
                 ('29',mes.rendata[6][29][lg],'29'),
                 ('30',mes.rendata[6][30][lg],'30'),
                 ('31',mes.rendata[6][31][lg],'31'),
                 ('32',mes.rendata[6][32][lg],'32')],
                 default = '1')

    my_bone = EnumProperty(
        name = mes.rendata[7][0][lg],
        items = [
                 ('1',mes.rendata[7][1][lg],'1'),
                 ('2',mes.rendata[7][2][lg],'2'),
                 ('3',mes.rendata[7][3][lg],'3'),
                 ('4',mes.rendata[7][4][lg],'4'),
                 ('5',mes.rendata[7][5][lg],'5'),
                 ('6',mes.rendata[7][6][lg],'6'),
                 ('7',mes.rendata[7][7][lg],'7'),
                 ('8',mes.rendata[7][8][lg],'8'),
                 ('9',mes.rendata[7][9][lg],'9'),
                 ('10',mes.rendata[7][10][lg],'10'),
                 ('11',mes.rendata[7][11][lg],'11'),
                 ('12',mes.rendata[7][12][lg],'12'),
                 ('13',mes.rendata[7][13][lg],'13'),
                 ('14',mes.rendata[7][14][lg],'14'),
                 ('15',mes.rendata[7][15][lg],'15'),
                 ('16',mes.rendata[7][16][lg],'16'),
                 ('17',mes.rendata[7][17][lg],'17'),
                 ('18',mes.rendata[7][18][lg],'18'),
                 ('19',mes.rendata[7][19][lg],'19'),
                 ('20',mes.rendata[7][20][lg],'20'),
                 ('21',mes.rendata[7][21][lg],'21'),
                 ('22',mes.rendata[7][22][lg],'22'),
                 ('23',mes.rendata[7][23][lg],'23'),
                 ('24',mes.rendata[7][24][lg],'24'),
                 ('25',mes.rendata[7][25][lg],'25'),
                 ('26',mes.rendata[7][26][lg],'26'),
                 ('27',mes.rendata[7][27][lg],'27'),
                 ('28',mes.rendata[7][28][lg],'28'),
                 ('29',mes.rendata[7][29][lg],'29'),
                 ('30',mes.rendata[7][30][lg],'30'),
                 ('31',mes.rendata[7][31][lg],'31'),
                 ('32',mes.rendata[7][32][lg],'32'),
                 ('33',mes.rendata[7][33][lg],'33'),
                 ('34',mes.rendata[7][34][lg],'34'),
                 ('35',mes.rendata[7][35][lg],'35')],
                 default = '1')

    my_mc = EnumProperty(
        name = mes.rendata[8][0][lg],
        items = [
                 ('1',mes.rendata[8][1][lg],'1'),
                 ('2',mes.rendata[8][2][lg],'2'),
                 ('3',mes.rendata[8][3][lg],'3'),
                 ('4',mes.rendata[8][4][lg],'4'),
                 ('5',mes.rendata[8][5][lg],'5'),
                 ('6',mes.rendata[8][6][lg],'6'),
                 ('7',mes.rendata[8][7][lg],'7'),
                 ('8',mes.rendata[8][8][lg],'8'),
                 ('9',mes.rendata[8][9][lg],'9'),
                 ('10',mes.rendata[8][10][lg],'10'),
                 ('11',mes.rendata[8][11][lg],'11'),
                 ('12',mes.rendata[8][12][lg],'12'),
                 ('13',mes.rendata[8][13][lg],'13'),
                 ('14',mes.rendata[8][14][lg],'14'),
                 ('15',mes.rendata[8][15][lg],'15'),
                 ('16',mes.rendata[8][16][lg],'16'),
                 ('17',mes.rendata[8][17][lg],'17'),
                 ('18',mes.rendata[8][18][lg],'18'),
                 ('19',mes.rendata[8][19][lg],'19'),
                 ('20',mes.rendata[8][20][lg],'20'),
                 ('21',mes.rendata[8][21][lg],'21'),
                 ('22',mes.rendata[8][22][lg],'22'),
                 ('23',mes.rendata[8][23][lg],'23'),
                 ('24',mes.rendata[8][24][lg],'24'),
                 ('25',mes.rendata[8][25][lg],'25'),
                 ('26',mes.rendata[8][26][lg],'26'),
                 ('27',mes.rendata[8][27][lg],'27'),
                 ('28',mes.rendata[8][28][lg],'28'),
                 ('29',mes.rendata[8][29][lg],'29'),
                 ('30',mes.rendata[8][30][lg],'30'),
                 ('31',mes.rendata[8][31][lg],'31'),
                 ('32',mes.rendata[8][32][lg],'32'),
                 ('33',mes.rendata[8][33][lg],'33'),
                 ('34',mes.rendata[8][34][lg],'34'),
                 ('35',mes.rendata[8][35][lg],'35'),
                 ('36',mes.rendata[8][36][lg],'36'),
                 ('37',mes.rendata[8][37][lg],'37'),
                 ('38',mes.rendata[8][38][lg],'38'),
                 ('39',mes.rendata[8][39][lg],'39'),
                 ('40',mes.rendata[8][40][lg],'40'),
                 ('41',mes.rendata[8][41][lg],'41'),
                 ('42',mes.rendata[8][42][lg],'42'),
                 ('43',mes.rendata[8][43][lg],'43'),
                 ('44',mes.rendata[8][44][lg],'44'),
                 ('45',mes.rendata[8][45][lg],'45'),
                 ('46',mes.rendata[8][46][lg],'46'),
                 ('47',mes.rendata[8][47][lg],'47'),
                 ('48',mes.rendata[8][48][lg],'48'),
                 ('49',mes.rendata[8][49][lg],'49'),
                 ('50',mes.rendata[8][50][lg],'50'),
                 ('51',mes.rendata[8][51][lg],'51'),
                 ('52',mes.rendata[8][52][lg],'52'),
                 ('53',mes.rendata[8][53][lg],'53'),
                 ('54',mes.rendata[8][54][lg],'54'),
                 ('55',mes.rendata[8][55][lg],'55'),
                 ('56',mes.rendata[8][56][lg],'56'),
                 ('57',mes.rendata[8][57][lg],'57'),
                 ('58',mes.rendata[8][58][lg],'58'),
                 ('59',mes.rendata[8][59][lg],'59'),
                 ('60',mes.rendata[8][60][lg],'60'),
                 ('61',mes.rendata[8][61][lg],'61'),
                 ('62',mes.rendata[8][62][lg],'62'),
                 ('63',mes.rendata[8][63][lg],'63'),
                 ('64',mes.rendata[8][64][lg],'64'),
                 ('65',mes.rendata[8][65][lg],'65'),
                 ('66',mes.rendata[8][66][lg],'46'),
                 ('67',mes.rendata[8][67][lg],'67')],
                 default = '1')

    my_mc2 = EnumProperty(
        name = mes.rendata[9][0][lg],
        items = [
                 ('1',mes.rendata[9][1][lg],'1'),
                 ('2',mes.rendata[9][2][lg],'2'),
                 ('3',mes.rendata[9][3][lg],'3'),
                 ('4',mes.rendata[9][4][lg],'4'),
                 ('5',mes.rendata[9][5][lg],'5'),
                 ('6',mes.rendata[9][6][lg],'6'),
                 ('7',mes.rendata[9][7][lg],'7'),
                 ('8',mes.rendata[9][8][lg],'8'),
                 ('9',mes.rendata[9][9][lg],'9'),
                 ('10',mes.rendata[9][10][lg],'10'),
                 ('11',mes.rendata[9][11][lg],'11'),
                 ('12',mes.rendata[9][12][lg],'12'),
                 ('13',mes.rendata[9][13][lg],'13'),
                 ('14',mes.rendata[9][14][lg],'14'),
                 ('15',mes.rendata[9][15][lg],'15'),
                 ('16',mes.rendata[9][16][lg],'16'),
                 ('17',mes.rendata[9][17][lg],'17'),
                 ('18',mes.rendata[9][18][lg],'18'),
                 ('19',mes.rendata[9][19][lg],'19'),
                 ('20',mes.rendata[9][20][lg],'20'),
                 ('21',mes.rendata[9][21][lg],'21'),
                 ('22',mes.rendata[9][22][lg],'22'),
                 ('23',mes.rendata[9][23][lg],'23'),
                 ('24',mes.rendata[9][24][lg],'24'),
                 ('25',mes.rendata[9][25][lg],'25'),
                 ('26',mes.rendata[9][26][lg],'26'),
                 ('27',mes.rendata[9][27][lg],'27'),
                 ('28',mes.rendata[9][28][lg],'28'),
                 ('29',mes.rendata[9][29][lg],'29'),
                 ('30',mes.rendata[9][30][lg],'30'),
                 ('31',mes.rendata[9][31][lg],'31'),
                 ('32',mes.rendata[9][32][lg],'32'),
                 ('33',mes.rendata[9][33][lg],'33'),
                 ('34',mes.rendata[9][34][lg],'34'),
                 ('35',mes.rendata[9][35][lg],'35'),
                 ('36',mes.rendata[9][36][lg],'36'),
                 ('37',mes.rendata[9][37][lg],'37'),
                 ('38',mes.rendata[9][38][lg],'38'),
                 ('39',mes.rendata[9][39][lg],'39'),
                 ('40',mes.rendata[9][40][lg],'40'),
                 ('41',mes.rendata[9][41][lg],'41'),
                 ('42',mes.rendata[9][42][lg],'42'),
                 ('43',mes.rendata[9][43][lg],'43'),
                 ('44',mes.rendata[9][44][lg],'44'),
                 ('45',mes.rendata[9][45][lg],'45'),
                 ('46',mes.rendata[9][46][lg],'46'),
                 ('47',mes.rendata[9][47][lg],'47'),
                 ('48',mes.rendata[9][48][lg],'48'),
                 ('49',mes.rendata[9][49][lg],'49'),
                 ('50',mes.rendata[9][50][lg],'50'),
                 ('51',mes.rendata[9][51][lg],'51'),
                 ('52',mes.rendata[9][52][lg],'52'),
                 ('53',mes.rendata[9][53][lg],'53'),
                 ('54',mes.rendata[9][54][lg],'54'),
                 ('55',mes.rendata[9][55][lg],'55'),
                 ('56',mes.rendata[9][56][lg],'56'),
                 ('57',mes.rendata[9][57][lg],'57'),
                 ('58',mes.rendata[9][58][lg],'58'),
                 ('59',mes.rendata[9][59][lg],'59'),
                 ('60',mes.rendata[9][60][lg],'60'),
                 ('61',mes.rendata[9][61][lg],'61'),
                 ('62',mes.rendata[9][62][lg],'62'),
                 ('63',mes.rendata[9][63][lg],'63'),
                 ('64',mes.rendata[9][64][lg],'64'),
                 ('65',mes.rendata[9][65][lg],'65'),
                 ('66',mes.rendata[9][66][lg],'46'),
                 ('67',mes.rendata[9][67][lg],'67')],
                 default = '1')

    my_mc3 = EnumProperty(
        name = mes.rendata[10][0][lg],
        items = [
                 ('1',mes.rendata[10][1][lg],'1'),
                 ('2',mes.rendata[10][2][lg],'2'),
                 ('3',mes.rendata[10][3][lg],'3'),
                 ('4',mes.rendata[10][4][lg],'4'),
                 ('5',mes.rendata[10][5][lg],'5'),
                 ('6',mes.rendata[10][6][lg],'6'),
                 ('7',mes.rendata[10][7][lg],'7'),
                 ('8',mes.rendata[10][8][lg],'8'),
                 ('9',mes.rendata[10][9][lg],'9'),
                 ('10',mes.rendata[10][10][lg],'10'),
                 ('11',mes.rendata[10][11][lg],'11'),
                 ('12',mes.rendata[10][12][lg],'12'),
                 ('13',mes.rendata[10][13][lg],'13'),
                 ('14',mes.rendata[10][14][lg],'14'),
                 ('15',mes.rendata[10][15][lg],'15'),
                 ('16',mes.rendata[10][16][lg],'16'),
                 ('17',mes.rendata[10][17][lg],'17'),
                 ('18',mes.rendata[10][18][lg],'18'),
                 ('19',mes.rendata[10][19][lg],'19'),
                 ('20',mes.rendata[10][20][lg],'20'),
                 ('21',mes.rendata[10][21][lg],'21'),
                 ('22',mes.rendata[10][22][lg],'22'),
                 ('23',mes.rendata[10][23][lg],'23'),
                 ('24',mes.rendata[10][24][lg],'24'),
                 ('25',mes.rendata[10][25][lg],'25'),
                 ('26',mes.rendata[10][26][lg],'26'),
                 ('27',mes.rendata[10][27][lg],'27'),
                 ('28',mes.rendata[10][28][lg],'28'),
                 ('29',mes.rendata[10][29][lg],'29'),
                 ('30',mes.rendata[10][30][lg],'30'),
                 ('31',mes.rendata[10][31][lg],'31'),
                 ('32',mes.rendata[10][32][lg],'32'),
                 ('33',mes.rendata[10][33][lg],'33'),
                 ('34',mes.rendata[10][34][lg],'34'),
                 ('35',mes.rendata[10][35][lg],'35'),
                 ('36',mes.rendata[10][36][lg],'36'),
                 ('37',mes.rendata[10][37][lg],'37'),
                 ('38',mes.rendata[10][38][lg],'38'),
                 ('39',mes.rendata[10][39][lg],'39'),
                 ('40',mes.rendata[10][40][lg],'40'),
                 ('41',mes.rendata[10][41][lg],'41'),
                 ('42',mes.rendata[10][42][lg],'42'),
                 ('43',mes.rendata[10][43][lg],'43'),
                 ('44',mes.rendata[10][44][lg],'44'),
                 ('45',mes.rendata[10][45][lg],'45'),
                 ('46',mes.rendata[10][46][lg],'46'),
                 ('47',mes.rendata[10][47][lg],'47'),
                 ('48',mes.rendata[10][48][lg],'48'),
                 ('49',mes.rendata[10][49][lg],'49'),
                 ('50',mes.rendata[10][50][lg],'50'),
                 ('51',mes.rendata[10][51][lg],'51'),
                 ('52',mes.rendata[10][52][lg],'52'),
                 ('53',mes.rendata[10][53][lg],'53'),
                 ('54',mes.rendata[10][54][lg],'54'),
                 ('55',mes.rendata[10][55][lg],'55'),
                 ('56',mes.rendata[10][56][lg],'56'),
                 ('57',mes.rendata[10][57][lg],'57'),
                 ('58',mes.rendata[10][58][lg],'58'),
                 ('59',mes.rendata[10][59][lg],'59'),
                 ('60',mes.rendata[10][60][lg],'60'),
                 ('61',mes.rendata[10][61][lg],'61'),
                 ('62',mes.rendata[10][62][lg],'62'),
                 ('63',mes.rendata[10][63][lg],'63'),
                 ('64',mes.rendata[10][64][lg],'64'),
                 ('65',mes.rendata[10][65][lg],'65'),
                 ('66',mes.rendata[10][66][lg],'46'),
                 ('67',mes.rendata[10][67][lg],'67')],
                 default = '1')

    my_ex = EnumProperty(
        name = mes.rendata[11][0][lg],
        items = [
                  ('1',mes.rendata[11][1][lg],'1'),
                 ('2',mes.rendata[11][2][lg],'2'),
                 ('3',mes.rendata[11][3][lg],'3'),
                 ('4',mes.rendata[11][4][lg],'4'),
                 ('5',mes.rendata[11][5][lg],'5'),
                 ('6',mes.rendata[11][6][lg],'6'),
                 ('7',mes.rendata[11][7][lg],'7'),
                 ('8',mes.rendata[11][8][lg],'8'),
                 ('9',mes.rendata[11][9][lg],'9'),
                 ('10',mes.rendata[11][10][lg],'10'),
                 ('11',mes.rendata[11][11][lg],'11'),
                 ('12',mes.rendata[11][12][lg],'12'),
                 ('13',mes.rendata[11][13][lg],'13'),
                 ('14',mes.rendata[11][14][lg],'14'),
                 ('15',mes.rendata[11][15][lg],'15'),
                 ('16',mes.rendata[11][16][lg],'16'),
                 ('17',mes.rendata[11][17][lg],'17'),
                 ('18',mes.rendata[11][18][lg],'18'),
                 ('19',mes.rendata[11][19][lg],'19'),
                 ('20',mes.rendata[11][20][lg],'20'),
                 ('21',mes.rendata[11][21][lg],'21'),
                 ('22',mes.rendata[11][22][lg],'22'),
                 ('23',mes.rendata[11][23][lg],'23'),
                 ('24',mes.rendata[11][24][lg],'24'),
                 ('25',mes.rendata[11][25][lg],'25'),
                 ('26',mes.rendata[11][26][lg],'26'),
                 ('27',mes.rendata[11][27][lg],'27'),
                 ('28',mes.rendata[11][28][lg],'28'),
                 ('29',mes.rendata[11][29][lg],'29'),
                 ('30',mes.rendata[11][30][lg],'30'),
                 ('31',mes.rendata[11][31][lg],'31'),
                 ('32',mes.rendata[11][32][lg],'32'),
                 ('33',mes.rendata[11][33][lg],'33'),
                 ('34',mes.rendata[11][34][lg],'34'),
                 ('35',mes.rendata[11][35][lg],'35'),
                 ('36',mes.rendata[11][36][lg],'36'),
                 ('37',mes.rendata[11][37][lg],'37'),
                 ('38',mes.rendata[11][38][lg],'38'),
                 ('39',mes.rendata[11][39][lg],'39'),
                 ('40',mes.rendata[11][40][lg],'40'),
                 ('41',mes.rendata[11][41][lg],'41'),
                 ('42',mes.rendata[11][42][lg],'42'),
                 ('43',mes.rendata[11][43][lg],'43'),
                 ('44',mes.rendata[11][44][lg],'44'),
                 ('45',mes.rendata[11][45][lg],'45'),
                 ('46',mes.rendata[11][46][lg],'46'),
                 ('47',mes.rendata[11][47][lg],'47'),
                 ('48',mes.rendata[11][48][lg],'48'),
                 ('49',mes.rendata[11][49][lg],'49'),
                 ('50',mes.rendata[11][50][lg],'50'),
                 ('51',mes.rendata[11][51][lg],'51')],
                 default = '1')

    my_ctb = EnumProperty(
        name = mes.rendata[12][0][lg],
        items = [
                 ('1',mes.rendata[12][1][lg],'1'),
                 ('2',mes.rendata[12][2][lg],'2'),
                 ('3',mes.rendata[12][3][lg],'3'),
                 ('4',mes.rendata[12][4][lg],'4'),
                 ('5',mes.rendata[12][5][lg],'5'),
                 ('6',mes.rendata[12][6][lg],'6'),
                 ('7',mes.rendata[12][7][lg],'7'),
                 ('8',mes.rendata[12][8][lg],'8'),
                 ('9',mes.rendata[12][9][lg],'9'),
                 ('10',mes.rendata[12][10][lg],'10'),
                 ('11',mes.rendata[12][11][lg],'11'),
                 ('12',mes.rendata[12][12][lg],'12'),
                 ('13',mes.rendata[12][13][lg],'13'),
                 ('14',mes.rendata[12][14][lg],'14'),
                 ('15',mes.rendata[12][15][lg],'15'),
                 ('16',mes.rendata[12][16][lg],'16'),
                 ('17',mes.rendata[12][17][lg],'17'),
                 ('18',mes.rendata[12][18][lg],'18'),
                 ('19',mes.rendata[12][19][lg],'19'),
                 ('20',mes.rendata[12][20][lg],'20'),
                 ('21',mes.rendata[12][21][lg],'21')],
                 default = '1')

    my_dlr = EnumProperty(
        name = mes.rendata[13][0][lg],
        items = [
                ('1',mes.rendata[13][1][lg],'1'),
                ('2',mes.rendata[13][2][lg],'2'),
                ('3',mes.rendata[13][3][lg],'3')],
                 default = '1')

    my_string = bpy.props.StringProperty(name=mes.str[lg],default = '')
    my_trlang = EnumProperty(
        name = mes.trns[lg],
        items = [
                 ('0',mes.rendata[14][0][lg],'0'),
                 ('1',mes.rendata[14][1][lg],'1'),
                 ('2',mes.rendata[14][2][lg],'2'),
                 ('3',mes.rendata[14][3][lg],'3'),
                 ('4',mes.rendata[14][4][lg],'4'),
                 ('5',mes.rendata[14][5][lg],'5'),
                 ('6',mes.rendata[14][6][lg],'6'),
                 ('7',mes.rendata[14][7][lg],'7'),
                 ('8',mes.rendata[14][8][lg],'8'),
                 ('9',mes.rendata[14][9][lg],'9'),
                 ('10',mes.rendata[14][10][lg],'10'),
                 ('11',mes.rendata[14][11][lg],'11'),
                 ('12',mes.rendata[14][12][lg],'12'),
                 ('13',mes.rendata[14][13][lg],'13'),
                 ('14',mes.rendata[14][14][lg],'14'),
                 ('15',mes.rendata[14][15][lg],'15')],
				 default = str(lg))


    def execute(self, context):
        str = self.my_string
        tr = int(self.my_trlang)
 
        rwd = [
                mes.rendata[0][int(self.my_ctt)][tr],
				mes.rendata[1][int(self.my_bdy)][tr],
				mes.rendata[2][int(self.my_arm)][tr],
				mes.rendata[3][int(self.my_foot)][tr],
				mes.rendata[4][int(self.my_hp)][tr],
				mes.rendata[5][int(self.my_hair)][tr],
				mes.rendata[6][int(self.my_msl)][tr],
				mes.rendata[7][int(self.my_bone)][tr],
				mes.rendata[8][int(self.my_mc)][tr],
				mes.rendata[9][int(self.my_mc2)][tr],
				mes.rendata[10][int(self.my_mc3)][tr],
				mes.rendata[11][int(self.my_ex)][tr],
				mes.rendata[12][int(self.my_ctb)][tr],
				mes.rendata[13][int(self.my_dlr)][tr]]

        ctt = mes.rendata[0][int(self.my_ctt)][tr]
        ctb = mes.rendata[12][int(self.my_ctb)][tr]
        dlr = mes.rendata[13][int(self.my_dlr)][tr]
               
        itms = ''
        for i in rwd:
            itms += i
        ostr = str
        str = itms+str
        str = str.replace('-','')
        if str == '':
            print('string is empty.')
            return{'FINISHED'}

        amt = bpy.context.object.data
        usemr = amt.use_mirror_x
        amt.use_mirror_x = True
        eblist = bpy.context.selected_editable_bones
        amt.use_mirror_x = False
        for i in eblist:
            i.use_deform = True
            if ctt != '-' or ctb != '-':
                i.use_deform = False
                bpy.ops.armature.calculate_roll(type='ACTIVE')

            if i.name.endswith('.L') and dlr == '-' and ostr == '':
                i.name = str
                i.name += '.L'
            elif i.name.endswith('.R') and dlr == '-' and ostr == '':
                i.name = str
                i.name += '.R'
            else:
                i.name = str
                
        for i in eblist:
            if '.L.' in i.name:
                i.name = i.name.replace('.L.','')
                i.name += '.L'
            if '.R.' in i.name:
                i.name = i.name.replace('.R.','')
                i.name += '.R'

        amt.use_mirror_x = usemr
        return{'FINISHED'}

    def invoke(self, context, event):
        if amtcheck():
            wm = context.window_manager
            return wm.invoke_props_dialog(self)
        return{'FINISHED'}

#---------- Create Bevel Curve -------------

def objselect(objct,selection):
    bpy.ops.object.mode_set(mode = 'OBJECT')
    if (selection == 'ONLY'):
        bpy.ops.object.select_all(action='DESELECT')
    bpy.context.scene.objects.active = objct
    objct.select = True

def mesh_separate():
    obj = bpy.context.object
    bpy.ops.object.mode_set(mode='EDIT')
    msh = bpy.ops.mesh
    msh.duplicate_move()
    msh.select_all(action='INVERT')
    msh.separate(type='SELECTED')
    msh.select_all(action='SELECT')
    msh.delete(type='ONLY_FACE')
    bpy.ops.object.mode_set(mode='OBJECT')
    objselect(obj,'ONLY')
    bpy.ops.object.convert(target='CURVE')

def curve_separate():
    obj = bpy.context.object
    bpy.ops.object.mode_set(mode='EDIT')
    cv = bpy.ops.curve
    cv.duplicate_move()
    cv.select_all(action='INVERT')
    bpy.ops.curve.separate()
    cv.select_all(action='SELECT')
    bpy.ops.object.mode_set(mode='OBJECT')
    objselect(obj,'ONLY')

def create_bc(obj,cvt):
    if obj.type == 'MESH':
        mesh_separate()
    elif obj.type == 'CURVE':
        curve_separate()
    else:
        print('Please Select Mesh or Curve Object.')        

    bpy.ops.mesh.primitive_circle_add(vertices=cvt,radius=0.1)
    bpy.ops.object.convert(target='CURVE')
    bevelobj = bpy.context.active_object

    objselect(obj,'ONLY')
    bpy.context.object.data.bevel_object = bevelobj
    objselect(bevelobj,'ONLY')                    
    return 1

def mccheck():
    cobj = bpy.context.active_object
    obj = bpy.ops.object

    obj.mode_set(mode='OBJECT')
    if cobj.type != 'MESH' and cobj.type != 'CURVE':
        error(mes.select_mesh_curve[lang()])
        return False             
    mesh = cobj.data    
    for i in mesh.edges:
        if i.select:
            return True
    obj.mode_set(mode='EDIT')
    error(mes.select_edge[lang()])
    return False             
    
class CreateBevelCurve(bpy.types.Operator):
    bl_idname = "create.bevelcurve"
    bl_label = mes.btn04[lang()]
    bl_options = {'REGISTER','UNDO'}

    my_cut = bpy.props.IntProperty(name=mes.dlg01[lang()],min=3,max=128,default = 6)

    def execute(self, context):
        obj = bpy.context.active_object
        cut = self.my_cut
        create_bc(obj,cut)

        return{'FINISHED'}

    def invoke(self, context, event):
        if mccheck():
            wm = context.window_manager
            return wm.invoke_props_dialog(self)
        return{'FINISHED'}

#------------ convert & join ----------------

class ConvJoin(bpy.types.Operator):
    bl_idname = "conv.join"
    bl_label = mes.btn05[lang()]
    bl_options = {'REGISTER','UNDO'}

    def execute(self, context):
        bpy.ops.object.mode_set(mode='OBJECT')
        cobj = bpy.context.object
        if cobj.type != 'CURVE':
            error(mes.select_curve[lang()])
            return{'FINISHED'}
        bpy.ops.object.convert(target='MESH')
        bpy.ops.object.join()
        return{'FINISHED'}

#------------ Add Mirror Moidifier ----------------

def addmirrormod(direct):

    obj = bpy.ops.object

    obj.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='DESELECT')
    obj.mode_set(mode='OBJECT')
    cobj = bpy.context.object
    mesh = cobj.data

    for vertex in mesh.vertices:
        if direct == 'X':
            if (vertex.co.x < -0.000001):
                vertex.select = True
        else:
           if (vertex.co.x > 0.000001):
                vertex.select = True
             
    obj.mode_set(mode='OBJECT')
    obj.mode_set(mode='EDIT')
    bpy.ops.mesh.delete(type='VERT')
    bpy.ops.object.modifier_add(type='MIRROR')
    for i in bpy.context.object.modifiers:
        mname = i.name
    bpy.context.object.modifiers[mname].use_clip = True
    return 1

def meshcheck():
    obj = bpy.context.active_object
    if obj.type != 'MESH':
        error(mes.select_mesh[lang()])
        return False
    return True   

class AddMmx_Bmh(bpy.types.Operator):
    bl_idname = "add.mmxbmh"
    bl_label = mes.btn06a[lang()]
    bl_options = {'REGISTER'}

    def execute(self, context):
        if meshcheck():
            addmirrormod('X')       
        return{'FINISHED'}

class AddMm_x_Bmh(bpy.types.Operator):
    bl_idname = "add.mm_xbmh"
    bl_label = mes.btn06b[lang()]
    bl_options = {'REGISTER'}

    def execute(self, context):
        if meshcheck():
            addmirrormod('-X')       
        return{'FINISHED'}

#---------- option -----------

def obtype(otype):
    obj = bpy.context.active_object
    if obj.type != otype:
        error(mes.select_armature[lang()])
        return False
    return True
    
def draw_edges(pos,bct):
    remdbls = bpy.context.object.Remdb
    bpy.ops.object.mode_set(mode='OBJECT')
    me = bpy.data.meshes.new("myMesh")		#中身が空のメッシュオブジェクトを作成
    ob = bpy.data.objects.new("my_mesh", me)	#オブジェクト内にメッシュを作成

    ob.location = bpy.context.scene.cursor_location	#３Ｄカーソルの位置
    bpy.context.scene.objects.link(ob)		#オブジェクトをシーンにリンク
    bpy.ops.object.mode_set(mode='EDIT')

    #----------------- 辺作成 -------------------
    #辺を結ぶ順番
    edges = []
    ct =  0
    for i in range(0,bct):
        edges.append((ct, ct+1))
        ct += 2
    me.from_pydata(pos,edges,[])	#辺作成
    me.update(calc_edges=True)		#メッシュを更新
    objselect(ob, 'ONLY')
    if not remdbls:
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.remove_doubles()

def set_pos(pos):
    cobj = bpy.context.object
    amt = cobj.data
    bones = amt.edit_bones
    
    bpy.ops.object.mode_set(mode='EDIT')
    bct = 0
    for i in bones:
        if i.select:
            pos.append((i.head.x,i.head.y,i.head.z))
            pos.append((i.tail.x,i.tail.y,i.tail.z))                    
            bct += 1
    return bct

class Bone2Edge(bpy.types.Operator):

    bl_idname = "bone2.edge"
    bl_label = mes.opt_btn1[lang()]
    bl_options = {'REGISTER'}

    def execute(self, context):
        if obtype('ARMATURE'):
            pos = []
            bct = set_pos(pos)
            draw_edges(pos,bct)
            bpy.ops.object.mode_set(mode='OBJECT')
        
        return{'FINISHED'}

#-------- bone link select ---------

def countbone(ctype):
    bones = bpy.context.object.data.edit_bones
    ct = 0
    if ctype == 'ALL':
        for i in bones:
            ct += 1
    else:
        for i in bones:
            if i.select:
                ct += 1
    return ct
    
class SelectBoneLinked(bpy.types.Operator):
    bl_idname = "sb.linked"
    bl_label = mes.opt_btn2[lang()]
    bl_options = {'REGISTER'}

    def execute(self, context):
        if obtype('ARMATURE'):
            bpy.ops.object.mode_set(mode='EDIT')
            for i in range(0,countbone('ALL')):
                bpy.ops.armature.select_more()
        return{'FINISHED'}

#-------- link renumber ---------

def set_bone_num(sbone):

    bones = []
    bone = bpy.context.object.data.edit_bones
    bones.append(sbone)
    bname = re.split(r'\d{3}', sbone.name)
    if len(bname) == 1:
        bname[0] += "."
        bname.append("DUMMY")
    for i in bone:
        if sbone.use_connect:
            bones.append(sbone.parent)
            sbone = sbone.parent
        else:
            break

    sct = len(bones)-1
    dmy = 'bmh2dummy'
    for i in bones:
        i.name = dmy+str(sct).zfill(3)+"."+bname[1]
        sct -= 1

    for i in bones:
        i.name = i.name.replace(dmy,bname[0])
        if i.name.find("000"):
            i.name = i.name.replace("000","")
        if i.name.find(".."):
            i.name = i.name.replace("..",".")
        if i.name.endswith("."):
            i.name = i.name.strip(".")
        i.name = i.name.replace(".DUMMY","")
        
class LinkRenum(bpy.types.Operator):
    bl_idname = "link.renum"
    bl_label = mes.linkrenum_btn[lang()]
    bl_options = {'REGISTER','UNDO'}

    def execute(self, context):
        if obtype('ARMATURE'):
            bpy.ops.object.mode_set(mode='EDIT')
            ct = countbone('SELECTED')
            if not ct == 1:
                error(mes.linkrenum[lang()])
                return{'FINISHED'}

            bones = []
            cobj = bpy.context.object
            amt = cobj.data
            bone = amt.edit_bones
        
            sbone = bone.active
            bones.append(sbone)

            mbonename = ''
            if sbone.name.endswith(".L"):
                mbonename = sbone.name.replace(".L",".R")
            elif sbone.name.endswith(".R"):
                mbonename = sbone.name.replace(".R",".L")

            set_bone_num(sbone)
            mexist = False
            for i in bone:
                if i.name == mbonename:
                    mexist = True
                    break
            if mexist:
                set_bone_num(bone[mbonename])
                
        return{'FINISHED'}

#======== Registration ==========

def add_select_link(self, context):
    self.layout.operator(
        SelectBoneLinked.bl_idname,
        text = mes.blinked[lang()])

def register():
    bpy.utils.register_class(Bmh2Panel)
    bpy.utils.register_class(CreateBones)
    bpy.types.Object.Bconnect = bpy.props.BoolProperty()
    bpy.utils.register_class(ConnectBones)
    bpy.utils.register_class(UnconnectBones)
    bpy.utils.register_class(CreateMirrorBones)
    bpy.utils.register_class(MirBonesL)
    bpy.utils.register_class(MirBonesR)
    
    bpy.utils.register_class(CreateBevelCurve)
    bpy.utils.register_class(BoneRename)
    bpy.utils.register_class(ConvJoin)
    bpy.utils.register_class(AddMmx_Bmh)
    bpy.utils.register_class(AddMm_x_Bmh)
    bpy.types.Object.Remdb = bpy.props.BoolProperty()
    bpy.utils.register_class(Bone2Edge)
    bpy.utils.register_class(SelectBoneLinked)
    bpy.utils.register_class(LinkRenum)

    bpy.utils.register_class(ErrorDialog)
    kc = bpy.context.window_manager.keyconfigs.addon
    if kc:
        kma = kc.keymaps.new(name="Armature", space_type="EMPTY")
        kmi1 = kma.keymap_items.new('bone.rename', 'R', 'PRESS', alt=True)
        kmi2 = kma.keymap_items.new('sb.linked', 'L', 'PRESS', ctrl=True)
        kmi3 = kma.keymap_items.new('bone2.edge', 'E', 'PRESS', alt=True, shift=True)
        kmi4 = kma.keymap_items.new('create.mirrorbones', 'M', 'PRESS', alt=True, shift=True)
        kmi5 = kma.keymap_items.new('mir.bonesl', 'R', 'PRESS', alt=True, shift=True)
        kmi6 = kma.keymap_items.new('mir.bonesr', 'L', 'PRESS', alt=True, shift=True)
        kmi7 = kma.keymap_items.new('connect.bones', 'C', 'PRESS', alt=True)
        kmi8 = kma.keymap_items.new('unconnect.bones', 'U', 'PRESS', alt=True)
        kmi9 = kma.keymap_items.new('link.renum', 'N', 'PRESS', alt=True, shift=True)

        kmm = kc.keymaps.new(name="Mesh", space_type="EMPTY")
        kmi10 = kmm.keymap_items.new('create.bones', 'B', 'PRESS', alt=True, shift=True)
        kmi11 = kmm.keymap_items.new('create.bevelcurve', 'C', 'PRESS', alt=True, shift=True)
        kmi12 = kmm.keymap_items.new('add.mmxbmh', 'R', 'PRESS', alt=True, shift=True)
        kmi13 = kmm.keymap_items.new('add.mm_xbmh', 'L', 'PRESS', alt=True, shift=True)

        kmc = kc.keymaps.new(name="Object Mode", space_type="EMPTY")
        kmi14 = kmc.keymap_items.new('conv.join', 'J', 'PRESS', alt=True, shift=True)
        kmi15 = kmc.keymap_items.new('create.bones', 'B', 'PRESS', alt=True, shift=True)
        kmi16 = kmc.keymap_items.new('create.bevelcurve', 'C', 'PRESS', alt=True, shift=True)
        kmi17 = kmc.keymap_items.new('bone2.edge', 'E', 'PRESS', alt=True, shift=True)
    #bpy.types.VIEW3D_MT_select_edit_armature.append(add_select_link)

def unregister():
    bpy.utils.unregister_class(Bmh2Panel)
    bpy.utils.unregister_class(CreateBones)
    bpy.utils.unregister_class(ConnectBones)
    bpy.utils.unregister_class(UnconnectBones)
    bpy.utils.unregister_class(CreateMirrorBones)
    bpy.utils.unregister_class(MirBonesL)
    bpy.utils.unregister_class(MirBonesR)
    
    bpy.utils.unregister_class(CreateBevelCurve)
    bpy.utils.unregister_class(BoneRename)
    bpy.utils.unregister_class(ConvJoin)
    bpy.utils.unregister_class(AddMmx_Bmh)
    bpy.utils.unregister_class(AddMm_x_Bmh)
    bpy.utils.unregister_class(Bone2Edge)
    bpy.utils.unregister_class(SelectBoneLinked)
    bpy.utils.register_class(LinkRenum)

    bpy.utils.unregister_class(ErrorDialog)
    kc = bpy.context.window_manager.keyconfigs.addon
    if kc:
        km = kc.keymaps["Armature"]
        for kmi in km.keymap_items:
            if kmi.idname == 'bone.rename':
                km.keymap_items.remove(kmi)
            if kmi.idname == 'sb.linked':
                km.keymap_items.remove(kmi)
            if kmi.idname == 'bone2.edge':
                km.keymap_items.remove(kmi)
            if kmi.idname == 'create.mirrorbones':
                km.keymap_items.remove(kmi)
            if kmi.idname == 'mir.bonesl':
                km.keymap_items.remove(kmi)
            if kmi.idname == 'mir.bonesr':
                km.keymap_items.remove(kmi)
            if kmi.idname == 'connect.bones':
                km.keymap_items.remove(kmi)
            if kmi.idname == 'unconnect.bones':
                km.keymap_items.remove(kmi)
            if kmi.idname == 'link.renum':
                km.keymap_items.remove(kmi)
                #break
        km = kc.keymaps["Mesh"]
        for kmi in km.keymap_items:
            if kmi.idname == 'create.bones':
                km.keymap_items.remove(kmi)
            if kmi.idname == 'create.bevelcurve':
                km.keymap_items.remove(kmi)
            if kmi.idname == 'add.mmxbmh':
                km.keymap_items.remove(kmi)
            if kmi.idname == 'add.mm_xbmh':
                km.keymap_items.remove(kmi)
        km = kc.keymaps["Object Mode"]
        for kmi in km.keymap_items:
            if kmi.idname == 'create.bones':
                km.keymap_items.remove(kmi)
            if kmi.idname == 'conv.join':
                km.keymap_items.remove(kmi)
            if kmi.idname == 'bone2.edge':
                km.keymap_items.remove(kmi)
            
    #bpy.types.VIEW3D_MT_select_edit_armature.remove(add_select_link)

if __name__ == "__main__":
    register()









