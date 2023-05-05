import numpy as np
import pandas as pd
from pylab import figure, axes, pie, title
import pylab
import math

class Description:
    """
    provides static information about dataframe
    column by column
    """
    def __init__(self,df):
        self.df=df
        self.dtype_values=self.__get_type_wise_columns()

    def show_meta(self):
        """
        show static information about dataframe.
        Dataframe should be initialized using constructer.
        """
        print("No of Rows "+str(len(self.df)))
        print("")
        print("No of Columns "+str(self.__no_of_columns()))
        print(self.df.head(3))
        print("")
        print("Column Types:")
        print(self.df.dtypes.value_counts())
        print("")
        # dtype-wise name of columns
        dtype_values=self.__get_type_wise_columns()
        self.__print_dict_of_list(dtype_values)



    def __get_type_wise_columns(self):
        """
        return column names grouped by type of columns.
        returns dictionary
        input : dataframe,
        output :
        {
        col_type1 : [col1,col2 ],
        col_type2 : [col3 ,col4 ]
        ....... :   ........
        }
        """
        dtype_values={str(k):[] for k in self.df.dtypes.values}
        for c in self.df.columns:
            dtype_values[str(self.df[c].dtype)].append(c)
        return dtype_values


    def __no_of_columns(self):
        return len(self.df.columns)


    def __print_dict_of_list(self,dictionary):
        """
        print key wise value of list of dictionary
        """
        for key,values in dictionary.items():
            print(key)
            s=""
            for k in dictionary[key]:
                s=s+k+" , "
            print("[ "+s+" ]")


    def __percentage(self,x, **kwargs):
        """
        calculate percentage of series.
        """
        total=kwargs['total']
        return x*100/total



    def top_values(self,n,col_name,chart='pie',float_chart='hist',show_values=True):
        """        displays top n values of a single dataframe column
                if column type is float it will display graph for whole data
                otherwise it will show top n values in graph.
        """
        if (self.df[col_name]).dtype=='float64':
            print("-------------------------------------------")
            p=self.df[col_name]
            functions = {'kde': p.plot.kde,
                         'bar':p.plot.bar,
                         'barh':p.plot.barh,
                         'box':p.plot.box,
                         'density':p.plot.density,
                         'hist':p.plot.hist,
                         'kde':p.plot.kde,
                         'line':p.plot.line,
                         'pie':p.plot.pie,
                        }
            count=len(self.df[col_name].unique())
            min=self.df[col_name].min()
            max=self.df[col_name].max()
            range=max-min
            bin_count=math.ceil(math.log(range,2))
            print(str(count)+" values found in range "+ str(min) +" to "+str(max))
            #if chart in functions:bins=bin_count
            #show(p.plot.kde())
            if float_chart in functions:
                pylab.show(functions[float_chart]())
        else:
            p=self.df[col_name].value_counts()
            total=sum(p)
            others=sum(p.values[n:])
            p=p.iloc[:n]
            p['_Others_'] =  others
            p_per=p.apply(self.__percentage,total=total)
            functions = {'kde': p.plot.kde,
                         'bar':p.plot.bar,
                         'barh':p.plot.barh,
                         'box':p.plot.box,
                         'density':p.plot.density,
                         'hist':p.plot.hist,
                         'kde':p.plot.kde,
                         'line':p.plot.line,
                         'pie':p.plot.pie,
                        }
            if chart in functions:
                pylab.show(functions[chart]())

            if show_values:
                if chart=='pie':
                    print(p_per)
                else:
                    print(p)


    def show_top_values(self,n,chart="pie",float_chart='hist',show_values=False):
        """
        displays top n values of each columns in dataframe with graph and percentage
        """
        type_dict=self.__get_type_wise_columns()
        for keys in type_dict.keys():
            print(str(keys))
            print("-----")
            for col_name in type_dict[keys]:
                print(col_name)
                if show_values:
                    self.top_values(n,col_name, chart=chart,float_chart=float_chart,show_values=True)
                else:
                    self.top_values(n,col_name, chart=chart,float_chart=float_chart,show_values=False)

    def describe_stats(self):
        type_wise_cols=self.__get_type_wise_columns()
        for key,value in type_wise_cols.items():
            print("-----------"+str(key)+"-------------")
            print(self.df.loc[:,value].describe())


    def show_grids_of_histogram(self,type,layout):
        """
            Parameters
            ----------
            type : String
                       type of column for which graph is being generated

            layout: touple
                        (row, column)
        """
        self.df[self.dtype_values[type]].hist(figsize=(14, 5), layout = layout);
