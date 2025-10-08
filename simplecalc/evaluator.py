# simplecalc/evaluator.py
import ast
import operator
from decimal import Decimal, getcontext

class EvalError(Exception): pass

class Evaluator:
    operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Mod: operator.mod,
    }

    def eval(self, expr: str) -> Decimal:
        try:
            # expr는 Parser에서 안전성/치환을 마친 문자열
            tree = ast.parse(expr, mode='eval')
            return Decimal(str(self._eval_node(tree.body)))
        except Exception as e:
            raise EvalError(str(e))

    def _eval_node(self, node):
        if isinstance(node, ast.BinOp):
            left = self._eval_node(node.left)
            right = self._eval_node(node.right)
            op_func = self.operators.get(type(node.op))
            if op_func is None:
                raise EvalError(f"Unsupported operator: {type(node.op)}")
            return op_func(left, right)

        # Python 3.8+ 숫자 리터럴
        elif isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return Decimal(str(node.value))
            else:
                raise EvalError(f"Unsupported constant: {node.value!r}")

        # (이전 버전 호환) ast.Num
        elif hasattr(ast, "Num") and isinstance(node, ast.Num):
            return Decimal(str(node.n))

        # 단항 연산자: -x, +x
        elif isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            val = self._eval_node(node.operand)
            return +val if isinstance(node.op, ast.UAdd) else -val

        # 괄호/식 래퍼 (안 들어올 수도 있지만 안전망)
        elif isinstance(node, ast.Expression):
            return self._eval_node(node.body)

        else:
            raise EvalError(f"Unsupported node: {type(node)}")
