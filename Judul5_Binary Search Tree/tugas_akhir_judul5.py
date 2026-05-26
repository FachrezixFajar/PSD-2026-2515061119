class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BSTDasar:
    def __init__(self):
        self.root = None

    def insert_node(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert_node(root.left, key)
        elif key > root.key:
            root.right = self.insert_node(root.right, key)
        return root

    def insert(self, key):
        self.root = self.insert_node(self.root, key)

    def search_node(self, root, key):
        if root is None:
            return False
        if root.key == key:
            return True
        if key < root.key:
            return self.search_node(root.left, key)
        return self.search_node(root.right, key)

    def search(self, key):
        return self.search_node(self.root, key)

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.key, end=" ")
        self.inorder(root.right)

    def preorder(self, root):
        if root is None:
            return
        print(root.key, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.key, end=" ")

    def find_min(self, root):
        if root is None:
            return -1
        current = root
        while current.left is not None:
            current = current.left
        return current.key

    def find_max(self, root):
        if root is None:
            return -1
        current = root
        while current.right is not None:
            current = current.right
        return current.key

    def count_nodes(self, root):
        if root is None:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

    def sum_nodes(self, root):
        if root is None:
            return 0
        return root.key + self.sum_nodes(root.left) + self.sum_nodes(root.right)


def main():
    boss_level = BSTDasar()
    pilih = 0

    while pilih != 10:
        print("\n=== Sistem Level Boss Wuthering Waves ===")
        print("1. Tambah Level Boss")
        print("2. Cari Level Boss")
        print("3. Tampilkan Level Boss Terurut")
        print("4. Tampilkan Preorder Level Boss")
        print("5. Tampilkan Postorder Level Boss")
        print("6. Level Boss Terendah")
        print("7. Level Boss Tertinggi")
        print("8. Jumlah Boss")
        print("9. Total Level Boss")
        print("10. Keluar")

        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            try:
                level = int(input("Masukkan level boss: "))
                boss_level.insert(level)
                print(f"Level boss {level} berhasil dimasukkan")
            except ValueError:
                print("Input tidak valid!")

        elif pilih == 2:
            try:
                level = int(input("Cari level boss: "))
                if boss_level.search(level):
                    print(f"Boss dengan level {level} ditemukan")
                else:
                    print(f"Boss dengan level {level} tidak ditemukan")
            except ValueError:
                print("Input tidak valid!")

        elif pilih == 3:
            print("Level boss terurut: ", end="")
            boss_level.inorder(boss_level.root)
            print()

        elif pilih == 4:
            print("Preorder level boss: ", end="")
            boss_level.preorder(boss_level.root)
            print()

        elif pilih == 5:
            print("Postorder level boss: ", end="")
            boss_level.postorder(boss_level.root)
            print()

        elif pilih == 6:
            print(f"Level boss terendah: {boss_level.find_min(boss_level.root)}")

        elif pilih == 7:
            print(f"Level boss tertinggi: {boss_level.find_max(boss_level.root)}")

        elif pilih == 8:
            print(f"Jumlah boss yang tersimpan: {boss_level.count_nodes(boss_level.root)}")

        elif pilih == 9:
            print(f"Total seluruh level boss: {boss_level.sum_nodes(boss_level.root)}")

        elif pilih == 10:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()