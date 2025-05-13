'''
[编程实现]
写程序实现一个购物车，主要功能有： 
1、查看商品 
2、加入商品 
3、删除商品 
4、修改商品 
[输入格式]
无 
[输出格式]
无 
[样例输入]
无 
[样例输出]
无 
'''
class ShoppingCart:
    def __init__(self):
        self.products = {
            1001: {'name': 'iPhone 15', 'price': 7999, 'stock': 50},
            1002: {'name': 'MacBook Pro', 'price': 12999, 'stock': 30},
            1003: {'name': 'AirPods Pro', 'price': 1499, 'stock': 100}
        }
        self.cart = {}

    def show_products(self):
        print("\n=== 商品列表 ===")
        for pid, info in self.products.items():
            print(f"ID: {pid} | 名称: {info['name']} | 价格: ￥{info['price']} | 库存: {info['stock']}")

    def show_cart(self):
        print("\n=== 购物车 ===")
        if not self.cart:
            print("购物车为空")
            return
        
        total = 0
        for pid, quantity in self.cart.items():
            product = self.products[pid]
            subtotal = product['price'] * quantity
            print(f"ID: {pid} | 名称: {product['name']} | 单价: ￥{product['price']} | 数量: {quantity} | 小计: ￥{subtotal}")
            total += subtotal
        print(f"总计: ￥{total}")

    def add_product(self):
        self.show_products()
        try:
            pid = int(input("请输入要添加的商品ID: "))
            if pid not in self.products:
                print("商品不存在!")
                return
            
            quantity = int(input("请输入数量: "))
            if quantity <= 0:
                print("数量必须大于0!")
                return
            
            if self.products[pid]['stock'] < quantity:
                print(f"库存不足! 当前库存: {self.products[pid]['stock']}")
                return
            
            self.cart[pid] = self.cart.get(pid, 0) + quantity
            self.products[pid]['stock'] -= quantity
            print(f"已添加 {self.products[pid]['name']} x{quantity}")
        except ValueError:
            print("请输入有效的数字!")

    def remove_product(self):
        if not self.cart:
            print("购物车为空!")
            return
        
        self.show_cart()
        try:
            pid = int(input("请输入要删除的商品ID: "))
            if pid not in self.cart:
                print("购物车中没有此商品!")
                return
            
            quantity = int(input(f"当前数量: {self.cart[pid]}\n请输入要删除的数量: "))
            if quantity <= 0:
                print("数量必须大于0!")
                return
            
            if quantity > self.cart[pid]:
                print("删除数量不能超过购物车中的数量!")
                return
            
            self.cart[pid] -= quantity
            self.products[pid]['stock'] += quantity
            if self.cart[pid] == 0:
                del self.cart[pid]
            print("删除成功!")
        except ValueError:
            print("请输入有效的数字!")

    def modify_product(self):
        if not self.cart:
            print("购物车为空!")
            return
        
        self.show_cart()
        try:
            pid = int(input("请输入要修改的商品ID: "))
            if pid not in self.cart:
                print("购物车中没有此商品!")
                return
            
            new_quantity = int(input("请输入新的数量: "))
            if new_quantity <= 0:
                print("数量必须大于0!")
                return
            
            stock_change = new_quantity - self.cart[pid]
            if self.products[pid]['stock'] < stock_change:
                print(f"库存不足! 当前库存: {self.products[pid]['stock']}")
                return
            
            self.cart[pid] = new_quantity
            self.products[pid]['stock'] -= stock_change
            print("修改成功!")
        except ValueError:
            print("请输入有效的数字!")

    def run(self):
        while True:
            print("\n=== 购物车系统 ===")
            print("1. 查看商品列表")
            print("2. 查看购物车")
            print("3. 添加商品")
            print("4. 删除商品")
            print("5. 修改商品数量")
            print("0. 退出系统")
            
            choice = input("请选择操作: ")
            
            if choice == '1':
                self.show_products()
            elif choice == '2':
                self.show_cart()
            elif choice == '3':
                self.add_product()
            elif choice == '4':
                self.remove_product()
            elif choice == '5':
                self.modify_product()
            elif choice == '0':
                print("感谢使用购物车系统!")
                break
            else:
                print("无效的选择，请重新输入!")

# 启动购物车系统
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.run()
