from prettytable import PrettyTable

class Tool:
    
    def numbertoletter(self, num):
        letters_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        letter = letters_list[num-1]
        return letter
    
    def table(self, field_n=None, row_n=None, **kwargs):
        if field_n is None:
            field_n = 2
        if row_n is None:
            row_n = 1
            
        tab = PrettyTable()
        field_names = []
        
        for i in range(1, field_n + 1):
            GGH=self.numbertoletter(i)
            field_names.append(kwargs.get(GGH, ''))
        
        tab.field_names = field_names
        
        for x in range(1, row_n + 1):
            row_values = []
            for z in range(1, field_n + 1):  # Adjusted the range to start from 0
                var_name = self.numbertoletter(z) + str(x)
                row_values.append(kwargs.get(var_name, ''))  # Accessing variable by name from kwargs
            tab.add_row(row_values)
            
        return tab
