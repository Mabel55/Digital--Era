import os

def upload_to_tiktok(video_file, description):
    """
    Uploads a video to TikTok using the tiktok-uploader package and Playwright.
    Requires a cookies.txt file containing your TikTok session cookies.
    """
    print("\nPreparing to upload to TikTok...")
    
    cookie_file = None
    if os.path.exists("cookies.txt"):
        cookie_file = "cookies.txt"
    elif os.path.exists("cookies.json"):
        cookie_file = "cookies.json"
        
    if not cookie_file:
        print("[!] Error: cookies.txt or cookies.json not found.")
        print("[!] To upload to TikTok, you must export your cookies from tiktok.com")
        print("[!] using the Cookie-Editor extension and save them as 'cookies.txt'.")
        return False
        
    try:
        from tiktok_uploader.upload import upload_video
        import json
        
        print(f"Uploading {video_file} to TikTok...")
        print("This runs a hidden browser to upload the video. Please wait...")
        
        # Load the cookies from file
        cookies_list = []
        try:
            with open(cookie_file, 'r', encoding='utf-8') as f:
                if cookie_file.endswith('.json'):
                    cookies_list = json.load(f)
        except Exception as e:
            print(f"[!] Could not load cookie file: {e}")
            
        # Convert JSON cookies to Netscape format string if we loaded JSON
        cookies_str = None
        if cookies_list:
            netscape_lines = ["# Netscape HTTP Cookie File"]
            for c in cookies_list:
                domain = c.get('domain', '.tiktok.com')
                # Netscape format: domain, include_subdomains, path, https, expires, name, value
                include_subdomains = "TRUE" if domain.startswith('.') else "FALSE"
                path = c.get('path', '/')
                secure = "TRUE" if c.get('secure', True) else "FALSE"
                expires = str(int(c.get('expirationDate', c.get('expires', 0))))
                name = c.get('name', '')
                value = c.get('value', '')
                netscape_lines.append(f"{domain}\t{include_subdomains}\t{path}\t{secure}\t{expires}\t{name}\t{value}")
            cookies_str = "\n".join(netscape_lines)
            
            # Write to a temporary netscape file
            with open("netscape_cookies.txt", "w", encoding='utf-8') as f:
                f.write(cookies_str)
            cookie_path = "netscape_cookies.txt"
        else:
            cookie_path = cookie_file
            
        failed_uploads = upload_video(
            filename=video_file,
            description=description,
            cookies=cookie_path,
            headless=False # Set to False temporarily so the user can close the popup!
        )
        
        # Cleanup
        if os.path.exists("netscape_cookies.txt"):
            os.remove("netscape_cookies.txt")
            
        if failed_uploads:
            print("[!] Failed to upload to TikTok.")
            return False
            
        print("Video uploaded to TikTok successfully!")
        return True
        
    except ImportError:
        print("[!] tiktok-uploader is not installed.")
        print("[!] Please run: pip install tiktok-uploader playwright && playwright install chromium")
        return False
    except Exception as e:
        print(f"[!] An error occurred during TikTok upload: {e}")
        return False

if __name__ == "__main__":
    upload_to_tiktok("final_output.mp4", "Testing automated upload! #viral #mystery")
