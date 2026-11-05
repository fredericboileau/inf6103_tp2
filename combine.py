#!/usr/bin/env python3
import itertools
import sys

def combine_wordlists(user_file, pass_file, output_file):
    try:
        # Read files and strip invisible carriage returns (\r) and newlines (\n)
        with open(user_file, 'r', encoding='utf-8', errors='ignore') as f:
            users = [line.strip() for line in f if line.strip()]
            
        with open(pass_file, 'r', encoding='utf-8', errors='ignore') as f:
            passwords = [line.strip() for line in f if line.strip()]

        # Generate cross-product matrix using fast C-optimized itertools
        pairs = itertools.product(users, passwords)

        # Write out to the new combined file cleanly
        with open(output_file, 'w', encoding='utf-8') as f:
            # Join with newline for maximum I/O performance
            f.write('\n'.join(f"{u}:{p}" for u, p in pairs) + '\n')
            
        print(f"[+] Successfully generated {len(users) * len(passwords)} credential pairs.")

    except FileNotFoundError as e:
        print(f"[-] Error: {e.strerror} ({e.filename})", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    # Change these filenames if yours are named differently
    combine_wordlists("usernames.txt", "passwords.txt", "combined_pairs.txt")
