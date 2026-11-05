
#!/usr/bin/env python3
import itertools
import base64
import sys

def generate_b64_wordlist(user_file, pass_file, output_file):
    try:
        # Open files with ignore errors to prevent crashes on non-UTF-8 chars
        with open(user_file, 'r', encoding='utf-8', errors='ignore') as f:
            users = [line.strip() for line in f if line.strip()]
            
        with open(pass_file, 'r', encoding='utf-8', errors='ignore') as f:
            passwords = [line.strip() for line in f if line.strip()]

        print(f"[*] Processing {len(users)} users and {len(passwords)} passwords...")

        # Generate every possible combination
        combinations = itertools.product(users, passwords)

        with open(output_file, 'w', encoding='utf-8') as f:
            for user, password in combinations:
                # 1. Format the standard basic auth string
                raw_pair = f"{user}:{password}"
                
                # 2. Encode to bytes, apply base64, and decode back to a clean string
                b64_encoded = base64.b64encode(raw_pair.encode('utf-8')).decode('utf-8')
                
                # 3. Write out directly to the file
                f.write(b64_encoded + '\n')
                
        print(f"[+] Successfully generated {len(users) * len(passwords)} Base64 encoded lines in '{output_file}'.")

    except FileNotFoundError as e:
        print(f"[-] Error: {e.strerror} ({e.filename})", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    generate_b64_wordlist("usernames.txt", "passwords.txt", "b64_pairs.txt")
