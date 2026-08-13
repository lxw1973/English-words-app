"""初始化词库数据"""
from sqlalchemy.orm import Session
from app.models import Word, DifficultyLevel
from app.database import SessionLocal

SEED_WORDS = {
    DifficultyLevel.CET4: [
        {
            "word": "abandon",
            "phonetic": "/əˈbændən/",
            "meaning": "遗弃，放弃",
            "definition": "to leave someone or something with no intention of returning",
            "example": "He abandoned his family and never returned.",
            "example_cn": "他遗弃了他的家庭，再也没有回来。",
            "pos": "verb"
        },
        {
            "word": "ability",
            "phonetic": "/əˈbɪləti/",
            "meaning": "能力",
            "definition": "power or skill to do something",
            "example": "She has the ability to solve complex problems.",
            "example_cn": "她有解决复杂问题的能力。",
            "pos": "noun"
        },
        {
            "word": "absorb",
            "phonetic": "/əbˈzɔːrb/",
            "meaning": "吸收；使专心",
            "definition": "to take in or soak up a liquid, gas or information",
            "example": "Plants absorb water through their roots.",
            "example_cn": "植物通过根部吸收水分。",
            "pos": "verb"
        },
        {
            "word": "academic",
            "phonetic": "/ˌækəˈdemɪk/",
            "meaning": "学术的；学院的",
            "definition": "relating to education, schools and studying",
            "example": "She achieved great academic success at university.",
            "example_cn": "她在大学取得了优异的学业成绩。",
            "pos": "adj"
        },
        {
            "word": "access",
            "phonetic": "/ˈækses/",
            "meaning": "进入；使用权",
            "definition": "the right or opportunity to use something or enter a place",
            "example": "Students have free access to the library.",
            "example_cn": "学生可以免费使用图书馆。",
            "pos": "noun"
        },
        {
            "word": "accompany",
            "phonetic": "/əˈkʌmpəni/",
            "meaning": "陪伴；伴随",
            "definition": "to go somewhere with someone",
            "example": "I will accompany you to the airport.",
            "example_cn": "我会陪你去机场。",
            "pos": "verb"
        },
        {
            "word": "accomplish",
            "phonetic": "/əˈkɑːmplɪʃ/",
            "meaning": "完成，实现",
            "definition": "to succeed in doing or completing something",
            "example": "We accomplished the task ahead of schedule.",
            "example_cn": "我们提前完成了任务。",
            "pos": "verb"
        },
        {
            "word": "accurate",
            "phonetic": "/ˈækjərət/",
            "meaning": "准确的，精确的",
            "definition": "correct and free from error",
            "example": "The report gives an accurate description of the accident.",
            "example_cn": "这份报告准确描述了事故的情况。",
            "pos": "adj"
        },
        {
            "word": "achieve",
            "phonetic": "/əˈtʃiːv/",
            "meaning": "实现，达到",
            "definition": "to successfully complete something or get a good result",
            "example": "She worked hard to achieve her goals.",
            "example_cn": "她努力工作以实现自己的目标。",
            "pos": "verb"
        },
        {
            "word": "acquire",
            "phonetic": "/əˈkwaɪər/",
            "meaning": "获得，习得",
            "definition": "to get or gain something, such as knowledge or skills",
            "example": "Children acquire language quickly in a natural environment.",
            "example_cn": "儿童在自然环境中习得语言很快。",
            "pos": "verb"
        },
        {
            "word": "adapt",
            "phonetic": "/əˈdæpt/",
            "meaning": "适应；改编",
            "definition": "to change in order to deal with a new situation",
            "example": "It took him a while to adapt to the new environment.",
            "example_cn": "他花了一段时间才适应新环境。",
            "pos": "verb"
        },
        {
            "word": "adequate",
            "phonetic": "/ˈædɪkwət/",
            "meaning": "足够的，适当的",
            "definition": "enough in quantity or good enough in quality",
            "example": "Make sure you get adequate sleep before the exam.",
            "example_cn": "考试前一定要保证充足的睡眠。",
            "pos": "adj"
        },
    ],
    DifficultyLevel.CET6: [
        {
            "word": "aberration",
            "phonetic": "/ˌæbəˈreɪʃn/",
            "meaning": "偏差，异常",
            "definition": "a departure from what is normal, usual, or expected",
            "example": "His violent behavior was an aberration.",
            "example_cn": "他的暴力行为是一种反常表现。",
            "pos": "noun"
        },
        {
            "word": "abolish",
            "phonetic": "/əˈbɑːlɪʃ/",
            "meaning": "废除，废止",
            "definition": "to officially end a law, system or institution",
            "example": "The government decided to abolish the outdated tax.",
            "example_cn": "政府决定废除这项过时的税收。",
            "pos": "verb"
        },
        {
            "word": "abrupt",
            "phonetic": "/əˈbrʌpt/",
            "meaning": "突然的；生硬的",
            "definition": "sudden and unexpected, or rude and unfriendly",
            "example": "The meeting came to an abrupt end.",
            "example_cn": "会议突然结束了。",
            "pos": "adj"
        },
        {
            "word": "absurd",
            "phonetic": "/əbˈsɜːrd/",
            "meaning": "荒谬的，荒唐的",
            "definition": "completely unreasonable and silly",
            "example": "The idea that money brings happiness is absurd to some people.",
            "example_cn": "金钱带来幸福这一想法在有些人看来是荒谬的。",
            "pos": "adj"
        },
        {
            "word": "abundant",
            "phonetic": "/əˈbʌndənt/",
            "meaning": "丰富的，充裕的",
            "definition": "existing in large quantities; more than enough",
            "example": "The region has abundant natural resources.",
            "example_cn": "该地区拥有丰富的自然资源。",
            "pos": "adj"
        },
        {
            "word": "accelerate",
            "phonetic": "/əkˈseləreɪt/",
            "meaning": "加速，促进",
            "definition": "to happen or make something happen faster",
            "example": "Economic reforms accelerated the growth of the industry.",
            "example_cn": "经济改革加速了该行业的发展。",
            "pos": "verb"
        },
        {
            "word": "accommodate",
            "phonetic": "/əˈkɑːmədeɪt/",
            "meaning": "容纳；为…提供住宿；适应",
            "definition": "to provide space or lodging for someone, or to adapt to something",
            "example": "The hotel can accommodate up to 500 guests.",
            "example_cn": "这家酒店最多可容纳500位客人。",
            "pos": "verb"
        },
        {
            "word": "accumulate",
            "phonetic": "/əˈkjuːmjəleɪt/",
            "meaning": "积累，积聚",
            "definition": "to gradually collect an increasing amount of something",
            "example": "Over the years he accumulated a large fortune.",
            "example_cn": "多年来他积累了大量财富。",
            "pos": "verb"
        },
        {
            "word": "acknowledge",
            "phonetic": "/əkˈnɑːlɪdʒ/",
            "meaning": "承认；致谢",
            "definition": "to accept or admit that something is true or exists",
            "example": "He acknowledged that he had made a mistake.",
            "example_cn": "他承认自己犯了一个错误。",
            "pos": "verb"
        },
        {
            "word": "acute",
            "phonetic": "/əˈkjuːt/",
            "meaning": "敏锐的；严重的；急性的",
            "definition": "very serious or severe; quick to notice things",
            "example": "There is an acute shortage of clean water in the area.",
            "example_cn": "该地区严重缺乏清洁水源。",
            "pos": "adj"
        },
        {
            "word": "adhere",
            "phonetic": "/ədˈhɪr/",
            "meaning": "遵守；坚持；粘附",
            "definition": "to stick firmly to something or follow a rule strictly",
            "example": "All employees must adhere to the safety regulations.",
            "example_cn": "所有员工都必须遵守安全规定。",
            "pos": "verb"
        },
        {
            "word": "aggravate",
            "phonetic": "/ˈæɡrəveɪt/",
            "meaning": "加重，恶化；激怒",
            "definition": "to make a situation worse or more serious",
            "example": "Stress can aggravate health problems.",
            "example_cn": "压力会加重健康问题。",
            "pos": "verb"
        },
    ],
    DifficultyLevel.BEC: [
        {
            "word": "revenue",
            "phonetic": "/ˈrevənuː/",
            "meaning": "收入，收益",
            "definition": "the money that a company or government receives regularly",
            "example": "The company's annual revenue exceeded one billion dollars.",
            "example_cn": "该公司的年收入超过了十亿美元。",
            "pos": "noun"
        },
        {
            "word": "negotiate",
            "phonetic": "/nɪˈɡoʊʃieɪt/",
            "meaning": "谈判，协商",
            "definition": "to discuss something formally in order to reach an agreement",
            "example": "The two companies are negotiating a new contract.",
            "example_cn": "两家公司正在就新合同进行谈判。",
            "pos": "verb"
        },
        {
            "word": "invoice",
            "phonetic": "/ˈɪnvɔɪs/",
            "meaning": "发票，账单",
            "definition": "a document listing goods or services provided and the amount due",
            "example": "Please send the invoice to the finance department.",
            "example_cn": "请把发票发给财务部门。",
            "pos": "noun"
        },
        {
            "word": "procurement",
            "phonetic": "/prəˈkjʊrmənt/",
            "meaning": "采购",
            "definition": "the process of buying supplies or services for a company",
            "example": "The procurement team is responsible for sourcing raw materials.",
            "example_cn": "采购团队负责寻找原材料供应商。",
            "pos": "noun"
        },
        {
            "word": "stakeholder",
            "phonetic": "/ˈsteɪkhoʊldər/",
            "meaning": "利益相关者",
            "definition": "a person or group with an interest in the success of a business",
            "example": "The proposal was discussed with all key stakeholders.",
            "example_cn": "该提案与所有关键利益相关者进行了讨论。",
            "pos": "noun"
        },
        {
            "word": "turnover",
            "phonetic": "/ˈtɜːrnoʊvər/",
            "meaning": "营业额；人员流动率",
            "definition": "the total amount of money a business earns; the rate at which staff leave",
            "example": "The store has a turnover of five million yuan a year.",
            "example_cn": "这家商店的年营业额为五百万元。",
            "pos": "noun"
        },
        {
            "word": "liability",
            "phonetic": "/ˌlaɪəˈbɪləti/",
            "meaning": "负债；责任",
            "definition": "a debt or financial obligation; legal responsibility",
            "example": "The company had to write off its liabilities after bankruptcy.",
            "example_cn": "公司破产后不得不注销其债务。",
            "pos": "noun"
        },
        {
            "word": "asset",
            "phonetic": "/ˈæset/",
            "meaning": "资产；有价值的人或物",
            "definition": "something valuable owned by a company or person",
            "example": "Brand reputation is one of the company's most valuable assets.",
            "example_cn": "品牌声誉是公司最有价值的资产之一。",
            "pos": "noun"
        },
        {
            "word": "merger",
            "phonetic": "/ˈmɜːrdʒər/",
            "meaning": "合并，兼并",
            "definition": "the joining of two or more companies into one",
            "example": "The merger between the two banks created the largest lender in the region.",
            "example_cn": "两家银行的合并造就了该地区最大的贷款机构。",
            "pos": "noun"
        },
        {
            "word": "benchmark",
            "phonetic": "/ˈbentʃmɑːrk/",
            "meaning": "基准，标杆",
            "definition": "a standard by which things may be measured or judged",
            "example": "The new product set a benchmark for the whole industry.",
            "example_cn": "这款新产品为整个行业树立了标杆。",
            "pos": "noun"
        },
        {
            "word": "logistics",
            "phonetic": "/ləˈdʒɪstɪks/",
            "meaning": "物流，后勤",
            "definition": "the careful organization of transporting goods or people",
            "example": "Efficient logistics can significantly reduce distribution costs.",
            "example_cn": "高效的物流可以显著降低配送成本。",
            "pos": "noun"
        },
        {
            "word": "entrepreneur",
            "phonetic": "/ˌɑːntrəprəˈnɜːr/",
            "meaning": "企业家",
            "definition": "a person who starts and runs a business, taking on financial risks",
            "example": "The young entrepreneur founded three successful startups.",
            "example_cn": "这位年轻的企业家创办了三家成功的初创公司。",
            "pos": "noun"
        },
    ],
    DifficultyLevel.TOEFL: [
        {
            "word": "hypothesis",
            "phonetic": "/haɪˈpɑːθəsɪs/",
            "meaning": "假设，假说",
            "definition": "an idea that is suggested as a possible explanation for something",
            "example": "The experiment was designed to test the hypothesis.",
            "example_cn": "这个实验旨在验证该假设。",
            "pos": "noun"
        },
        {
            "word": "phenomenon",
            "phonetic": "/fəˈnɑːmɪnən/",
            "meaning": "现象",
            "definition": "a fact or event that can be observed and studied",
            "example": "Global warming is a worldwide phenomenon.",
            "example_cn": "全球变暖是一种世界性的现象。",
            "pos": "noun"
        },
        {
            "word": "inevitable",
            "phonetic": "/ɪnˈevɪtəbl/",
            "meaning": "不可避免的",
            "definition": "certain to happen and impossible to avoid",
            "example": "Technological change is inevitable in modern society.",
            "example_cn": "在现代社会，技术变革是不可避免的。",
            "pos": "adj"
        },
        {
            "word": "rigorous",
            "phonetic": "/ˈrɪɡərəs/",
            "meaning": "严格的，严谨的",
            "definition": "careful, thorough and exact",
            "example": "The findings are based on rigorous scientific research.",
            "example_cn": "这些发现基于严谨的科学研究。",
            "pos": "adj"
        },
        {
            "word": "sophisticated",
            "phonetic": "/səˈfɪstɪkeɪtɪd/",
            "meaning": "复杂的；老练的",
            "definition": "highly developed and complex; having refined knowledge",
            "example": "The laboratory uses sophisticated equipment for analysis.",
            "example_cn": "实验室使用精密复杂的设备进行分析。",
            "pos": "adj"
        },
        {
            "word": "crucial",
            "phonetic": "/ˈkruːʃl/",
            "meaning": "关键的，至关重要的",
            "definition": "extremely important because it affects the result of something",
            "example": "Early diagnosis is crucial for effective treatment.",
            "example_cn": "早期诊断对有效治疗至关重要。",
            "pos": "adj"
        },
        {
            "word": "diverse",
            "phonetic": "/daɪˈvɜːrs/",
            "meaning": "多样的，不同的",
            "definition": "including many different types of people or things",
            "example": "The city is home to a diverse population.",
            "example_cn": "这座城市居住着多元化的居民。",
            "pos": "adj"
        },
        {
            "word": "flourish",
            "phonetic": "/ˈflɜːrɪʃ/",
            "meaning": "繁荣，兴旺",
            "definition": "to grow or develop successfully and strongly",
            "example": "Small businesses flourished under the new economic policy.",
            "example_cn": "在新经济政策下，小企业蓬勃发展。",
            "pos": "verb"
        },
        {
            "word": "undermine",
            "phonetic": "/ˌʌndərˈmaɪn/",
            "meaning": "削弱，逐渐损害",
            "definition": "to gradually make something weaker or less effective",
            "example": "Constant criticism can undermine a person's confidence.",
            "example_cn": "不断的批评会削弱一个人的信心。",
            "pos": "verb"
        },
        {
            "word": "compensate",
            "phonetic": "/ˈkɑːmpenseɪt/",
            "meaning": "补偿，弥补",
            "definition": "to pay someone money or do something to make up for a loss",
            "example": "The airline compensated passengers for the long delay.",
            "example_cn": "航空公司为长时间的延误向乘客进行了赔偿。",
            "pos": "verb"
        },
        {
            "word": "vulnerable",
            "phonetic": "/ˈvʌlnərəbl/",
            "meaning": "脆弱的，易受伤害的",
            "definition": "weak and easily hurt physically or emotionally",
            "example": "Children are especially vulnerable to online risks.",
            "example_cn": "儿童尤其容易受到网络风险的影响。",
            "pos": "adj"
        },
        {
            "word": "aesthetic",
            "phonetic": "/esˈθetɪk/",
            "meaning": "美学的，审美的",
            "definition": "concerned with beauty and the appreciation of beauty",
            "example": "The building was designed for both function and aesthetic appeal.",
            "example_cn": "这座建筑的设计兼顾了功能性与美学魅力。",
            "pos": "adj"
        },
    ],
    DifficultyLevel.IELTS: [
        {
            "word": "sustainable",
            "phonetic": "/səˈsteɪnəbl/",
            "meaning": "可持续的",
            "definition": "able to continue over a long period without harming the environment",
            "example": "We need to develop sustainable energy sources.",
            "example_cn": "我们需要开发可持续的能源。",
            "pos": "adj"
        },
        {
            "word": "urbanization",
            "phonetic": "/ˌɜːrbənəˈzeɪʃn/",
            "meaning": "城市化",
            "definition": "the process by which more people move to and live in cities",
            "example": "Rapid urbanization has put pressure on public services.",
            "example_cn": "快速的城市化给公共服务带来了压力。",
            "pos": "noun"
        },
        {
            "word": "biodiversity",
            "phonetic": "/ˌbaɪoʊdaɪˈvɜːrsəti/",
            "meaning": "生物多样性",
            "definition": "the variety of plant and animal life in a particular habitat",
            "example": "Deforestation threatens biodiversity in tropical regions.",
            "example_cn": "森林砍伐威胁着热带地区的生物多样性。",
            "pos": "noun"
        },
        {
            "word": "deforestation",
            "phonetic": "/ˌdiːˌfɔːrɪˈsteɪʃn/",
            "meaning": "森林砍伐",
            "definition": "the cutting down of trees over a large area",
            "example": "Deforestation accelerates soil erosion and climate change.",
            "example_cn": "森林砍伐加剧了水土流失和气候变化。",
            "pos": "noun"
        },
        {
            "word": "migration",
            "phonetic": "/maɪˈɡreɪʃn/",
            "meaning": "移民；迁徙",
            "definition": "the movement of people or animals from one place to another",
            "example": "Many birds make a long migration every winter.",
            "example_cn": "每年冬天许多鸟类都要长途迁徙。",
            "pos": "noun"
        },
        {
            "word": "infrastructure",
            "phonetic": "/ˈɪnfrəstrʌktʃər/",
            "meaning": "基础设施",
            "definition": "the basic systems and services needed for a country or city to work",
            "example": "The government invested heavily in transport infrastructure.",
            "example_cn": "政府在交通基础设施上投入了大量资金。",
            "pos": "noun"
        },
        {
            "word": "globalization",
            "phonetic": "/ˌɡloʊbələˈzeɪʃn/",
            "meaning": "全球化",
            "definition": "the process by which businesses and cultures operate worldwide",
            "example": "Globalization has changed the way we trade and communicate.",
            "example_cn": "全球化改变了我们贸易和沟通的方式。",
            "pos": "noun"
        },
        {
            "word": "congestion",
            "phonetic": "/kənˈdʒestʃən/",
            "meaning": "拥堵，堵塞",
            "definition": "the state of being so crowded that movement is difficult",
            "example": "Traffic congestion is a major problem in big cities.",
            "example_cn": "交通拥堵是大城市的一个主要问题。",
            "pos": "noun"
        },
        {
            "word": "renewable",
            "phonetic": "/rɪˈnuːəbl/",
            "meaning": "可再生的",
            "definition": "able to be replaced naturally, such as solar or wind energy",
            "example": "Solar and wind power are renewable sources of energy.",
            "example_cn": "太阳能和风能是可再生的能源。",
            "pos": "adj"
        },
        {
            "word": "alleviate",
            "phonetic": "/əˈliːvieɪt/",
            "meaning": "减轻，缓解",
            "definition": "to make pain or a problem less severe",
            "example": "The new policy aims to alleviate poverty in rural areas.",
            "example_cn": "新政策旨在缓解农村地区的贫困。",
            "pos": "verb"
        },
        {
            "word": "disparity",
            "phonetic": "/dɪˈspærəti/",
            "meaning": "差距，不平等",
            "definition": "a great difference between two or more things",
            "example": "There is a widening disparity between the rich and the poor.",
            "example_cn": "贫富之间的差距正在扩大。",
            "pos": "noun"
        },
        {
            "word": "perception",
            "phonetic": "/pərˈsepʃn/",
            "meaning": "感知；看法",
            "definition": "the way in which something is understood or regarded",
            "example": "Public perception of the issue has changed dramatically.",
            "example_cn": "公众对这一问题的看法已发生巨大变化。",
            "pos": "noun"
        },
    ],
}


def seed_database():
    """初始化数据库"""
    db = SessionLocal()

    for level, words in SEED_WORDS.items():
        for word_data in words:
            existing = db.query(Word).filter(Word.word == word_data['word']).first()
            if not existing:
                word = Word(
                    **word_data,
                    difficulty=level
                )
                db.add(word)

    db.commit()
    print("✅ 数据库初始化完成！")


if __name__ == "__main__":
    seed_database()
