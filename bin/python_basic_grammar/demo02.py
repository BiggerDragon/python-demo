import time


class Tool:
    """
    Marketing tool. 
    """
    tool_attrs_keys = ['tool_no', 'tool_name', 'tool_type',
                        'tool_desc', 'tool_status','create_date']
    def __init__(self, **kwargs):
        self.tool_attrs = {}
        for key in self.tool_attrs_keys:
            self.tool_attrs[key] = kwargs[key]
    
    def print_attrs(self):
        print(self.tool_attrs)
    
    def print_tool_type(self):
        raise NotImplementedError

class ScoreTool(Tool):
    """
    Score tool is sub class of Tool
    """
    score_tool_attrs = ["total_score", "max_score", "min_score"]
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for key in self.score_tool_attrs:
            self.tool_attrs[key] = kwargs[key]
    
    def print_attrs(self):
        print("Invoking of sub class print_attrs()...")
        super().print_attrs()
    
    def print_tool_type(self):
        print("This tool's type is ", self.tool_attrs.get("tool_type"))


t_attrs = {
    'tool_no':'123456789', 'tool_name':'积分', 'tool_type':'S',
    'tool_desc':'积分描述', 'tool_status':'P','create_date':time.time(),
    "total_score":'1000', "max_score":'50', "min_score":'20'
}
score_tool1 = ScoreTool(**t_attrs)

print(score_tool1)
print(score_tool1.__getattribute__("tool_attrs"))

print('score_tool1 is the type of Tool', type(score_tool1) is Tool)
print('score_tool1 is the instance of Tool', isinstance(score_tool1, Tool))

score_tool1.print_attrs()

score_tool1.print_tool_type()
