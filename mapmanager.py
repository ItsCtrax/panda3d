class Mapmanager:
    """ Управління карткою """
    def __init__(self):
        self.models = {
            0: 'dirt.png',  # dirt
            1: 'grass.png',  # grass
            2: 'sand.png',  # sand
            3: 'stone.png',  # stone
            4: 'snow.png',
            5: 'water.png',
            6: 'oak.png',
            7: 'leaves.png'
        }
        self.colors = {
            'dirt.png': (0.5, 0.3, 0.1, 1),  # Колір для dirt
            'grass.png': (0.1, 0.8, 0.1, 1),  # Колір для grass
            'sand.png': (1.0, 0.9, 0.6, 1),  # Колір для sand
            'stone.png': (0.7, 0.7, 0.7, 1),  # Колір для stone
            'snow.png': (1.0, 1.0, 1.0, 1),
            'water.png': (0, 0.2, 1., 1),
            'oak.png': (1.0, 0.9, 0.9, 1),
            'leaves.png': (0.1, 0.8, 0.1, 1)
        }

        # створюємо основний вузол картки:
        self.startNew()

    def startNew(self):
        """створює основу для нової картки"""
        self.land = render.attachNewNode("Land")  # вузол, до якого прив'язані всі блоки картки

    def getColor(self, block_type):
        """Повертає колір залежно від текстури блоку"""
        texture = self.models[block_type]
        return self.colors.get(texture, (1, 1, 1, 1))  # Якщо текстури нема в словнику, використовуємо білий

    def addBlock(self, position, block_type):
        """Додає блок на картку з вказаним типом і позицією"""
        # Якщо block_type == -1, не додаємо блок
        if block_type == -1:
            return

        self.block = loader.loadModel('block')
        texture = self.models[block_type]
        self.block.setTexture(loader.loadTexture(texture))
        self.block.setPos(position)
        self.block.setColor(self.getColor(block_type))  # Змінюємо колір за текстурою
        self.block.reparentTo(self.land)

    def loadLayer(self, layer_num):
        """Завантажує конкретний шар карти з файлу"""
        file_name = f"layers{layer_num}.txt"
        with open(file_name, 'r') as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(' ')
                for z in line:
                    z = int(z)  # Перетворюємо цифри на числа для типу текстури
                    # Додаємо блок лише якщо z != -1
                    if z != -1:
                        self.addBlock((x, y, layer_num), z)  # Задаємо текстуру та позицію
                    x += 1
                y += 1

    def loadLand(self, num_layers):
        """Завантажує всю карту, яка складається з кількох шарів"""
        for layer in range(num_layers):
            self.loadLayer(layer)

    def clear(self):
        """Очищає картку"""
        self.land.removeNode()
        self.startNew()
