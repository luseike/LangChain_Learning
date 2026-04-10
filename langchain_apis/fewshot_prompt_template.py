from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate

from models import ds


examples = [
    {"sinput": "2+2", "soutput": "4", "sdescription": "加法运算"},
    {"sinput": "5-2", "soutput": "3", "sdescription": "减法运算"},
]

examples_prompt_tmplt_txt = "算式： {sinput} 值： {soutput} 类型： {sdescription} "

prompt_sample = PromptTemplate.from_template(examples_prompt_tmplt_txt)

prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=prompt_sample,
    prefix="你是一个数学专家, 能够准确说出算式的类型，",
    suffix="现在给你算式: {input} ， 值: {output} ，告诉我类型：",
    input_variables=["input", "output"]
)

response = ds.invoke(prompt.format(input="3*3", output="9"))
print(response.content)