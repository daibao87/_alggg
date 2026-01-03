import math

class Value:
    def __init__(self, data, _children=(), _op='', label=''):
        """
        data: 數值本身
        grad: 梯度 (導數)，初始化為 0
        _prev: 前一個節點 (用於建立計算圖)
        _op: 產生此數值的運算符號 (如 +, *)，用於除錯
        """
        self.data = data
        self.grad = 0.0
        self._backward = lambda: None  
        self._prev = set(_children)
        self._op = _op
        self.label = label

    def __repr__(self):
        return f"Value(data={self.data}, grad={self.grad})"

    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        
        out = Value(self.data + other.data, (self, other), '+')

        def _backward():
            self.grad += 1.0 * out.grad
            other.grad += 1.0 * out.grad
        
        out._backward = _backward
        return out

    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)

        out = Value(self.data * other.data, (self, other), '*')

        def _backward():
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad
            
        out._backward = _backward
        return out

    def __pow__(self, other):
        assert isinstance(other, (int, float)), "次方必須是 int 或 float"
        
        out = Value(self.data**other, (self,), f'**{other}')

        def _backward():
            self.grad += (other * self.data**(other - 1)) * out.grad
            
        out._backward = _backward
        return out

    def tanh(self):

        x = self.data
        t = (math.exp(2*x) - 1) / (math.exp(2*x) + 1)
        out = Value(t, (self,), 'tanh')

        def _backward():

            self.grad += (1 - t**2) * out.grad
            
        out._backward = _backward
        return out

    def backward(self):
        """
        自動反向傳播核心函數
        """

        topo = []
        visited = set()
        def build_topo(v):
            if v not in visited:
                visited.add(v)
                for child in v._prev:
                    build_topo(child)
                topo.append(v)
        
        build_topo(self)


        self.grad = 1.0


        for node in reversed(topo):
            node._backward()


    def __radd__(self, other): 
        return self + other
    def __rmul__(self, other): 
        return self * other

a = Value(2.0, label='a')
b = Value(-3.0, label='b')
c = Value(10.0, label='c')

e = a * b; e.label = 'e'
d = e + c; d.label = 'd'
L = d.tanh(); L.label = 'L' 

L.backward()

print(f"輸入值: a={a.data}, b={b.data}, c={c.data}")
print(f"中間值: e={e.data} (a*b)")
print(f"中間值: d={d.data} (e+c)")
print(f"最終輸出 L: {L.data}")
print("-" * 20)
print("梯度計算結果 (dL/dx):")
print(f"dL/dL = {L.grad}")
print(f"dL/dd = {d.grad}")
print(f"dL/de = {e.grad}")
print(f"dL/dc = {c.grad}")
print(f"dL/da = {a.grad}")
print(f"dL/db = {b.grad}")
