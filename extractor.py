import os
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

image_path = "/sdcard/DCIM/Camera/photo.jpg"

if not os.path.exists(image_path):
    print("\n[-] لم يتم العثور على الصورة!")
else:
    try:
        img = Image.open(image_path)
        info = img._getexif()
        
        if info:
            print("\n[+] تم استخراج البيانات بنجاح:\n")
            print("=" * 40)
            for tag_id, value in info.items():
                tag_name = TAGS.get(tag_id, tag_id)
                
                if tag_name in ['Make', 'Model', 'DateTimeOriginal']:
                    print(f"📌 {tag_name}: {value}")
                
                # هنا سنقوم بتفكيك قاموس الـ GPS وطباعة كل محتوياته
                elif tag_name == 'GPSInfo':
                    print("\n📍 --- تفاصيل الموقع الجغرافي المخفية ---")
                    for gps_tag in value:
                        sub_tag = GPSTAGS.get(gps_tag, gps_tag)
                        print(f"   {sub_tag}: {value[gps_tag]}")
            print("=" * 40)
        else:
            print("\n[-] لا توجد بيانات مخفية.")
            
    except Exception as e:
        print(f"\n[-] خطأ: {e}")

