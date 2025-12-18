#!/usr/bin/env python3
"""
Eye Mouse - Entry Point
Gaze-controlled cursor application
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    try:
        from src.gui.main_window import main
        main()
    except Exception as e:
        import traceback
        error_msg = f"HATA OLUSTU:\n{str(e)}\n\nDETAYLAR:\n{traceback.format_exc()}"
        
        try:
            # Log dosyasini KULLANICI ANA DIZININE kaydet (En guvenli ve izin sorunu olmayan yer)
            home_path = os.path.expanduser("~")
            log_path = os.path.join(home_path, "Cyclops_DEBUG.txt")
            
            with open(log_path, "w", encoding="utf-8") as f:
                f.write(error_msg)
                
            print(f"Log dosyasina yazildi: {log_path}")
                
            # Eger PyQt yukluyse popup goster
            try:
                from PyQt6.QtWidgets import QApplication, QMessageBox
                if QApplication.instance():
                    QMessageBox.critical(None, "Kritik Hata", f"Uygulama coktu!\nHata logu şuraya kaydedildi:\n{log_path}\n\nHata: {str(e)}")
            except:
                pass
        except Exception as log_error:
            print(f"KRITIK: Log yazarken hata oldu: {log_error}")
            print(error_msg)
        
        sys.exit(1)
