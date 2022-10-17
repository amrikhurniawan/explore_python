"""
 * ============ 
 * ACCESS LEVEL
 * ============
 * 
 * Jika access kosong, maka tampilkan "Input access"
 * Access public, jika level di bawah 5 maka tampilkan "Public di bawah 5"
 * Access public, jika level di atas 5 maka tampilkan "Public di atas 5"
 * Access public, jika level sama dengan 5 maka tampilkan "Public five"
 *
 * Access private, jika level di bawah 5 maka tampilkan "Private di bawah 5"
 * Access private, jika level di atas 5 maka tampilkan "Private di atas 5"
 * Access private, jika level sama dengan 5 maka tampilkan "Private five"
 *
 * Access protected, jika level di bawah 5 maka tampilkan "Protected di bawah 5"
 * Access protected, jika level di atas 5 maka tampilkan "Protected di atas 5"
 * Access protected, jika level sama dengan 5 maka tampilkan "Protected five"
 *
 * Jika access salah, tampilkan "Access is not defined"
"""

access = ""
level = 5

if (access == "private" and level < 5):
    print("Private dibawah 5")
elif (access == "private" and level > 5):
    print("Private diatas 5")
elif (access == "private" and level == 5):
    print("Private five")
elif (access == "protected" and level < 5):
    print("Protected dibawah 5")
elif (access == "protected" and level > 5):
    print("Protected diatas dengan 5")
elif (access == "protected" and level == 5):
    print("Protected five")
elif (access == "public" and level < 5):
    print("Public dibawah 5")
elif (access == "public" and level > 5):
    print("Public diatas 5")
elif (access == "public" and level == 5):
    print("Public five")
elif (access == ""):
    print("Access kosong")
else:
    print("Access Denied")
