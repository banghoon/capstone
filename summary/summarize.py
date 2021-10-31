# -*- coding: utf-8 -*-
import torch
from kobart import get_kobart_tokenizer
from transformers.models.bart import BartForConditionalGeneration
import warnings


warnings.simplefilter('ignore')


def load_model(path='./kobart_summary'):
    model = BartForConditionalGeneration.from_pretrained(path)
    return model


def get_summary(texts: list, path='./kobart_summary'):
    model = load_model(path)
    tokenizer = get_kobart_tokenizer()
    outputs = []
    for text_ in texts:
        text_ = text_.replace('\n', '')[:2000]
        input_ids = tokenizer.encode(text_)
        input_ids = torch.tensor(input_ids)
        input_ids = input_ids.unsqueeze(0)
        output = model.generate(input_ids, eos_token_id=1, max_length=512, num_beams=5)
        outputs.append(tokenizer.decode(output[0], skip_special_tokens=True))
    return outputs


if __name__ == '__main__':

    text = ['''
(서울=연합뉴스) 조성흠 기자 = 삼성전자[005930] 스마트폰 사업이 3분기 갤럭시Z폴드3와 갤럭시Z플립3 등 폴더블폰의 흥행으로 전 분기에 주춤했던 실적을 다시 끌어올렸다.

삼성전자는 스마트폰을 담당하는 IM(IT & Mobile Communications) 부문의 3분기 매출이 28조4천200억원, 영업이익이 3조3천600억원이었다고 28일 밝혔다.

지난해 같은 기간보다 매출(30조4천900억원)은 2조700억원, 영업이익(4조4천500억원)은 1조900억원 감소했다.

올해 2분기와 비교하면 매출(22조6천700억원)은 5조7천500억원, 영업이익(3조2천400억원)은 1천200억원 증가했다.

삼성전자는 "폴더블폰 신제품과 중저가 스마트폰 판매 확대, 갤럭시 생태계 제품군 성장으로 전 분기 대비 실적이 개선됐다"며 "네트워크는 국내 5G 이동통신망 증설에 지속적으로 대응하는 가운데 북미·일본 등 해외 사업을 확대했다"고 설명했다.

삼성전자는 기존 하반기 주력 라인업이던 갤럭시노트 시리즈를 올해는 출시하지 않고, 8월 갤럭시Z폴드3·플립3를 선보이며 폴더블폰 대세화에 주력했다.

전작보다 가격대를 40만원 가량 낮추고 기능과 디자인을 개선한 이들 제품은 국내에서 39일 만에 100만대가 팔리는 등 세계적인 반도체 공급난에도 불구하고 이전 갤럭시노트20와 갤럭시S21의 판매 기록을 뛰어넘었다.

글로벌 시장조사업체 카운터포인트리서치는 갤럭시Z폴드3·플립3의 글로벌 판매량이 출시 후 한 달간 200만대에 달한 것으로 추산했다.

삼성전자는 4분기 폴더블폰 등 프리미엄 제품 판매를 꾸준히 확대하는 가운데, 중저가 5G 스마트폰 판매 확대를 통해 기기 교체 수요에 적극 대응키로 했다. 또한 태블릿·웨어러블 제품군 판매를 확대해 견조한 수익성을 확보할 방침이다.

내년에는 대세로 떠오른 폴더블과 플래그십 제품 판매를 늘려 프리미엄 라인업을 강화할 계획을 세웠다.

중저가 5G 스마트폰 강화도 병행해 매출 성장과 수익성 제고를 추진하며, 태블릿과 웨어러블 사업을 육성하고 선행 기술 개발도 이어간다.

네트워크 분야에서는 해외 사업 성장을 지속하는 동시에 미래 성장을 위해 자체 5G칩으로 하드웨어를 강화하고 소프트웨어 기반의 가상화 솔루션도 강화하기로 했다.
''']
    res = get_summary(text)
    print(res)
