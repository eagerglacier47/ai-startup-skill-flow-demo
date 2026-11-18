from dataclasses import dataclass
from typing import Callable, Dict, List

@dataclass
class Step:
    key: str
    name: str
    goal: str
    run: Callable[[dict], dict]

def validate(ctx: dict) -> dict:
    return {'mvp': ctx['idea'], 'pain': '明确目标用户的核心痛点', 'status': 'validated'}

def business_plan(ctx: dict) -> dict:
    return {'bp': '{} 的商业模式画布草稿'.format(ctx['idea']), 'status': 'drafted'}

def policy(ctx: dict) -> dict:
    return {'policy': ['数据隐私', '内容合规', 'AI 使用声明'], 'status': 'checked'}

def pitch(ctx: dict) -> dict:
    return {'pitch': '用 AI 解决 {}，先服务 10 个种子用户'.format(ctx['mvp']), 'status': 'ready'}

def growth(ctx: dict) -> dict:
    return {'channels': ['社群', '内容', '伙伴'], 'status': 'planned'}

def pricing(ctx: dict) -> dict:
    return {'model': '订阅 + 按量', 'status': 'proposed'}

def register(ctx: dict) -> dict:
    return {'company': ctx.get('company', 'Demo AI Inc.'), 'status': 'registered'}

STEPS = [
    Step('validate', '验证', '找到真实痛点', validate),
    Step('bp', 'BP', '形成商业计划', business_plan),
    Step('policy', '政策', '检查合规风险', policy),
    Step('pitch', '路演', '准备融资叙事', pitch),
    Step('growth', '获客', '设计增长渠道', growth),
    Step('pricing', '定价', '制定收费模型', pricing),
    Step('register', '注册', '落地公司主体', register),
]

def run_skill(idea: str, company: str = 'Demo AI Inc.') -> Dict:
    ctx = {'idea': idea, 'company': company}
    log: List[Dict] = []
    for step in STEPS:
        result = step.run(ctx)
        ctx.update(result)
        log.append({'step': step.key, 'name': step.name, 'goal': step.goal, 'result': result})
    return {'idea': idea, 'steps': log, 'final_context': ctx}

if __name__ == '__main__':
    import json
    output = run_skill('为独立开发者自动生成商业计划书')
    print(json.dumps(output, ensure_ascii=False, indent=2))