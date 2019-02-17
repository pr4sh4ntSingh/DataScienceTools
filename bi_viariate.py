    import seaborn as sns
    import numpy as np
    from pylab import figure, axes, pie, title
    import numpy as np
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    from scipy import stats

    import random
    from bokeh.core.properties import value
    from pylab import show

    from bokeh.io import show, output_file,output_notebook
    from bokeh.io import show as bokeh_show
    from bokeh.plotting import figure


    class bivariate:
        def __init__(self,df):
            self.df=df

        def correlation_matrix(self):
            corr = self.df.corr()
            # plot the heatmap
            cols=corr.columns.values
            print(cols)
            show(sns.heatmap(corr,
                    annot=True,
                    xticklabels=cols,
                    yticklabels=cols))


        def calc_iv(self,feature, target, pr=False):
            """
            Set pr=True to enable printing of output.
            Output:
              * iv: float,
              * data: pandas.DataFrame
            """

            lst = []
            df=self.df
            df[feature] = df[feature].fillna("NULL")

            for i in range(df[feature].nunique()):
                val = list(df[feature].unique())[i]
                lst.append([feature,                                                        # Variable
                            val,                                                            # Value
                            df[df[feature] == val].count()[feature],                        # All
                            df[(df[feature] == val) & (df[target] == 0)].count()[feature],  # Good (think: Fraud == 0)
                            df[(df[feature] == val) & (df[target] == 1)].count()[feature]]) # Bad (think: Fraud == 1)

            data = pd.DataFrame(lst, columns=['Variable', 'Value', 'All', 'Good', 'Bad'])

            data['Share'] = data['All'] / data['All'].sum()
            data['Bad Rate'] = data['Bad'] / data['All']
            data['Distribution Good'] = (data['All'] - data['Bad']) / (data['All'].sum() - data['Bad'].sum())
            data['Distribution Bad'] = data['Bad'] / data['Bad'].sum()
            data['WoE'] = np.log(data['Distribution Good'] / data['Distribution Bad'])

            data = data.replace({'WoE': {np.inf: 0, -np.inf: 0}})

            data['IV'] = data['WoE'] * (data['Distribution Good'] - data['Distribution Bad'])

            data = data.sort_values(by=['Variable', 'Value'], ascending=[True, True])
            data.index = range(len(data.index))

            if pr:
                print(data)
                print('IV = ', data['IV'].sum())


            iv = data['IV'].sum()
            # print(iv)

            return iv, data


        def calculate_iv(self,target,col_names='ALL',print_woi=False):
            """
            set sample_fraction= f to take f fraction of dataset

            If no of rows of very high. It might be good idea to take sampling.
            Set col_names for columns to calculate iv. Default All columns
            set print_woi = True to print woi for each class

            This is ideal for Categorical variable.
            For continuous variable you might need to do binning.

            Information Value	 Variable Predictiveness
            Less than 0.02  	 Not useful for prediction
            0.02 to 0.1	         Weak predictive Power
            0.1 to 0.3	         Medium predictive Power
            0.3 to 0.5	         Strong predictive Power
            >0.5	             Suspicious Predictive Power

            """

            ls=[]
            if col_names=='ALL':
                for col in self.df.columns.values:
                    iv,data=self.calc_iv(col,target=target)
                    ls.append(iv)
                    if(print_woi):
                        print(col)
                        print(data)
                        print(iv)
                iv_series=pd.Series(data=ls,index=self.df.columns.values)
            else:
                for col in col_names:
                    iv,data=self.calc_iv(col,target=target)
                    ls.append(iv)
                    if(print_woi):
                        print(col)
                        print(data)
                        print(iv)
                iv_series=pd.Series(data=ls,index=col_names)

            ax=iv_series.sort_values(ascending=False).plot(kind='bar', yticks=[0.02,0.1,0.3,0.5])
            for p in ax.patches:
                h="{0:.2f}".format(p.get_height() * 1.005)
                ax.annotate(h, (p.get_x() * 1.005, h))
            show(ax)


        def pair_plot(self):
            """
            just for representation.
            https://seaborn.pydata.org/tutorial/distributions.html
            """
            sns.pairplot(self.df);


        def bar_graph_with_color(self,col_name, stacked_col):
            """
            displays histogram of given variable. and show distribution of Categorical variable
            this is best for Categorical-Categorical  bivariate analysis

            Parameters
            ----------
            col_name : String
                       column which is going to be on x-axis

            stacked_col: String
                        column which is going to be displayed in colored bars
            """
            output_file(r"D:\p.html")

            stacks_original = self.df[col_name].unique().tolist()
            bars_original = self.df[stacked_col].unique().tolist()
            print(stacks_original)
            stacks=[str(s)+"_"  for s in stacks_original]
            bars=[str(s)+"_"  for s in bars_original]

            print(bars_original)
            colors = self.random_color(len(bars))

            data_source = {k:[] for k in bars }

            print(data_source)

            for bar_o,bar_str in zip(bars_original,bars):
                for stack in stacks_original:
                    data_source[bar_str].append(len(self.df.loc[(self.df[col_name]==stack)& (self.df[stacked_col]==bar_o) ,stacked_col]))


            data_source['stacks_v']=stacks
            #print(data_source)

            p = figure(x_range=stacks, plot_height=550, title=col_name+" Counts by"+ stacked_col,
                       toolbar_location="right", tools="pan,wheel_zoom,box_zoom,reset")

            print([value(str(x)+"_") for x in bars])
            p.vbar_stack(bars, x='stacks_v', width=0.9, color=colors, source=data_source,
                         legend=[value(str(x)+"_") for x in bars])


            p.y_range.start = 0
            p.x_range.range_padding = 0.1
            p.xgrid.grid_line_color = None
            p.axis.minor_tick_line_color = None
            p.outline_line_color = None
            p.legend.location = "top_right"
            p.legend.orientation = "horizontal"

            bokeh_show(p)




        def random_color(self,number_of_colors):
            """
            returns n random colors
            """
            color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)]) for i in range(number_of_colors)]
            return color;





    bi=bivariate(data)
    #bi.correlation_matrix()
    #bi.calculate_iv("Survived",cols)
    #bi.pair_plot()
    bi.bar_graph_with_color('Sex','Pclass')
