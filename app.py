"""
生产决策优化系统

运行步骤：
1. 安装依赖: pip install -r requirements.txt
2. 启动服务: python app.py
3. 访问地址: http://localhost:5001

系统功能：
- /sprt-test : SPRT抽样检测
- /single-optimization : 单级生产优化
- /multi-optimization : 多级协同优化
- /generate-sample : 生成随机样本
"""
from flask import Flask, jsonify, request
import random

app = Flask(__name__)


# 添加 CORS 支持
@app.after_request
def add_cors_headers(response):
    """添加跨域请求支持头信息"""
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    return response


@app.route('/')
def home():
    """首页路由，用于测试服务是否正常运行"""
    return "生产决策系统后端服务已启动！访问 /sprt-test 进行SPRT测试"


@app.route('/sprt-test', methods=['POST'])
def sprt_test():
    """SPRT测试路由"""
    try:
        # 获取前端发送的JSON数据
        data = request.json
        print("收到SPRT测试请求:", data)

        # 这里添加您的SPRT测试逻辑
        # 示例：随机生成测试结果
        result = {
            "status": "success",
            "test_result": random.choice(["通过", "失败"]),
            "confidence": round(random.uniform(0.85, 0.99), 4),
            "iterations": random.randint(5, 20)
        }

        return jsonify(result)

    except Exception as e:
        # 返回错误信息
        return jsonify({
            "status": "error",
            "message": f"SPRT测试失败: {str(e)}"
        }), 500


@app.route('/single-optimization', methods=['POST'])
def single_optimization():
    """单级优化生产路由"""
    try:
        data = request.json
        print("收到单级优化请求:", data)

        # 这里添加您的单级优化逻辑
        # 示例：返回优化结果
        result = {
            "status": "success",
            "optimized_parameters": {
                "production_rate": random.randint(50, 100),
                "quality_level": round(random.uniform(0.9, 0.99), 2),
                "cost_reduction": round(random.uniform(5.0, 15.0), 1)
            }
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"单级优化失败: {str(e)}"
        }), 500


@app.route('/multi-optimization', methods=['POST'])
def multi_optimization():
    """多级优化生产路由"""
    try:
        data = request.json
        print("收到多级优化请求:", data)

        # 这里添加您的多级优化逻辑
        # 示例：返回多级优化结果
        stages = []
        for i in range(1, random.randint(2, 5)):
            stages.append({
                "stage": i,
                "parameters": {
                    "input": random.randint(100, 200),
                    "output": random.randint(80, 190),
                    "efficiency": round(random.uniform(0.7, 0.95), 3)
                }
            })

        result = {
            "status": "success",
            "total_efficiency": round(random.uniform(0.65, 0.85), 3),
            "stages": stages
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"多级优化失败: {str(e)}"
        }), 500


@app.route('/generate-sample', methods=['GET'])
def generate_sample():
    """生成随机样本数据"""
    try:
        # 生成随机样本数据
        samples = []
        for i in range(10):
            samples.append({
                "id": i + 1,
                "value": round(random.gauss(50, 10), 2),
                "quality": random.choice(["A", "B", "C"])
            })

        return jsonify({
            "status": "success",
            "samples": samples
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"样本生成失败: {str(e)}"
        }), 500


if __name__ == '__main__':
    # 使用 5001 端口避免冲突
    app.run(host='0.0.0.0', port=5001, debug=True)
