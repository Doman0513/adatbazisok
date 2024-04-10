{
    "metadata": {
        "kernelspec": {
            "name": "SQL",
            "display_name": "SQL",
            "language": "sql"
        },
        "language_info": {
            "name": "sql",
            "version": ""
        }
    },
    "nbformat_minor": 2,
    "nbformat": 4,
    "cells": [
        {
            "cell_type": "code",
            "source": [
                "--Készítsen lekérdezést, amely megjeleníti, hogy szobánként (SZOBA_FK) hány olyan foglalás történt,\r\n",
                "-- ahol a felnőttek száma nagyobb volt a gyermekek számánál!\r\n",
                "\r\n",
                "--a. A lekérdezés jelenítse meg a végösszeget is megfelelően jelölve!\r\n",
                "\r\n",
                "SELECT count(*),\r\n",
                "        IIF(SZOBA_FK is null, 'végérték', cast(SZOBA_FK as nvarchar(20)))\r\n",
                "From foglalas\r\n",
                "where FELNOTT_SZAM>GYERMEK_SZAM\r\n",
                "group by rollup (SZOBA_FK)\r\n",
                ""
            ],
            "metadata": {
                "azdata_cell_guid": "45c82ebd-a6e8-4d30-acc1-9e875a5ccfb1",
                "language": "sql"
            },
            "outputs": [
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "(190 rows affected)"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "Total execution time: 00:00:00.010"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "execute_result",
                    "metadata": {},
                    "execution_count": 1,
                    "data": {
                        "application/vnd.dataresource+json": {
                            "schema": {
                                "fields": [
                                    {
                                        "name": "(No column name)"
                                    },
                                    {
                                        "name": "(No column name)"
                                    }
                                ]
                            },
                            "data": [
                                {
                                    "(No column name)": "1"
                                },
                                {
                                    "(No column name)": "2"
                                },
                                {
                                    "(No column name)": "3"
                                },
                                {
                                    "(No column name)": "4"
                                },
                                {
                                    "(No column name)": "5"
                                },
                                {
                                    "(No column name)": "6"
                                },
                                {
                                    "(No column name)": "7"
                                },
                                {
                                    "(No column name)": "8"
                                },
                                {
                                    "(No column name)": "9"
                                },
                                {
                                    "(No column name)": "10"
                                },
                                {
                                    "(No column name)": "11"
                                },
                                {
                                    "(No column name)": "12"
                                },
                                {
                                    "(No column name)": "13"
                                },
                                {
                                    "(No column name)": "14"
                                },
                                {
                                    "(No column name)": "15"
                                },
                                {
                                    "(No column name)": "16"
                                },
                                {
                                    "(No column name)": "17"
                                },
                                {
                                    "(No column name)": "18"
                                },
                                {
                                    "(No column name)": "19"
                                },
                                {
                                    "(No column name)": "20"
                                },
                                {
                                    "(No column name)": "21"
                                },
                                {
                                    "(No column name)": "22"
                                },
                                {
                                    "(No column name)": "23"
                                },
                                {
                                    "(No column name)": "24"
                                },
                                {
                                    "(No column name)": "25"
                                },
                                {
                                    "(No column name)": "27"
                                },
                                {
                                    "(No column name)": "28"
                                },
                                {
                                    "(No column name)": "29"
                                },
                                {
                                    "(No column name)": "30"
                                },
                                {
                                    "(No column name)": "31"
                                },
                                {
                                    "(No column name)": "32"
                                },
                                {
                                    "(No column name)": "33"
                                },
                                {
                                    "(No column name)": "34"
                                },
                                {
                                    "(No column name)": "35"
                                },
                                {
                                    "(No column name)": "36"
                                },
                                {
                                    "(No column name)": "37"
                                },
                                {
                                    "(No column name)": "38"
                                },
                                {
                                    "(No column name)": "39"
                                },
                                {
                                    "(No column name)": "40"
                                },
                                {
                                    "(No column name)": "41"
                                },
                                {
                                    "(No column name)": "42"
                                },
                                {
                                    "(No column name)": "43"
                                },
                                {
                                    "(No column name)": "44"
                                },
                                {
                                    "(No column name)": "45"
                                },
                                {
                                    "(No column name)": "46"
                                },
                                {
                                    "(No column name)": "47"
                                },
                                {
                                    "(No column name)": "48"
                                },
                                {
                                    "(No column name)": "49"
                                },
                                {
                                    "(No column name)": "50"
                                },
                                {
                                    "(No column name)": "51"
                                },
                                {
                                    "(No column name)": "52"
                                },
                                {
                                    "(No column name)": "54"
                                },
                                {
                                    "(No column name)": "55"
                                },
                                {
                                    "(No column name)": "56"
                                },
                                {
                                    "(No column name)": "57"
                                },
                                {
                                    "(No column name)": "58"
                                },
                                {
                                    "(No column name)": "59"
                                },
                                {
                                    "(No column name)": "60"
                                },
                                {
                                    "(No column name)": "61"
                                },
                                {
                                    "(No column name)": "62"
                                },
                                {
                                    "(No column name)": "63"
                                },
                                {
                                    "(No column name)": "64"
                                },
                                {
                                    "(No column name)": "66"
                                },
                                {
                                    "(No column name)": "67"
                                },
                                {
                                    "(No column name)": "69"
                                },
                                {
                                    "(No column name)": "70"
                                },
                                {
                                    "(No column name)": "71"
                                },
                                {
                                    "(No column name)": "72"
                                },
                                {
                                    "(No column name)": "73"
                                },
                                {
                                    "(No column name)": "74"
                                },
                                {
                                    "(No column name)": "75"
                                },
                                {
                                    "(No column name)": "76"
                                },
                                {
                                    "(No column name)": "77"
                                },
                                {
                                    "(No column name)": "78"
                                },
                                {
                                    "(No column name)": "79"
                                },
                                {
                                    "(No column name)": "80"
                                },
                                {
                                    "(No column name)": "81"
                                },
                                {
                                    "(No column name)": "82"
                                },
                                {
                                    "(No column name)": "83"
                                },
                                {
                                    "(No column name)": "84"
                                },
                                {
                                    "(No column name)": "85"
                                },
                                {
                                    "(No column name)": "86"
                                },
                                {
                                    "(No column name)": "87"
                                },
                                {
                                    "(No column name)": "88"
                                },
                                {
                                    "(No column name)": "89"
                                },
                                {
                                    "(No column name)": "90"
                                },
                                {
                                    "(No column name)": "91"
                                },
                                {
                                    "(No column name)": "92"
                                },
                                {
                                    "(No column name)": "93"
                                },
                                {
                                    "(No column name)": "94"
                                },
                                {
                                    "(No column name)": "95"
                                },
                                {
                                    "(No column name)": "96"
                                },
                                {
                                    "(No column name)": "97"
                                },
                                {
                                    "(No column name)": "98"
                                },
                                {
                                    "(No column name)": "99"
                                },
                                {
                                    "(No column name)": "100"
                                },
                                {
                                    "(No column name)": "101"
                                },
                                {
                                    "(No column name)": "102"
                                },
                                {
                                    "(No column name)": "103"
                                },
                                {
                                    "(No column name)": "104"
                                },
                                {
                                    "(No column name)": "106"
                                },
                                {
                                    "(No column name)": "107"
                                },
                                {
                                    "(No column name)": "108"
                                },
                                {
                                    "(No column name)": "109"
                                },
                                {
                                    "(No column name)": "110"
                                },
                                {
                                    "(No column name)": "111"
                                },
                                {
                                    "(No column name)": "112"
                                },
                                {
                                    "(No column name)": "113"
                                },
                                {
                                    "(No column name)": "114"
                                },
                                {
                                    "(No column name)": "115"
                                },
                                {
                                    "(No column name)": "117"
                                },
                                {
                                    "(No column name)": "118"
                                },
                                {
                                    "(No column name)": "119"
                                },
                                {
                                    "(No column name)": "120"
                                },
                                {
                                    "(No column name)": "121"
                                },
                                {
                                    "(No column name)": "122"
                                },
                                {
                                    "(No column name)": "123"
                                },
                                {
                                    "(No column name)": "124"
                                },
                                {
                                    "(No column name)": "126"
                                },
                                {
                                    "(No column name)": "127"
                                },
                                {
                                    "(No column name)": "129"
                                },
                                {
                                    "(No column name)": "130"
                                },
                                {
                                    "(No column name)": "131"
                                },
                                {
                                    "(No column name)": "132"
                                },
                                {
                                    "(No column name)": "133"
                                },
                                {
                                    "(No column name)": "134"
                                },
                                {
                                    "(No column name)": "135"
                                },
                                {
                                    "(No column name)": "136"
                                },
                                {
                                    "(No column name)": "137"
                                },
                                {
                                    "(No column name)": "138"
                                },
                                {
                                    "(No column name)": "139"
                                },
                                {
                                    "(No column name)": "140"
                                },
                                {
                                    "(No column name)": "141"
                                },
                                {
                                    "(No column name)": "142"
                                },
                                {
                                    "(No column name)": "143"
                                },
                                {
                                    "(No column name)": "144"
                                },
                                {
                                    "(No column name)": "145"
                                },
                                {
                                    "(No column name)": "146"
                                },
                                {
                                    "(No column name)": "147"
                                },
                                {
                                    "(No column name)": "148"
                                },
                                {
                                    "(No column name)": "149"
                                },
                                {
                                    "(No column name)": "150"
                                },
                                {
                                    "(No column name)": "151"
                                },
                                {
                                    "(No column name)": "152"
                                },
                                {
                                    "(No column name)": "153"
                                },
                                {
                                    "(No column name)": "154"
                                },
                                {
                                    "(No column name)": "155"
                                },
                                {
                                    "(No column name)": "156"
                                },
                                {
                                    "(No column name)": "157"
                                },
                                {
                                    "(No column name)": "158"
                                },
                                {
                                    "(No column name)": "160"
                                },
                                {
                                    "(No column name)": "161"
                                },
                                {
                                    "(No column name)": "162"
                                },
                                {
                                    "(No column name)": "163"
                                },
                                {
                                    "(No column name)": "164"
                                },
                                {
                                    "(No column name)": "165"
                                },
                                {
                                    "(No column name)": "166"
                                },
                                {
                                    "(No column name)": "167"
                                },
                                {
                                    "(No column name)": "168"
                                },
                                {
                                    "(No column name)": "169"
                                },
                                {
                                    "(No column name)": "170"
                                },
                                {
                                    "(No column name)": "171"
                                },
                                {
                                    "(No column name)": "172"
                                },
                                {
                                    "(No column name)": "173"
                                },
                                {
                                    "(No column name)": "174"
                                },
                                {
                                    "(No column name)": "175"
                                },
                                {
                                    "(No column name)": "176"
                                },
                                {
                                    "(No column name)": "177"
                                },
                                {
                                    "(No column name)": "178"
                                },
                                {
                                    "(No column name)": "179"
                                },
                                {
                                    "(No column name)": "180"
                                },
                                {
                                    "(No column name)": "181"
                                },
                                {
                                    "(No column name)": "182"
                                },
                                {
                                    "(No column name)": "183"
                                },
                                {
                                    "(No column name)": "184"
                                },
                                {
                                    "(No column name)": "185"
                                },
                                {
                                    "(No column name)": "186"
                                },
                                {
                                    "(No column name)": "187"
                                },
                                {
                                    "(No column name)": "188"
                                },
                                {
                                    "(No column name)": "189"
                                },
                                {
                                    "(No column name)": "190"
                                },
                                {
                                    "(No column name)": "191"
                                },
                                {
                                    "(No column name)": "192"
                                },
                                {
                                    "(No column name)": "193"
                                },
                                {
                                    "(No column name)": "194"
                                },
                                {
                                    "(No column name)": "195"
                                },
                                {
                                    "(No column name)": "196"
                                },
                                {
                                    "(No column name)": "197"
                                },
                                {
                                    "(No column name)": "198"
                                },
                                {
                                    "(No column name)": "végérték"
                                }
                            ]
                        },
                        "text/html": [
                            "<table>",
                            "<tr><th>(No column name)</th><th>(No column name)</th></tr>",
                            "<tr><td>7</td><td>1</td></tr>",
                            "<tr><td>2</td><td>2</td></tr>",
                            "<tr><td>3</td><td>3</td></tr>",
                            "<tr><td>5</td><td>4</td></tr>",
                            "<tr><td>2</td><td>5</td></tr>",
                            "<tr><td>5</td><td>6</td></tr>",
                            "<tr><td>6</td><td>7</td></tr>",
                            "<tr><td>5</td><td>8</td></tr>",
                            "<tr><td>4</td><td>9</td></tr>",
                            "<tr><td>4</td><td>10</td></tr>",
                            "<tr><td>4</td><td>11</td></tr>",
                            "<tr><td>7</td><td>12</td></tr>",
                            "<tr><td>4</td><td>13</td></tr>",
                            "<tr><td>3</td><td>14</td></tr>",
                            "<tr><td>4</td><td>15</td></tr>",
                            "<tr><td>1</td><td>16</td></tr>",
                            "<tr><td>2</td><td>17</td></tr>",
                            "<tr><td>3</td><td>18</td></tr>",
                            "<tr><td>4</td><td>19</td></tr>",
                            "<tr><td>5</td><td>20</td></tr>",
                            "<tr><td>1</td><td>21</td></tr>",
                            "<tr><td>2</td><td>22</td></tr>",
                            "<tr><td>3</td><td>23</td></tr>",
                            "<tr><td>3</td><td>24</td></tr>",
                            "<tr><td>1</td><td>25</td></tr>",
                            "<tr><td>5</td><td>27</td></tr>",
                            "<tr><td>5</td><td>28</td></tr>",
                            "<tr><td>3</td><td>29</td></tr>",
                            "<tr><td>2</td><td>30</td></tr>",
                            "<tr><td>1</td><td>31</td></tr>",
                            "<tr><td>1</td><td>32</td></tr>",
                            "<tr><td>3</td><td>33</td></tr>",
                            "<tr><td>3</td><td>34</td></tr>",
                            "<tr><td>6</td><td>35</td></tr>",
                            "<tr><td>4</td><td>36</td></tr>",
                            "<tr><td>2</td><td>37</td></tr>",
                            "<tr><td>5</td><td>38</td></tr>",
                            "<tr><td>4</td><td>39</td></tr>",
                            "<tr><td>3</td><td>40</td></tr>",
                            "<tr><td>1</td><td>41</td></tr>",
                            "<tr><td>5</td><td>42</td></tr>",
                            "<tr><td>4</td><td>43</td></tr>",
                            "<tr><td>6</td><td>44</td></tr>",
                            "<tr><td>4</td><td>45</td></tr>",
                            "<tr><td>3</td><td>46</td></tr>",
                            "<tr><td>2</td><td>47</td></tr>",
                            "<tr><td>6</td><td>48</td></tr>",
                            "<tr><td>5</td><td>49</td></tr>",
                            "<tr><td>3</td><td>50</td></tr>",
                            "<tr><td>3</td><td>51</td></tr>",
                            "<tr><td>5</td><td>52</td></tr>",
                            "<tr><td>4</td><td>54</td></tr>",
                            "<tr><td>3</td><td>55</td></tr>",
                            "<tr><td>1</td><td>56</td></tr>",
                            "<tr><td>3</td><td>57</td></tr>",
                            "<tr><td>8</td><td>58</td></tr>",
                            "<tr><td>4</td><td>59</td></tr>",
                            "<tr><td>1</td><td>60</td></tr>",
                            "<tr><td>4</td><td>61</td></tr>",
                            "<tr><td>3</td><td>62</td></tr>",
                            "<tr><td>3</td><td>63</td></tr>",
                            "<tr><td>5</td><td>64</td></tr>",
                            "<tr><td>3</td><td>66</td></tr>",
                            "<tr><td>2</td><td>67</td></tr>",
                            "<tr><td>2</td><td>69</td></tr>",
                            "<tr><td>8</td><td>70</td></tr>",
                            "<tr><td>2</td><td>71</td></tr>",
                            "<tr><td>2</td><td>72</td></tr>",
                            "<tr><td>4</td><td>73</td></tr>",
                            "<tr><td>8</td><td>74</td></tr>",
                            "<tr><td>2</td><td>75</td></tr>",
                            "<tr><td>2</td><td>76</td></tr>",
                            "<tr><td>3</td><td>77</td></tr>",
                            "<tr><td>3</td><td>78</td></tr>",
                            "<tr><td>4</td><td>79</td></tr>",
                            "<tr><td>5</td><td>80</td></tr>",
                            "<tr><td>3</td><td>81</td></tr>",
                            "<tr><td>5</td><td>82</td></tr>",
                            "<tr><td>5</td><td>83</td></tr>",
                            "<tr><td>3</td><td>84</td></tr>",
                            "<tr><td>2</td><td>85</td></tr>",
                            "<tr><td>4</td><td>86</td></tr>",
                            "<tr><td>5</td><td>87</td></tr>",
                            "<tr><td>5</td><td>88</td></tr>",
                            "<tr><td>8</td><td>89</td></tr>",
                            "<tr><td>3</td><td>90</td></tr>",
                            "<tr><td>2</td><td>91</td></tr>",
                            "<tr><td>5</td><td>92</td></tr>",
                            "<tr><td>3</td><td>93</td></tr>",
                            "<tr><td>6</td><td>94</td></tr>",
                            "<tr><td>3</td><td>95</td></tr>",
                            "<tr><td>6</td><td>96</td></tr>",
                            "<tr><td>5</td><td>97</td></tr>",
                            "<tr><td>4</td><td>98</td></tr>",
                            "<tr><td>4</td><td>99</td></tr>",
                            "<tr><td>2</td><td>100</td></tr>",
                            "<tr><td>1</td><td>101</td></tr>",
                            "<tr><td>1</td><td>102</td></tr>",
                            "<tr><td>1</td><td>103</td></tr>",
                            "<tr><td>3</td><td>104</td></tr>",
                            "<tr><td>4</td><td>106</td></tr>",
                            "<tr><td>4</td><td>107</td></tr>",
                            "<tr><td>1</td><td>108</td></tr>",
                            "<tr><td>2</td><td>109</td></tr>",
                            "<tr><td>5</td><td>110</td></tr>",
                            "<tr><td>1</td><td>111</td></tr>",
                            "<tr><td>4</td><td>112</td></tr>",
                            "<tr><td>2</td><td>113</td></tr>",
                            "<tr><td>1</td><td>114</td></tr>",
                            "<tr><td>5</td><td>115</td></tr>",
                            "<tr><td>4</td><td>117</td></tr>",
                            "<tr><td>2</td><td>118</td></tr>",
                            "<tr><td>4</td><td>119</td></tr>",
                            "<tr><td>2</td><td>120</td></tr>",
                            "<tr><td>5</td><td>121</td></tr>",
                            "<tr><td>3</td><td>122</td></tr>",
                            "<tr><td>5</td><td>123</td></tr>",
                            "<tr><td>4</td><td>124</td></tr>",
                            "<tr><td>4</td><td>126</td></tr>",
                            "<tr><td>5</td><td>127</td></tr>",
                            "<tr><td>3</td><td>129</td></tr>",
                            "<tr><td>5</td><td>130</td></tr>",
                            "<tr><td>4</td><td>131</td></tr>",
                            "<tr><td>4</td><td>132</td></tr>",
                            "<tr><td>4</td><td>133</td></tr>",
                            "<tr><td>4</td><td>134</td></tr>",
                            "<tr><td>3</td><td>135</td></tr>",
                            "<tr><td>2</td><td>136</td></tr>",
                            "<tr><td>2</td><td>137</td></tr>",
                            "<tr><td>5</td><td>138</td></tr>",
                            "<tr><td>6</td><td>139</td></tr>",
                            "<tr><td>5</td><td>140</td></tr>",
                            "<tr><td>4</td><td>141</td></tr>",
                            "<tr><td>1</td><td>142</td></tr>",
                            "<tr><td>5</td><td>143</td></tr>",
                            "<tr><td>2</td><td>144</td></tr>",
                            "<tr><td>2</td><td>145</td></tr>",
                            "<tr><td>3</td><td>146</td></tr>",
                            "<tr><td>1</td><td>147</td></tr>",
                            "<tr><td>5</td><td>148</td></tr>",
                            "<tr><td>5</td><td>149</td></tr>",
                            "<tr><td>6</td><td>150</td></tr>",
                            "<tr><td>2</td><td>151</td></tr>",
                            "<tr><td>3</td><td>152</td></tr>",
                            "<tr><td>4</td><td>153</td></tr>",
                            "<tr><td>3</td><td>154</td></tr>",
                            "<tr><td>3</td><td>155</td></tr>",
                            "<tr><td>2</td><td>156</td></tr>",
                            "<tr><td>2</td><td>157</td></tr>",
                            "<tr><td>3</td><td>158</td></tr>",
                            "<tr><td>2</td><td>160</td></tr>",
                            "<tr><td>3</td><td>161</td></tr>",
                            "<tr><td>2</td><td>162</td></tr>",
                            "<tr><td>5</td><td>163</td></tr>",
                            "<tr><td>4</td><td>164</td></tr>",
                            "<tr><td>5</td><td>165</td></tr>",
                            "<tr><td>3</td><td>166</td></tr>",
                            "<tr><td>2</td><td>167</td></tr>",
                            "<tr><td>1</td><td>168</td></tr>",
                            "<tr><td>3</td><td>169</td></tr>",
                            "<tr><td>3</td><td>170</td></tr>",
                            "<tr><td>5</td><td>171</td></tr>",
                            "<tr><td>6</td><td>172</td></tr>",
                            "<tr><td>3</td><td>173</td></tr>",
                            "<tr><td>4</td><td>174</td></tr>",
                            "<tr><td>3</td><td>175</td></tr>",
                            "<tr><td>2</td><td>176</td></tr>",
                            "<tr><td>1</td><td>177</td></tr>",
                            "<tr><td>1</td><td>178</td></tr>",
                            "<tr><td>2</td><td>179</td></tr>",
                            "<tr><td>1</td><td>180</td></tr>",
                            "<tr><td>5</td><td>181</td></tr>",
                            "<tr><td>11</td><td>182</td></tr>",
                            "<tr><td>3</td><td>183</td></tr>",
                            "<tr><td>4</td><td>184</td></tr>",
                            "<tr><td>10</td><td>185</td></tr>",
                            "<tr><td>1</td><td>186</td></tr>",
                            "<tr><td>6</td><td>187</td></tr>",
                            "<tr><td>2</td><td>188</td></tr>",
                            "<tr><td>1</td><td>189</td></tr>",
                            "<tr><td>5</td><td>190</td></tr>",
                            "<tr><td>3</td><td>191</td></tr>",
                            "<tr><td>1</td><td>192</td></tr>",
                            "<tr><td>2</td><td>193</td></tr>",
                            "<tr><td>1</td><td>194</td></tr>",
                            "<tr><td>5</td><td>195</td></tr>",
                            "<tr><td>2</td><td>196</td></tr>",
                            "<tr><td>6</td><td>197</td></tr>",
                            "<tr><td>7</td><td>198</td></tr>",
                            "<tr><td>668</td><td>végérték</td></tr>",
                            "</table>"
                        ]
                    }
                }
            ],
            "execution_count": 1
        },
        {
            "cell_type": "code",
            "source": [
                "--Készítsük listát, \r\n",
                "--amely a szobák azonosítóit és a hozzájuk tartozó foglalások azonosítóját és időtartalmát (napokban) jeleníti meg!\r\n",
                "\r\n",
                "--Egy új oszlopban jelenítsük meg az adott szoba időben előző foglalásának időtartamát is!\r\n",
                "--Ha nincs előző, akkor 0 jelenjen meg\r\n",
                "\r\n",
                "select SZOBA_FK,\r\n",
                "        FOGLALAS_PK,\r\n",
                "        DATEDIFF(day, mettol, MEDDIG) as 'idotartam',\r\n",
                "        lag(DATEDIFF(DAY, METTOL, MEDDIG), 1, 0) over (partition by szoba_fk order by METTOL)\r\n",
                "from Foglalas"
            ],
            "metadata": {
                "language": "sql",
                "azdata_cell_guid": "59e6a580-371f-4a6e-981a-03232ea778ea"
            },
            "outputs": [
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "(1027 rows affected)"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "Total execution time: 00:00:00.082"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "execute_result",
                    "execution_count": 8,
                    "data": {
                        "application/vnd.dataresource+json": {
                            "schema": {
                                "fields": [
                                    {
                                        "name": "SZOBA_FK"
                                    },
                                    {
                                        "name": "FOGLALAS_PK"
                                    },
                                    {
                                        "name": "mettol"
                                    },
                                    {
                                        "name": "meddig"
                                    },
                                    {
                                        "name": "idotartam"
                                    },
                                    {
                                        "name": "(No column name)"
                                    }
                                ]
                            },
                            "data": [
                                {
                                    "SZOBA_FK": "1",
                                    "FOGLALAS_PK": "620",
                                    "mettol": "2016-05-05",
                                    "meddig": "2016-05-10",
                                    "idotartam": "5",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "1",
                                    "FOGLALAS_PK": "949",
                                    "mettol": "2016-06-10",
                                    "meddig": "2016-06-11",
                                    "idotartam": "1",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "1",
                                    "FOGLALAS_PK": "738",
                                    "mettol": "2016-07-30",
                                    "meddig": "2016-08-06",
                                    "idotartam": "7",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "1",
                                    "FOGLALAS_PK": "803",
                                    "mettol": "2016-08-20",
                                    "meddig": "2016-08-24",
                                    "idotartam": "4",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "1",
                                    "FOGLALAS_PK": "1137",
                                    "mettol": "2016-10-09",
                                    "meddig": "2016-10-11",
                                    "idotartam": "2",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "1",
                                    "FOGLALAS_PK": "1152",
                                    "mettol": "2016-10-15",
                                    "meddig": "2016-10-16",
                                    "idotartam": "1",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "1",
                                    "FOGLALAS_PK": "1274",
                                    "mettol": "2016-11-11",
                                    "meddig": "2016-11-12",
                                    "idotartam": "1",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "1",
                                    "FOGLALAS_PK": "1334",
                                    "mettol": "2016-12-01",
                                    "meddig": "2016-12-05",
                                    "idotartam": "4",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "2",
                                    "FOGLALAS_PK": "828",
                                    "mettol": "2016-08-27",
                                    "meddig": "2016-08-30",
                                    "idotartam": "3",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "2",
                                    "FOGLALAS_PK": "1051",
                                    "mettol": "2016-09-14",
                                    "meddig": "2016-09-15",
                                    "idotartam": "1",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "2",
                                    "FOGLALAS_PK": "1069",
                                    "mettol": "2016-09-19",
                                    "meddig": "2016-09-26",
                                    "idotartam": "7",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "2",
                                    "FOGLALAS_PK": "1311",
                                    "mettol": "2016-11-23",
                                    "meddig": "2016-11-30",
                                    "idotartam": "7",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "3",
                                    "FOGLALAS_PK": "629",
                                    "mettol": "2016-05-09",
                                    "meddig": "2016-05-13",
                                    "idotartam": "4",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "3",
                                    "FOGLALAS_PK": "666",
                                    "mettol": "2016-07-13",
                                    "meddig": "2016-07-19",
                                    "idotartam": "6",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "3",
                                    "FOGLALAS_PK": "788",
                                    "mettol": "2016-08-16",
                                    "meddig": "2016-08-22",
                                    "idotartam": "6",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "3",
                                    "FOGLALAS_PK": "1038",
                                    "mettol": "2016-09-08",
                                    "meddig": "2016-09-11",
                                    "idotartam": "3",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "3",
                                    "FOGLALAS_PK": "1110",
                                    "mettol": "2016-10-01",
                                    "meddig": "2016-10-08",
                                    "idotartam": "7",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "3",
                                    "FOGLALAS_PK": "1151",
                                    "mettol": "2016-10-14",
                                    "meddig": "2016-10-15",
                                    "idotartam": "1",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "3",
                                    "FOGLALAS_PK": "1434",
                                    "mettol": "2017-01-12",
                                    "meddig": "2017-01-17",
                                    "idotartam": "5",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "3",
                                    "FOGLALAS_PK": "1544",
                                    "mettol": "2017-02-16",
                                    "meddig": "2017-02-21",
                                    "idotartam": "5",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "4",
                                    "FOGLALAS_PK": "651",
                                    "mettol": "2016-05-17",
                                    "meddig": "2016-05-24",
                                    "idotartam": "7",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "4",
                                    "FOGLALAS_PK": "946",
                                    "mettol": "2016-06-10",
                                    "meddig": "2016-06-15",
                                    "idotartam": "5",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "4",
                                    "FOGLALAS_PK": "1001",
                                    "mettol": "2016-07-02",
                                    "meddig": "2016-07-09",
                                    "idotartam": "7",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "4",
                                    "FOGLALAS_PK": "1127",
                                    "mettol": "2016-10-07",
                                    "meddig": "2016-10-10",
                                    "idotartam": "3",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "4",
                                    "FOGLALAS_PK": "1132",
                                    "mettol": "2016-10-08",
                                    "meddig": "2016-10-14",
                                    "idotartam": "6",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "4",
                                    "FOGLALAS_PK": "1492",
                                    "mettol": "2017-02-03",
                                    "meddig": "2017-02-09",
                                    "idotartam": "6",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "5",
                                    "FOGLALAS_PK": "564",
                                    "mettol": "2016-04-08",
                                    "meddig": "2016-04-10",
                                    "idotartam": "2",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "5",
                                    "FOGLALAS_PK": "965",
                                    "mettol": "2016-06-16",
                                    "meddig": "2016-06-23",
                                    "idotartam": "7",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "5",
                                    "FOGLALAS_PK": "1073",
                                    "mettol": "2016-09-21",
                                    "meddig": "2016-09-26",
                                    "idotartam": "5",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "5",
                                    "FOGLALAS_PK": "1257",
                                    "mettol": "2016-11-07",
                                    "meddig": "2016-11-10",
                                    "idotartam": "3",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "6",
                                    "FOGLALAS_PK": "560",
                                    "mettol": "2016-04-06",
                                    "meddig": "2016-04-12",
                                    "idotartam": "6",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "6",
                                    "FOGLALAS_PK": "873",
                                    "mettol": "2016-05-29",
                                    "meddig": "2016-06-01",
                                    "idotartam": "3",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "6",
                                    "FOGLALAS_PK": "990",
                                    "mettol": "2016-06-27",
                                    "meddig": "2016-07-01",
                                    "idotartam": "4",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "6",
                                    "FOGLALAS_PK": "772",
                                    "mettol": "2016-08-12",
                                    "meddig": "2016-08-18",
                                    "idotartam": "6",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "6",
                                    "FOGLALAS_PK": "850",
                                    "mettol": "2016-09-05",
                                    "meddig": "2016-09-07",
                                    "idotartam": "2",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "6",
                                    "FOGLALAS_PK": "1099",
                                    "mettol": "2016-10-01",
                                    "meddig": "2016-10-05",
                                    "idotartam": "4",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "7",
                                    "FOGLALAS_PK": "562",
                                    "mettol": "2016-04-06",
                                    "meddig": "2016-04-10",
                                    "idotartam": "4",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "7",
                                    "FOGLALAS_PK": "759",
                                    "mettol": "2016-08-06",
                                    "meddig": "2016-08-13",
                                    "idotartam": "7",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "7",
                                    "FOGLALAS_PK": "1131",
                                    "mettol": "2016-10-08",
                                    "meddig": "2016-10-09",
                                    "idotartam": "1",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "7",
                                    "FOGLALAS_PK": "1175",
                                    "mettol": "2016-10-21",
                                    "meddig": "2016-10-25",
                                    "idotartam": "4",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "7",
                                    "FOGLALAS_PK": "1182",
                                    "mettol": "2016-10-23",
                                    "meddig": "2016-10-27",
                                    "idotartam": "4",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "7",
                                    "FOGLALAS_PK": "1252",
                                    "mettol": "2016-11-05",
                                    "meddig": "2016-11-07",
                                    "idotartam": "2",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "8",
                                    "FOGLALAS_PK": "882",
                                    "mettol": "2016-05-30",
                                    "meddig": "2016-05-31",
                                    "idotartam": "1",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "8",
                                    "FOGLALAS_PK": "947",
                                    "mettol": "2016-06-10",
                                    "meddig": "2016-06-13",
                                    "idotartam": "3",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "8",
                                    "FOGLALAS_PK": "694",
                                    "mettol": "2016-07-20",
                                    "meddig": "2016-07-24",
                                    "idotartam": "4",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "8",
                                    "FOGLALAS_PK": "818",
                                    "mettol": "2016-08-24",
                                    "meddig": "2016-08-28",
                                    "idotartam": "4",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "8",
                                    "FOGLALAS_PK": "832",
                                    "mettol": "2016-08-28",
                                    "meddig": "2016-09-01",
                                    "idotartam": "4",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "9",
                                    "FOGLALAS_PK": "609",
                                    "mettol": "2016-04-29",
                                    "meddig": "2016-05-01",
                                    "idotartam": "2",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "9",
                                    "FOGLALAS_PK": "1157",
                                    "mettol": "2016-10-15",
                                    "meddig": "2016-10-21",
                                    "idotartam": "6",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "9",
                                    "FOGLALAS_PK": "1220",
                                    "mettol": "2016-10-30",
                                    "meddig": "2016-11-02",
                                    "idotartam": "3",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "9",
                                    "FOGLALAS_PK": "1260",
                                    "mettol": "2016-11-07",
                                    "meddig": "2016-11-13",
                                    "idotartam": "6",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "9",
                                    "FOGLALAS_PK": "1423",
                                    "mettol": "2017-01-06",
                                    "meddig": "2017-01-09",
                                    "idotartam": "3",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "9",
                                    "FOGLALAS_PK": "1537",
                                    "mettol": "2017-02-16",
                                    "meddig": "2017-02-19",
                                    "idotartam": "3",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "10",
                                    "FOGLALAS_PK": "569",
                                    "mettol": "2016-04-10",
                                    "meddig": "2016-04-13",
                                    "idotartam": "3",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "10",
                                    "FOGLALAS_PK": "790",
                                    "mettol": "2016-08-16",
                                    "meddig": "2016-08-21",
                                    "idotartam": "5",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "10",
                                    "FOGLALAS_PK": "795",
                                    "mettol": "2016-08-17",
                                    "meddig": "2016-08-21",
                                    "idotartam": "4",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "10",
                                    "FOGLALAS_PK": "1319",
                                    "mettol": "2016-11-25",
                                    "meddig": "2016-12-01",
                                    "idotartam": "6",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "11",
                                    "FOGLALAS_PK": "918",
                                    "mettol": "2016-06-06",
                                    "meddig": "2016-06-12",
                                    "idotartam": "6",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "11",
                                    "FOGLALAS_PK": "1123",
                                    "mettol": "2016-10-05",
                                    "meddig": "2016-10-10",
                                    "idotartam": "5",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "11",
                                    "FOGLALAS_PK": "1236",
                                    "mettol": "2016-11-01",
                                    "meddig": "2016-11-02",
                                    "idotartam": "1",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "11",
                                    "FOGLALAS_PK": "1523",
                                    "mettol": "2017-02-12",
                                    "meddig": "2017-02-13",
                                    "idotartam": "1",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "12",
                                    "FOGLALAS_PK": "876",
                                    "mettol": "2016-05-30",
                                    "meddig": "2016-06-06",
                                    "idotartam": "7",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "12",
                                    "FOGLALAS_PK": "951",
                                    "mettol": "2016-06-11",
                                    "meddig": "2016-06-14",
                                    "idotartam": "3",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "12",
                                    "FOGLALAS_PK": "970",
                                    "mettol": "2016-06-17",
                                    "meddig": "2016-06-19",
                                    "idotartam": "2",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "12",
                                    "FOGLALAS_PK": "1020",
                                    "mettol": "2016-07-09",
                                    "meddig": "2016-07-14",
                                    "idotartam": "5",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "12",
                                    "FOGLALAS_PK": "697",
                                    "mettol": "2016-07-20",
                                    "meddig": "2016-07-22",
                                    "idotartam": "2",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "12",
                                    "FOGLALAS_PK": "775",
                                    "mettol": "2016-08-13",
                                    "meddig": "2016-08-17",
                                    "idotartam": "4",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "12",
                                    "FOGLALAS_PK": "1140",
                                    "mettol": "2016-10-09",
                                    "meddig": "2016-10-12",
                                    "idotartam": "3",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "12",
                                    "FOGLALAS_PK": "1164",
                                    "mettol": "2016-10-18",
                                    "meddig": "2016-10-23",
                                    "idotartam": "5",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "12",
                                    "FOGLALAS_PK": "1430",
                                    "mettol": "2017-01-09",
                                    "meddig": "2017-01-11",
                                    "idotartam": "2",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "13",
                                    "FOGLALAS_PK": "763",
                                    "mettol": "2016-08-08",
                                    "meddig": "2016-08-12",
                                    "idotartam": "4",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "13",
                                    "FOGLALAS_PK": "1044",
                                    "mettol": "2016-09-12",
                                    "meddig": "2016-09-18",
                                    "idotartam": "6",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "13",
                                    "FOGLALAS_PK": "1347",
                                    "mettol": "2016-12-06",
                                    "meddig": "2016-12-09",
                                    "idotartam": "3",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "13",
                                    "FOGLALAS_PK": "1469",
                                    "mettol": "2017-01-23",
                                    "meddig": "2017-01-25",
                                    "idotartam": "2",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "14",
                                    "FOGLALAS_PK": "663",
                                    "mettol": "2016-05-22",
                                    "meddig": "2016-05-23",
                                    "idotartam": "1",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "14",
                                    "FOGLALAS_PK": "813",
                                    "mettol": "2016-08-24",
                                    "meddig": "2016-08-27",
                                    "idotartam": "3",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "14",
                                    "FOGLALAS_PK": "1542",
                                    "mettol": "2017-02-16",
                                    "meddig": "2017-02-20",
                                    "idotartam": "4",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "15",
                                    "FOGLALAS_PK": "1028",
                                    "mettol": "2016-07-13",
                                    "meddig": "2016-07-15",
                                    "idotartam": "2",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "15",
                                    "FOGLALAS_PK": "791",
                                    "mettol": "2016-08-16",
                                    "meddig": "2016-08-21",
                                    "idotartam": "5",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "15",
                                    "FOGLALAS_PK": "1129",
                                    "mettol": "2016-10-08",
                                    "meddig": "2016-10-12",
                                    "idotartam": "4",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "15",
                                    "FOGLALAS_PK": "1244",
                                    "mettol": "2016-11-03",
                                    "meddig": "2016-11-04",
                                    "idotartam": "1",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "15",
                                    "FOGLALAS_PK": "1418",
                                    "mettol": "2017-01-04",
                                    "meddig": "2017-01-08",
                                    "idotartam": "4",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "15",
                                    "FOGLALAS_PK": "1442",
                                    "mettol": "2017-01-16",
                                    "meddig": "2017-01-19",
                                    "idotartam": "3",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "16",
                                    "FOGLALAS_PK": "856",
                                    "mettol": "2016-05-24",
                                    "meddig": "2016-05-30",
                                    "idotartam": "6",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "16",
                                    "FOGLALAS_PK": "896",
                                    "mettol": "2016-06-03",
                                    "meddig": "2016-06-04",
                                    "idotartam": "1",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "16",
                                    "FOGLALAS_PK": "973",
                                    "mettol": "2016-06-20",
                                    "meddig": "2016-06-21",
                                    "idotartam": "1",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "16",
                                    "FOGLALAS_PK": "687",
                                    "mettol": "2016-07-18",
                                    "meddig": "2016-07-21",
                                    "idotartam": "3",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "16",
                                    "FOGLALAS_PK": "1498",
                                    "mettol": "2017-02-04",
                                    "meddig": "2017-02-11",
                                    "idotartam": "7",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "17",
                                    "FOGLALAS_PK": "602",
                                    "mettol": "2016-04-26",
                                    "meddig": "2016-05-02",
                                    "idotartam": "6",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "17",
                                    "FOGLALAS_PK": "916",
                                    "mettol": "2016-06-06",
                                    "meddig": "2016-06-08",
                                    "idotartam": "2",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "17",
                                    "FOGLALAS_PK": "713",
                                    "mettol": "2016-07-24",
                                    "meddig": "2016-07-30",
                                    "idotartam": "6",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "17",
                                    "FOGLALAS_PK": "744",
                                    "mettol": "2016-08-01",
                                    "meddig": "2016-08-02",
                                    "idotartam": "1",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "17",
                                    "FOGLALAS_PK": "1316",
                                    "mettol": "2016-11-25",
                                    "meddig": "2016-11-30",
                                    "idotartam": "5",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "17",
                                    "FOGLALAS_PK": "1549",
                                    "mettol": "2017-02-18",
                                    "meddig": "2017-02-21",
                                    "idotartam": "3",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "18",
                                    "FOGLALAS_PK": "626",
                                    "mettol": "2016-05-08",
                                    "meddig": "2016-05-11",
                                    "idotartam": "3",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "18",
                                    "FOGLALAS_PK": "767",
                                    "mettol": "2016-08-11",
                                    "meddig": "2016-08-14",
                                    "idotartam": "3",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "18",
                                    "FOGLALAS_PK": "1035",
                                    "mettol": "2016-09-07",
                                    "meddig": "2016-09-13",
                                    "idotartam": "6",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "18",
                                    "FOGLALAS_PK": "1173",
                                    "mettol": "2016-10-21",
                                    "meddig": "2016-10-27",
                                    "idotartam": "6",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "18",
                                    "FOGLALAS_PK": "1198",
                                    "mettol": "2016-10-26",
                                    "meddig": "2016-10-30",
                                    "idotartam": "4",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "18",
                                    "FOGLALAS_PK": "1505",
                                    "mettol": "2017-02-06",
                                    "meddig": "2017-02-12",
                                    "idotartam": "6",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "19",
                                    "FOGLALAS_PK": "948",
                                    "mettol": "2016-06-10",
                                    "meddig": "2016-06-12",
                                    "idotartam": "2",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "19",
                                    "FOGLALAS_PK": "696",
                                    "mettol": "2016-07-20",
                                    "meddig": "2016-07-21",
                                    "idotartam": "1",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "19",
                                    "FOGLALAS_PK": "778",
                                    "mettol": "2016-08-14",
                                    "meddig": "2016-08-15",
                                    "idotartam": "1",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "19",
                                    "FOGLALAS_PK": "1139",
                                    "mettol": "2016-10-09",
                                    "meddig": "2016-10-16",
                                    "idotartam": "7",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "19",
                                    "FOGLALAS_PK": "1237",
                                    "mettol": "2016-11-02",
                                    "meddig": "2016-11-03",
                                    "idotartam": "1",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "19",
                                    "FOGLALAS_PK": "1533",
                                    "mettol": "2017-02-14",
                                    "meddig": "2017-02-15",
                                    "idotartam": "1",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "20",
                                    "FOGLALAS_PK": "755",
                                    "mettol": "2016-08-04",
                                    "meddig": "2016-08-10",
                                    "idotartam": "6",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "20",
                                    "FOGLALAS_PK": "820",
                                    "mettol": "2016-08-24",
                                    "meddig": "2016-08-25",
                                    "idotartam": "1",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "20",
                                    "FOGLALAS_PK": "1070",
                                    "mettol": "2016-09-19",
                                    "meddig": "2016-09-20",
                                    "idotartam": "1",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "20",
                                    "FOGLALAS_PK": "1114",
                                    "mettol": "2016-10-01",
                                    "meddig": "2016-10-06",
                                    "idotartam": "5",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "20",
                                    "FOGLALAS_PK": "1106",
                                    "mettol": "2016-10-01",
                                    "meddig": "2016-10-03",
                                    "idotartam": "2",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "21",
                                    "FOGLALAS_PK": "566",
                                    "mettol": "2016-04-09",
                                    "meddig": "2016-04-15",
                                    "idotartam": "6",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "21",
                                    "FOGLALAS_PK": "660",
                                    "mettol": "2016-05-21",
                                    "meddig": "2016-05-26",
                                    "idotartam": "5",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "21",
                                    "FOGLALAS_PK": "805",
                                    "mettol": "2016-08-21",
                                    "meddig": "2016-08-22",
                                    "idotartam": "1",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "21",
                                    "FOGLALAS_PK": "1212",
                                    "mettol": "2016-10-28",
                                    "meddig": "2016-11-03",
                                    "idotartam": "6",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "22",
                                    "FOGLALAS_PK": "906",
                                    "mettol": "2016-06-04",
                                    "meddig": "2016-06-05",
                                    "idotartam": "1",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "22",
                                    "FOGLALAS_PK": "1005",
                                    "mettol": "2016-07-03",
                                    "meddig": "2016-07-06",
                                    "idotartam": "3",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "22",
                                    "FOGLALAS_PK": "1130",
                                    "mettol": "2016-10-08",
                                    "meddig": "2016-10-09",
                                    "idotartam": "1",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "22",
                                    "FOGLALAS_PK": "1195",
                                    "mettol": "2016-10-26",
                                    "meddig": "2016-11-01",
                                    "idotartam": "6",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "22",
                                    "FOGLALAS_PK": "1206",
                                    "mettol": "2016-10-27",
                                    "meddig": "2016-11-03",
                                    "idotartam": "7",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "22",
                                    "FOGLALAS_PK": "1287",
                                    "mettol": "2016-11-17",
                                    "meddig": "2016-11-20",
                                    "idotartam": "3",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "23",
                                    "FOGLALAS_PK": "934",
                                    "mettol": "2016-06-08",
                                    "meddig": "2016-06-09",
                                    "idotartam": "1",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "23",
                                    "FOGLALAS_PK": "945",
                                    "mettol": "2016-06-10",
                                    "meddig": "2016-06-17",
                                    "idotartam": "7",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "23",
                                    "FOGLALAS_PK": "848",
                                    "mettol": "2016-09-04",
                                    "meddig": "2016-09-05",
                                    "idotartam": "1",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "24",
                                    "FOGLALAS_PK": "852",
                                    "mettol": "2016-05-23",
                                    "meddig": "2016-05-25",
                                    "idotartam": "2",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "24",
                                    "FOGLALAS_PK": "1167",
                                    "mettol": "2016-10-19",
                                    "meddig": "2016-10-20",
                                    "idotartam": "1",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "24",
                                    "FOGLALAS_PK": "1415",
                                    "mettol": "2017-01-03",
                                    "meddig": "2017-01-06",
                                    "idotartam": "3",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "25",
                                    "FOGLALAS_PK": "1052",
                                    "mettol": "2016-09-14",
                                    "meddig": "2016-09-17",
                                    "idotartam": "3",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "25",
                                    "FOGLALAS_PK": "1362",
                                    "mettol": "2016-12-14",
                                    "meddig": "2016-12-16",
                                    "idotartam": "2",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "26",
                                    "FOGLALAS_PK": "1158",
                                    "mettol": "2016-10-16",
                                    "meddig": "2016-10-18",
                                    "idotartam": "2",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "26",
                                    "FOGLALAS_PK": "1388",
                                    "mettol": "2016-12-24",
                                    "meddig": "2016-12-27",
                                    "idotartam": "3",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "27",
                                    "FOGLALAS_PK": "758",
                                    "mettol": "2016-08-05",
                                    "meddig": "2016-08-08",
                                    "idotartam": "3",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "27",
                                    "FOGLALAS_PK": "807",
                                    "mettol": "2016-08-22",
                                    "meddig": "2016-08-24",
                                    "idotartam": "2",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "27",
                                    "FOGLALAS_PK": "1031",
                                    "mettol": "2016-09-05",
                                    "meddig": "2016-09-07",
                                    "idotartam": "2",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "27",
                                    "FOGLALAS_PK": "1082",
                                    "mettol": "2016-09-26",
                                    "meddig": "2016-10-01",
                                    "idotartam": "5",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "27",
                                    "FOGLALAS_PK": "1275",
                                    "mettol": "2016-11-11",
                                    "meddig": "2016-11-17",
                                    "idotartam": "6",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "27",
                                    "FOGLALAS_PK": "1377",
                                    "mettol": "2016-12-18",
                                    "meddig": "2016-12-19",
                                    "idotartam": "1",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "27",
                                    "FOGLALAS_PK": "1476",
                                    "mettol": "2017-01-27",
                                    "meddig": "2017-01-28",
                                    "idotartam": "1",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "28",
                                    "FOGLALAS_PK": "872",
                                    "mettol": "2016-05-29",
                                    "meddig": "2016-06-03",
                                    "idotartam": "5",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "28",
                                    "FOGLALAS_PK": "886",
                                    "mettol": "2016-06-01",
                                    "meddig": "2016-06-05",
                                    "idotartam": "4",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "28",
                                    "FOGLALAS_PK": "901",
                                    "mettol": "2016-06-04",
                                    "meddig": "2016-06-08",
                                    "idotartam": "4",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "28",
                                    "FOGLALAS_PK": "725",
                                    "mettol": "2016-07-27",
                                    "meddig": "2016-08-01",
                                    "idotartam": "5",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "28",
                                    "FOGLALAS_PK": "1150",
                                    "mettol": "2016-10-13",
                                    "meddig": "2016-10-19",
                                    "idotartam": "6",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "28",
                                    "FOGLALAS_PK": "1459",
                                    "mettol": "2017-01-20",
                                    "meddig": "2017-01-22",
                                    "idotartam": "2",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "29",
                                    "FOGLALAS_PK": "611",
                                    "mettol": "2016-05-01",
                                    "meddig": "2016-05-06",
                                    "idotartam": "5",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "29",
                                    "FOGLALAS_PK": "894",
                                    "mettol": "2016-06-03",
                                    "meddig": "2016-06-04",
                                    "idotartam": "1",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "29",
                                    "FOGLALAS_PK": "1076",
                                    "mettol": "2016-09-23",
                                    "meddig": "2016-09-30",
                                    "idotartam": "7",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "29",
                                    "FOGLALAS_PK": "1185",
                                    "mettol": "2016-10-23",
                                    "meddig": "2016-10-28",
                                    "idotartam": "5",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "29",
                                    "FOGLALAS_PK": "1235",
                                    "mettol": "2016-11-01",
                                    "meddig": "2016-11-08",
                                    "idotartam": "7",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "29",
                                    "FOGLALAS_PK": "1568",
                                    "mettol": "2017-02-24",
                                    "meddig": "2017-03-03",
                                    "idotartam": "7",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "30",
                                    "FOGLALAS_PK": "604",
                                    "mettol": "2016-04-27",
                                    "meddig": "2016-04-29",
                                    "idotartam": "2",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "30",
                                    "FOGLALAS_PK": "1023",
                                    "mettol": "2016-07-10",
                                    "meddig": "2016-07-17",
                                    "idotartam": "7",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "30",
                                    "FOGLALAS_PK": "1136",
                                    "mettol": "2016-10-09",
                                    "meddig": "2016-10-14",
                                    "idotartam": "5",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "31",
                                    "FOGLALAS_PK": "598",
                                    "mettol": "2016-04-24",
                                    "meddig": "2016-04-26",
                                    "idotartam": "2",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "31",
                                    "FOGLALAS_PK": "606",
                                    "mettol": "2016-04-27",
                                    "meddig": "2016-04-28",
                                    "idotartam": "1",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "31",
                                    "FOGLALAS_PK": "728",
                                    "mettol": "2016-07-27",
                                    "meddig": "2016-07-31",
                                    "idotartam": "4",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "32",
                                    "FOGLALAS_PK": "920",
                                    "mettol": "2016-06-06",
                                    "meddig": "2016-06-10",
                                    "idotartam": "4",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "33",
                                    "FOGLALAS_PK": "624",
                                    "mettol": "2016-05-08",
                                    "meddig": "2016-05-14",
                                    "idotartam": "6",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "33",
                                    "FOGLALAS_PK": "1012",
                                    "mettol": "2016-07-05",
                                    "meddig": "2016-07-12",
                                    "idotartam": "7",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "33",
                                    "FOGLALAS_PK": "1053",
                                    "mettol": "2016-09-15",
                                    "meddig": "2016-09-16",
                                    "idotartam": "1",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "33",
                                    "FOGLALAS_PK": "1321",
                                    "mettol": "2016-11-25",
                                    "meddig": "2016-11-29",
                                    "idotartam": "4",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "33",
                                    "FOGLALAS_PK": "1344",
                                    "mettol": "2016-12-05",
                                    "meddig": "2016-12-10",
                                    "idotartam": "5",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "33",
                                    "FOGLALAS_PK": "1381",
                                    "mettol": "2016-12-21",
                                    "meddig": "2016-12-27",
                                    "idotartam": "6",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "34",
                                    "FOGLALAS_PK": "870",
                                    "mettol": "2016-05-28",
                                    "meddig": "2016-06-03",
                                    "idotartam": "6",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "34",
                                    "FOGLALAS_PK": "904",
                                    "mettol": "2016-06-04",
                                    "meddig": "2016-06-06",
                                    "idotartam": "2",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "34",
                                    "FOGLALAS_PK": "777",
                                    "mettol": "2016-08-14",
                                    "meddig": "2016-08-17",
                                    "idotartam": "3",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "34",
                                    "FOGLALAS_PK": "821",
                                    "mettol": "2016-08-24",
                                    "meddig": "2016-08-25",
                                    "idotartam": "1",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "35",
                                    "FOGLALAS_PK": "971",
                                    "mettol": "2016-06-18",
                                    "meddig": "2016-06-21",
                                    "idotartam": "3",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "35",
                                    "FOGLALAS_PK": "979",
                                    "mettol": "2016-06-22",
                                    "meddig": "2016-06-29",
                                    "idotartam": "7",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "35",
                                    "FOGLALAS_PK": "686",
                                    "mettol": "2016-07-18",
                                    "meddig": "2016-07-24",
                                    "idotartam": "6",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "35",
                                    "FOGLALAS_PK": "707",
                                    "mettol": "2016-07-23",
                                    "meddig": "2016-07-25",
                                    "idotartam": "2",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "35",
                                    "FOGLALAS_PK": "829",
                                    "mettol": "2016-08-28",
                                    "meddig": "2016-08-30",
                                    "idotartam": "2",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "35",
                                    "FOGLALAS_PK": "1480",
                                    "mettol": "2016-12-29",
                                    "meddig": "2017-02-04",
                                    "idotartam": "37",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "35",
                                    "FOGLALAS_PK": "1411",
                                    "mettol": "2017-01-01",
                                    "meddig": "2017-01-02",
                                    "idotartam": "1",
                                    "(No column name)": "37"
                                },
                                {
                                    "SZOBA_FK": "35",
                                    "FOGLALAS_PK": "1436",
                                    "mettol": "2017-01-13",
                                    "meddig": "2017-01-14",
                                    "idotartam": "1",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "35",
                                    "FOGLALAS_PK": "1529",
                                    "mettol": "2017-02-13",
                                    "meddig": "2017-02-17",
                                    "idotartam": "4",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "36",
                                    "FOGLALAS_PK": "895",
                                    "mettol": "2016-06-03",
                                    "meddig": "2016-06-08",
                                    "idotartam": "5",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "36",
                                    "FOGLALAS_PK": "919",
                                    "mettol": "2016-06-06",
                                    "meddig": "2016-06-07",
                                    "idotartam": "1",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "36",
                                    "FOGLALAS_PK": "985",
                                    "mettol": "2016-06-24",
                                    "meddig": "2016-06-30",
                                    "idotartam": "6",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "36",
                                    "FOGLALAS_PK": "1003",
                                    "mettol": "2016-07-03",
                                    "meddig": "2016-07-07",
                                    "idotartam": "4",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "36",
                                    "FOGLALAS_PK": "748",
                                    "mettol": "2016-08-02",
                                    "meddig": "2016-08-04",
                                    "idotartam": "2",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "36",
                                    "FOGLALAS_PK": "750",
                                    "mettol": "2016-08-03",
                                    "meddig": "2016-08-09",
                                    "idotartam": "6",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "37",
                                    "FOGLALAS_PK": "688",
                                    "mettol": "2016-07-19",
                                    "meddig": "2016-07-21",
                                    "idotartam": "2",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "37",
                                    "FOGLALAS_PK": "705",
                                    "mettol": "2016-07-22",
                                    "meddig": "2016-07-26",
                                    "idotartam": "4",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "37",
                                    "FOGLALAS_PK": "1335",
                                    "mettol": "2016-12-01",
                                    "meddig": "2016-12-08",
                                    "idotartam": "7",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "38",
                                    "FOGLALAS_PK": "627",
                                    "mettol": "2016-05-08",
                                    "meddig": "2016-05-14",
                                    "idotartam": "6",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "38",
                                    "FOGLALAS_PK": "1033",
                                    "mettol": "2016-09-05",
                                    "meddig": "2016-09-07",
                                    "idotartam": "2",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "38",
                                    "FOGLALAS_PK": "1060",
                                    "mettol": "2016-09-17",
                                    "meddig": "2016-09-19",
                                    "idotartam": "2",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "38",
                                    "FOGLALAS_PK": "1078",
                                    "mettol": "2016-09-23",
                                    "meddig": "2016-09-30",
                                    "idotartam": "7",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "38",
                                    "FOGLALAS_PK": "1351",
                                    "mettol": "2016-12-06",
                                    "meddig": "2016-12-10",
                                    "idotartam": "4",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "38",
                                    "FOGLALAS_PK": "1416",
                                    "mettol": "2017-01-03",
                                    "meddig": "2017-01-08",
                                    "idotartam": "5",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "38",
                                    "FOGLALAS_PK": "1478",
                                    "mettol": "2017-01-28",
                                    "meddig": "2017-02-01",
                                    "idotartam": "4",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "38",
                                    "FOGLALAS_PK": "1556",
                                    "mettol": "2017-02-21",
                                    "meddig": "2017-02-27",
                                    "idotartam": "6",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "39",
                                    "FOGLALAS_PK": "601",
                                    "mettol": "2016-04-25",
                                    "meddig": "2016-05-01",
                                    "idotartam": "6",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "39",
                                    "FOGLALAS_PK": "899",
                                    "mettol": "2016-06-03",
                                    "meddig": "2016-06-09",
                                    "idotartam": "6",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "39",
                                    "FOGLALAS_PK": "1214",
                                    "mettol": "2016-10-29",
                                    "meddig": "2016-11-03",
                                    "idotartam": "5",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "39",
                                    "FOGLALAS_PK": "1380",
                                    "mettol": "2016-12-20",
                                    "meddig": "2016-12-25",
                                    "idotartam": "5",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "39",
                                    "FOGLALAS_PK": "1435",
                                    "mettol": "2017-01-12",
                                    "meddig": "2017-01-19",
                                    "idotartam": "7",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "39",
                                    "FOGLALAS_PK": "1454",
                                    "mettol": "2017-01-18",
                                    "meddig": "2017-01-19",
                                    "idotartam": "1",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "39",
                                    "FOGLALAS_PK": "1538",
                                    "mettol": "2017-02-16",
                                    "meddig": "2017-02-18",
                                    "idotartam": "2",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "40",
                                    "FOGLALAS_PK": "924",
                                    "mettol": "2016-06-07",
                                    "meddig": "2016-06-12",
                                    "idotartam": "5",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "40",
                                    "FOGLALAS_PK": "932",
                                    "mettol": "2016-06-07",
                                    "meddig": "2016-06-13",
                                    "idotartam": "6",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "40",
                                    "FOGLALAS_PK": "1018",
                                    "mettol": "2016-07-08",
                                    "meddig": "2016-07-13",
                                    "idotartam": "5",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "40",
                                    "FOGLALAS_PK": "1118",
                                    "mettol": "2016-10-03",
                                    "meddig": "2016-10-08",
                                    "idotartam": "5",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "41",
                                    "FOGLALAS_PK": "960",
                                    "mettol": "2016-06-15",
                                    "meddig": "2016-06-21",
                                    "idotartam": "6",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "41",
                                    "FOGLALAS_PK": "1144",
                                    "mettol": "2016-10-09",
                                    "meddig": "2016-10-10",
                                    "idotartam": "1",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "42",
                                    "FOGLALAS_PK": "561",
                                    "mettol": "2016-04-06",
                                    "meddig": "2016-04-10",
                                    "idotartam": "4",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "42",
                                    "FOGLALAS_PK": "590",
                                    "mettol": "2016-04-19",
                                    "meddig": "2016-04-24",
                                    "idotartam": "5",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "42",
                                    "FOGLALAS_PK": "851",
                                    "mettol": "2016-05-22",
                                    "meddig": "2016-05-29",
                                    "idotartam": "7",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "42",
                                    "FOGLALAS_PK": "770",
                                    "mettol": "2016-08-12",
                                    "meddig": "2016-08-15",
                                    "idotartam": "3",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "42",
                                    "FOGLALAS_PK": "1309",
                                    "mettol": "2016-11-23",
                                    "meddig": "2016-11-25",
                                    "idotartam": "2",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "42",
                                    "FOGLALAS_PK": "1444",
                                    "mettol": "2017-01-16",
                                    "meddig": "2017-01-22",
                                    "idotartam": "6",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "43",
                                    "FOGLALAS_PK": "1019",
                                    "mettol": "2016-07-08",
                                    "meddig": "2016-07-12",
                                    "idotartam": "4",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "43",
                                    "FOGLALAS_PK": "670",
                                    "mettol": "2016-07-14",
                                    "meddig": "2016-07-18",
                                    "idotartam": "4",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "43",
                                    "FOGLALAS_PK": "1088",
                                    "mettol": "2016-09-29",
                                    "meddig": "2016-10-01",
                                    "idotartam": "2",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "43",
                                    "FOGLALAS_PK": "1207",
                                    "mettol": "2016-10-27",
                                    "meddig": "2016-10-28",
                                    "idotartam": "1",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "43",
                                    "FOGLALAS_PK": "1227",
                                    "mettol": "2016-10-30",
                                    "meddig": "2016-11-04",
                                    "idotartam": "5",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "43",
                                    "FOGLALAS_PK": "1270",
                                    "mettol": "2016-11-10",
                                    "meddig": "2016-11-14",
                                    "idotartam": "4",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "43",
                                    "FOGLALAS_PK": "1524",
                                    "mettol": "2017-02-12",
                                    "meddig": "2017-02-13",
                                    "idotartam": "1",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "43",
                                    "FOGLALAS_PK": "1553",
                                    "mettol": "2017-02-20",
                                    "meddig": "2017-02-25",
                                    "idotartam": "5",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "44",
                                    "FOGLALAS_PK": "589",
                                    "mettol": "2016-04-19",
                                    "meddig": "2016-04-21",
                                    "idotartam": "2",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "44",
                                    "FOGLALAS_PK": "658",
                                    "mettol": "2016-05-21",
                                    "meddig": "2016-05-27",
                                    "idotartam": "6",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "44",
                                    "FOGLALAS_PK": "823",
                                    "mettol": "2016-08-25",
                                    "meddig": "2016-08-27",
                                    "idotartam": "2",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "44",
                                    "FOGLALAS_PK": "1295",
                                    "mettol": "2016-11-19",
                                    "meddig": "2016-11-21",
                                    "idotartam": "2",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "44",
                                    "FOGLALAS_PK": "1425",
                                    "mettol": "2017-01-08",
                                    "meddig": "2017-01-10",
                                    "idotartam": "2",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "44",
                                    "FOGLALAS_PK": "1552",
                                    "mettol": "2017-02-20",
                                    "meddig": "2017-02-22",
                                    "idotartam": "2",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "45",
                                    "FOGLALAS_PK": "802",
                                    "mettol": "2016-08-20",
                                    "meddig": "2016-08-27",
                                    "idotartam": "7",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "45",
                                    "FOGLALAS_PK": "800",
                                    "mettol": "2016-08-20",
                                    "meddig": "2016-08-25",
                                    "idotartam": "5",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "45",
                                    "FOGLALAS_PK": "846",
                                    "mettol": "2016-09-02",
                                    "meddig": "2016-09-05",
                                    "idotartam": "3",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "45",
                                    "FOGLALAS_PK": "1135",
                                    "mettol": "2016-10-09",
                                    "meddig": "2016-10-12",
                                    "idotartam": "3",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "45",
                                    "FOGLALAS_PK": "1303",
                                    "mettol": "2016-11-22",
                                    "meddig": "2016-11-24",
                                    "idotartam": "2",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "46",
                                    "FOGLALAS_PK": "752",
                                    "mettol": "2016-08-03",
                                    "meddig": "2016-08-08",
                                    "idotartam": "5",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "46",
                                    "FOGLALAS_PK": "1187",
                                    "mettol": "2016-10-23",
                                    "meddig": "2016-10-30",
                                    "idotartam": "7",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "46",
                                    "FOGLALAS_PK": "1291",
                                    "mettol": "2016-11-19",
                                    "meddig": "2016-11-22",
                                    "idotartam": "3",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "46",
                                    "FOGLALAS_PK": "1515",
                                    "mettol": "2017-02-10",
                                    "meddig": "2017-02-14",
                                    "idotartam": "4",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "47",
                                    "FOGLALAS_PK": "955",
                                    "mettol": "2016-06-13",
                                    "meddig": "2016-06-14",
                                    "idotartam": "1",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "47",
                                    "FOGLALAS_PK": "1056",
                                    "mettol": "2016-09-16",
                                    "meddig": "2016-09-23",
                                    "idotartam": "7",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "48",
                                    "FOGLALAS_PK": "603",
                                    "mettol": "2016-04-26",
                                    "meddig": "2016-04-29",
                                    "idotartam": "3",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "48",
                                    "FOGLALAS_PK": "628",
                                    "mettol": "2016-05-09",
                                    "meddig": "2016-05-11",
                                    "idotartam": "2",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "48",
                                    "FOGLALAS_PK": "914",
                                    "mettol": "2016-06-06",
                                    "meddig": "2016-06-11",
                                    "idotartam": "5",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "48",
                                    "FOGLALAS_PK": "986",
                                    "mettol": "2016-06-25",
                                    "meddig": "2016-06-30",
                                    "idotartam": "5",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "48",
                                    "FOGLALAS_PK": "824",
                                    "mettol": "2016-08-25",
                                    "meddig": "2016-08-27",
                                    "idotartam": "2",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "48",
                                    "FOGLALAS_PK": "1243",
                                    "mettol": "2016-11-03",
                                    "meddig": "2016-11-09",
                                    "idotartam": "6",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "48",
                                    "FOGLALAS_PK": "1546",
                                    "mettol": "2017-02-17",
                                    "meddig": "2017-02-20",
                                    "idotartam": "3",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "48",
                                    "FOGLALAS_PK": "1547",
                                    "mettol": "2017-02-18",
                                    "meddig": "2017-02-19",
                                    "idotartam": "1",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "48",
                                    "FOGLALAS_PK": "1581",
                                    "mettol": "2017-03-01",
                                    "meddig": "2017-03-06",
                                    "idotartam": "5",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "49",
                                    "FOGLALAS_PK": "888",
                                    "mettol": "2016-06-02",
                                    "meddig": "2016-06-09",
                                    "idotartam": "7",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "49",
                                    "FOGLALAS_PK": "793",
                                    "mettol": "2016-08-17",
                                    "meddig": "2016-08-23",
                                    "idotartam": "6",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "49",
                                    "FOGLALAS_PK": "826",
                                    "mettol": "2016-08-26",
                                    "meddig": "2016-08-30",
                                    "idotartam": "4",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "49",
                                    "FOGLALAS_PK": "1066",
                                    "mettol": "2016-09-18",
                                    "meddig": "2016-09-25",
                                    "idotartam": "7",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "49",
                                    "FOGLALAS_PK": "1200",
                                    "mettol": "2016-10-26",
                                    "meddig": "2016-11-02",
                                    "idotartam": "7",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "49",
                                    "FOGLALAS_PK": "1221",
                                    "mettol": "2016-10-30",
                                    "meddig": "2016-11-01",
                                    "idotartam": "2",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "49",
                                    "FOGLALAS_PK": "1536",
                                    "mettol": "2017-02-16",
                                    "meddig": "2017-02-22",
                                    "idotartam": "6",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "50",
                                    "FOGLALAS_PK": "787",
                                    "mettol": "2016-08-16",
                                    "meddig": "2016-08-19",
                                    "idotartam": "3",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "50",
                                    "FOGLALAS_PK": "1063",
                                    "mettol": "2016-09-18",
                                    "meddig": "2016-09-20",
                                    "idotartam": "2",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "50",
                                    "FOGLALAS_PK": "1224",
                                    "mettol": "2016-10-30",
                                    "meddig": "2016-10-31",
                                    "idotartam": "1",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "50",
                                    "FOGLALAS_PK": "1272",
                                    "mettol": "2016-11-10",
                                    "meddig": "2016-11-11",
                                    "idotartam": "1",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "51",
                                    "FOGLALAS_PK": "865",
                                    "mettol": "2016-05-28",
                                    "meddig": "2016-06-04",
                                    "idotartam": "7",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "51",
                                    "FOGLALAS_PK": "811",
                                    "mettol": "2016-08-23",
                                    "meddig": "2016-08-25",
                                    "idotartam": "2",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "51",
                                    "FOGLALAS_PK": "1165",
                                    "mettol": "2016-10-19",
                                    "meddig": "2016-10-24",
                                    "idotartam": "5",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "51",
                                    "FOGLALAS_PK": "1477",
                                    "mettol": "2017-01-28",
                                    "meddig": "2017-02-03",
                                    "idotartam": "6",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "51",
                                    "FOGLALAS_PK": "1550",
                                    "mettol": "2017-02-18",
                                    "meddig": "2017-02-19",
                                    "idotartam": "1",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "52",
                                    "FOGLALAS_PK": "822",
                                    "mettol": "2016-08-24",
                                    "meddig": "2016-08-31",
                                    "idotartam": "7",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "52",
                                    "FOGLALAS_PK": "1202",
                                    "mettol": "2016-10-26",
                                    "meddig": "2016-10-28",
                                    "idotartam": "2",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "52",
                                    "FOGLALAS_PK": "1258",
                                    "mettol": "2016-11-07",
                                    "meddig": "2016-11-12",
                                    "idotartam": "5",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "52",
                                    "FOGLALAS_PK": "1431",
                                    "mettol": "2017-01-10",
                                    "meddig": "2017-01-15",
                                    "idotartam": "5",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "52",
                                    "FOGLALAS_PK": "1534",
                                    "mettol": "2017-02-14",
                                    "meddig": "2017-02-19",
                                    "idotartam": "5",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "53",
                                    "FOGLALAS_PK": "855",
                                    "mettol": "2016-05-24",
                                    "meddig": "2016-05-25",
                                    "idotartam": "1",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "53",
                                    "FOGLALAS_PK": "987",
                                    "mettol": "2016-06-26",
                                    "meddig": "2016-06-30",
                                    "idotartam": "4",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "54",
                                    "FOGLALAS_PK": "622",
                                    "mettol": "2016-05-07",
                                    "meddig": "2016-05-14",
                                    "idotartam": "7",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "54",
                                    "FOGLALAS_PK": "642",
                                    "mettol": "2016-05-13",
                                    "meddig": "2016-05-18",
                                    "idotartam": "5",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "54",
                                    "FOGLALAS_PK": "889",
                                    "mettol": "2016-06-02",
                                    "meddig": "2016-06-04",
                                    "idotartam": "2",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "54",
                                    "FOGLALAS_PK": "668",
                                    "mettol": "2016-07-14",
                                    "meddig": "2016-07-15",
                                    "idotartam": "1",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "54",
                                    "FOGLALAS_PK": "1096",
                                    "mettol": "2016-09-30",
                                    "meddig": "2016-10-04",
                                    "idotartam": "4",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "54",
                                    "FOGLALAS_PK": "1328",
                                    "mettol": "2016-11-28",
                                    "meddig": "2016-12-02",
                                    "idotartam": "4",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "55",
                                    "FOGLALAS_PK": "734",
                                    "mettol": "2016-07-28",
                                    "meddig": "2016-08-03",
                                    "idotartam": "6",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "55",
                                    "FOGLALAS_PK": "1086",
                                    "mettol": "2016-09-28",
                                    "meddig": "2016-10-03",
                                    "idotartam": "5",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "55",
                                    "FOGLALAS_PK": "1163",
                                    "mettol": "2016-10-17",
                                    "meddig": "2016-10-19",
                                    "idotartam": "2",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "55",
                                    "FOGLALAS_PK": "1232",
                                    "mettol": "2016-10-30",
                                    "meddig": "2016-11-06",
                                    "idotartam": "7",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "55",
                                    "FOGLALAS_PK": "1327",
                                    "mettol": "2016-11-28",
                                    "meddig": "2016-12-04",
                                    "idotartam": "6",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "55",
                                    "FOGLALAS_PK": "1386",
                                    "mettol": "2016-12-24",
                                    "meddig": "2016-12-26",
                                    "idotartam": "2",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "55",
                                    "FOGLALAS_PK": "1512",
                                    "mettol": "2017-02-08",
                                    "meddig": "2017-02-09",
                                    "idotartam": "1",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "55",
                                    "FOGLALAS_PK": "1520",
                                    "mettol": "2017-02-12",
                                    "meddig": "2017-02-13",
                                    "idotartam": "1",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "56",
                                    "FOGLALAS_PK": "935",
                                    "mettol": "2016-06-08",
                                    "meddig": "2016-06-12",
                                    "idotartam": "4",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "56",
                                    "FOGLALAS_PK": "838",
                                    "mettol": "2016-08-29",
                                    "meddig": "2016-08-31",
                                    "idotartam": "2",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "57",
                                    "FOGLALAS_PK": "1348",
                                    "mettol": "2016-12-06",
                                    "meddig": "2016-12-07",
                                    "idotartam": "1",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "57",
                                    "FOGLALAS_PK": "1389",
                                    "mettol": "2016-12-25",
                                    "meddig": "2016-12-26",
                                    "idotartam": "1",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "57",
                                    "FOGLALAS_PK": "1466",
                                    "mettol": "2017-01-22",
                                    "meddig": "2017-01-29",
                                    "idotartam": "7",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "57",
                                    "FOGLALAS_PK": "1504",
                                    "mettol": "2017-02-06",
                                    "meddig": "2017-02-10",
                                    "idotartam": "4",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "58",
                                    "FOGLALAS_PK": "883",
                                    "mettol": "2016-05-30",
                                    "meddig": "2016-06-04",
                                    "idotartam": "5",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "58",
                                    "FOGLALAS_PK": "719",
                                    "mettol": "2016-07-27",
                                    "meddig": "2016-07-30",
                                    "idotartam": "3",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "58",
                                    "FOGLALAS_PK": "773",
                                    "mettol": "2016-08-12",
                                    "meddig": "2016-08-14",
                                    "idotartam": "2",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "58",
                                    "FOGLALAS_PK": "1113",
                                    "mettol": "2016-10-01",
                                    "meddig": "2016-10-04",
                                    "idotartam": "3",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "58",
                                    "FOGLALAS_PK": "1186",
                                    "mettol": "2016-10-23",
                                    "meddig": "2016-10-29",
                                    "idotartam": "6",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "58",
                                    "FOGLALAS_PK": "1208",
                                    "mettol": "2016-10-28",
                                    "meddig": "2016-11-03",
                                    "idotartam": "6",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "58",
                                    "FOGLALAS_PK": "1255",
                                    "mettol": "2016-11-06",
                                    "meddig": "2016-11-13",
                                    "idotartam": "7",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "58",
                                    "FOGLALAS_PK": "1261",
                                    "mettol": "2016-11-07",
                                    "meddig": "2016-11-13",
                                    "idotartam": "6",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "58",
                                    "FOGLALAS_PK": "1285",
                                    "mettol": "2016-11-16",
                                    "meddig": "2016-11-23",
                                    "idotartam": "7",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "58",
                                    "FOGLALAS_PK": "1293",
                                    "mettol": "2016-11-19",
                                    "meddig": "2016-11-22",
                                    "idotartam": "3",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "58",
                                    "FOGLALAS_PK": "1307",
                                    "mettol": "2016-11-23",
                                    "meddig": "2016-11-29",
                                    "idotartam": "6",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "58",
                                    "FOGLALAS_PK": "1322",
                                    "mettol": "2016-11-26",
                                    "meddig": "2016-11-29",
                                    "idotartam": "3",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "58",
                                    "FOGLALAS_PK": "1451",
                                    "mettol": "2017-01-17",
                                    "meddig": "2017-01-23",
                                    "idotartam": "6",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "59",
                                    "FOGLALAS_PK": "1080",
                                    "mettol": "2016-09-25",
                                    "meddig": "2016-09-26",
                                    "idotartam": "1",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "59",
                                    "FOGLALAS_PK": "1084",
                                    "mettol": "2016-09-28",
                                    "meddig": "2016-09-30",
                                    "idotartam": "2",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "59",
                                    "FOGLALAS_PK": "1170",
                                    "mettol": "2016-10-20",
                                    "meddig": "2016-10-25",
                                    "idotartam": "5",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "59",
                                    "FOGLALAS_PK": "1191",
                                    "mettol": "2016-10-25",
                                    "meddig": "2016-10-31",
                                    "idotartam": "6",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "59",
                                    "FOGLALAS_PK": "1239",
                                    "mettol": "2016-11-03",
                                    "meddig": "2016-11-05",
                                    "idotartam": "2",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "59",
                                    "FOGLALAS_PK": "1288",
                                    "mettol": "2016-11-17",
                                    "meddig": "2016-11-20",
                                    "idotartam": "3",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "59",
                                    "FOGLALAS_PK": "1573",
                                    "mettol": "2017-02-26",
                                    "meddig": "2017-02-27",
                                    "idotartam": "1",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "60",
                                    "FOGLALAS_PK": "676",
                                    "mettol": "2016-07-16",
                                    "meddig": "2016-07-18",
                                    "idotartam": "2",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "61",
                                    "FOGLALAS_PK": "701",
                                    "mettol": "2016-07-21",
                                    "meddig": "2016-07-23",
                                    "idotartam": "2",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "61",
                                    "FOGLALAS_PK": "756",
                                    "mettol": "2016-08-05",
                                    "meddig": "2016-08-11",
                                    "idotartam": "6",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "61",
                                    "FOGLALAS_PK": "1148",
                                    "mettol": "2016-10-11",
                                    "meddig": "2016-10-14",
                                    "idotartam": "3",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "61",
                                    "FOGLALAS_PK": "1218",
                                    "mettol": "2016-10-29",
                                    "meddig": "2016-10-31",
                                    "idotartam": "2",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "61",
                                    "FOGLALAS_PK": "1496",
                                    "mettol": "2017-02-04",
                                    "meddig": "2017-02-11",
                                    "idotartam": "7",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "62",
                                    "FOGLALAS_PK": "936",
                                    "mettol": "2016-06-08",
                                    "meddig": "2016-06-11",
                                    "idotartam": "3",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "62",
                                    "FOGLALAS_PK": "938",
                                    "mettol": "2016-06-09",
                                    "meddig": "2016-06-10",
                                    "idotartam": "1",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "62",
                                    "FOGLALAS_PK": "702",
                                    "mettol": "2016-07-21",
                                    "meddig": "2016-07-26",
                                    "idotartam": "5",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "62",
                                    "FOGLALAS_PK": "1081",
                                    "mettol": "2016-09-26",
                                    "meddig": "2016-10-03",
                                    "idotartam": "7",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "62",
                                    "FOGLALAS_PK": "1426",
                                    "mettol": "2017-01-09",
                                    "meddig": "2017-01-13",
                                    "idotartam": "4",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "63",
                                    "FOGLALAS_PK": "625",
                                    "mettol": "2016-05-08",
                                    "meddig": "2016-05-11",
                                    "idotartam": "3",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "63",
                                    "FOGLALAS_PK": "891",
                                    "mettol": "2016-06-02",
                                    "meddig": "2016-06-08",
                                    "idotartam": "6",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "63",
                                    "FOGLALAS_PK": "769",
                                    "mettol": "2016-08-12",
                                    "meddig": "2016-08-17",
                                    "idotartam": "5",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "63",
                                    "FOGLALAS_PK": "845",
                                    "mettol": "2016-09-02",
                                    "meddig": "2016-09-03",
                                    "idotartam": "1",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "64",
                                    "FOGLALAS_PK": "875",
                                    "mettol": "2016-05-30",
                                    "meddig": "2016-06-01",
                                    "idotartam": "2",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "64",
                                    "FOGLALAS_PK": "1122",
                                    "mettol": "2016-10-05",
                                    "meddig": "2016-10-09",
                                    "idotartam": "4",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "64",
                                    "FOGLALAS_PK": "1233",
                                    "mettol": "2016-10-31",
                                    "meddig": "2016-11-07",
                                    "idotartam": "7",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "64",
                                    "FOGLALAS_PK": "1446",
                                    "mettol": "2017-01-16",
                                    "meddig": "2017-01-22",
                                    "idotartam": "6",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "64",
                                    "FOGLALAS_PK": "1465",
                                    "mettol": "2017-01-22",
                                    "meddig": "2017-01-26",
                                    "idotartam": "4",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "64",
                                    "FOGLALAS_PK": "1582",
                                    "mettol": "2017-03-02",
                                    "meddig": "2017-03-03",
                                    "idotartam": "1",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "65",
                                    "FOGLALAS_PK": "650",
                                    "mettol": "2016-05-17",
                                    "meddig": "2016-05-23",
                                    "idotartam": "6",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "66",
                                    "FOGLALAS_PK": "950",
                                    "mettol": "2016-06-10",
                                    "meddig": "2016-06-13",
                                    "idotartam": "3",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "66",
                                    "FOGLALAS_PK": "736",
                                    "mettol": "2016-07-29",
                                    "meddig": "2016-08-01",
                                    "idotartam": "3",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "66",
                                    "FOGLALAS_PK": "1234",
                                    "mettol": "2016-11-01",
                                    "meddig": "2016-11-04",
                                    "idotartam": "3",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "66",
                                    "FOGLALAS_PK": "1264",
                                    "mettol": "2016-11-08",
                                    "meddig": "2016-11-12",
                                    "idotartam": "4",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "67",
                                    "FOGLALAS_PK": "638",
                                    "mettol": "2016-05-12",
                                    "meddig": "2016-05-17",
                                    "idotartam": "5",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "67",
                                    "FOGLALAS_PK": "645",
                                    "mettol": "2016-05-14",
                                    "meddig": "2016-05-20",
                                    "idotartam": "6",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "67",
                                    "FOGLALAS_PK": "874",
                                    "mettol": "2016-05-30",
                                    "meddig": "2016-06-05",
                                    "idotartam": "6",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "67",
                                    "FOGLALAS_PK": "1382",
                                    "mettol": "2016-12-22",
                                    "meddig": "2016-12-23",
                                    "idotartam": "1",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "67",
                                    "FOGLALAS_PK": "1580",
                                    "mettol": "2017-03-01",
                                    "meddig": "2017-03-06",
                                    "idotartam": "5",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "67",
                                    "FOGLALAS_PK": "1584",
                                    "mettol": "2017-03-03",
                                    "meddig": "2017-03-04",
                                    "idotartam": "1",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "68",
                                    "FOGLALAS_PK": "563",
                                    "mettol": "2016-04-07",
                                    "meddig": "2016-04-12",
                                    "idotartam": "5",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "68",
                                    "FOGLALAS_PK": "1027",
                                    "mettol": "2016-07-12",
                                    "meddig": "2016-07-19",
                                    "idotartam": "7",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "68",
                                    "FOGLALAS_PK": "1324",
                                    "mettol": "2016-11-27",
                                    "meddig": "2016-12-01",
                                    "idotartam": "4",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "69",
                                    "FOGLALAS_PK": "885",
                                    "mettol": "2016-05-31",
                                    "meddig": "2016-06-01",
                                    "idotartam": "1",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "69",
                                    "FOGLALAS_PK": "1055",
                                    "mettol": "2016-09-15",
                                    "meddig": "2016-09-20",
                                    "idotartam": "5",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "69",
                                    "FOGLALAS_PK": "1225",
                                    "mettol": "2016-10-30",
                                    "meddig": "2016-11-04",
                                    "idotartam": "5",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "69",
                                    "FOGLALAS_PK": "1246",
                                    "mettol": "2016-11-05",
                                    "meddig": "2016-11-12",
                                    "idotartam": "7",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "70",
                                    "FOGLALAS_PK": "585",
                                    "mettol": "2016-04-17",
                                    "meddig": "2016-04-22",
                                    "idotartam": "5",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "70",
                                    "FOGLALAS_PK": "860",
                                    "mettol": "2016-05-27",
                                    "meddig": "2016-05-29",
                                    "idotartam": "2",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "70",
                                    "FOGLALAS_PK": "1006",
                                    "mettol": "2016-07-03",
                                    "meddig": "2016-07-06",
                                    "idotartam": "3",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "70",
                                    "FOGLALAS_PK": "704",
                                    "mettol": "2016-07-22",
                                    "meddig": "2016-07-25",
                                    "idotartam": "3",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "70",
                                    "FOGLALAS_PK": "814",
                                    "mettol": "2016-08-24",
                                    "meddig": "2016-08-27",
                                    "idotartam": "3",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "70",
                                    "FOGLALAS_PK": "1092",
                                    "mettol": "2016-09-30",
                                    "meddig": "2016-10-03",
                                    "idotartam": "3",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "70",
                                    "FOGLALAS_PK": "1126",
                                    "mettol": "2016-10-07",
                                    "meddig": "2016-10-10",
                                    "idotartam": "3",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "70",
                                    "FOGLALAS_PK": "1325",
                                    "mettol": "2016-11-27",
                                    "meddig": "2016-12-04",
                                    "idotartam": "7",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "70",
                                    "FOGLALAS_PK": "1333",
                                    "mettol": "2016-11-30",
                                    "meddig": "2016-12-06",
                                    "idotartam": "6",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "70",
                                    "FOGLALAS_PK": "1365",
                                    "mettol": "2016-12-15",
                                    "meddig": "2016-12-18",
                                    "idotartam": "3",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "70",
                                    "FOGLALAS_PK": "1457",
                                    "mettol": "2017-01-19",
                                    "meddig": "2017-01-26",
                                    "idotartam": "7",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "71",
                                    "FOGLALAS_PK": "1009",
                                    "mettol": "2016-07-04",
                                    "meddig": "2016-07-05",
                                    "idotartam": "1",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "71",
                                    "FOGLALAS_PK": "681",
                                    "mettol": "2016-07-18",
                                    "meddig": "2016-07-21",
                                    "idotartam": "3",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "71",
                                    "FOGLALAS_PK": "712",
                                    "mettol": "2016-07-24",
                                    "meddig": "2016-07-25",
                                    "idotartam": "1",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "72",
                                    "FOGLALAS_PK": "902",
                                    "mettol": "2016-06-04",
                                    "meddig": "2016-06-09",
                                    "idotartam": "5",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "72",
                                    "FOGLALAS_PK": "961",
                                    "mettol": "2016-06-16",
                                    "meddig": "2016-06-22",
                                    "idotartam": "6",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "72",
                                    "FOGLALAS_PK": "1318",
                                    "mettol": "2016-11-25",
                                    "meddig": "2016-11-27",
                                    "idotartam": "2",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "72",
                                    "FOGLALAS_PK": "1396",
                                    "mettol": "2016-12-25",
                                    "meddig": "2016-12-28",
                                    "idotartam": "3",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "73",
                                    "FOGLALAS_PK": "1000",
                                    "mettol": "2016-07-01",
                                    "meddig": "2016-07-05",
                                    "idotartam": "4",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "73",
                                    "FOGLALAS_PK": "714",
                                    "mettol": "2016-07-25",
                                    "meddig": "2016-08-01",
                                    "idotartam": "7",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "73",
                                    "FOGLALAS_PK": "1159",
                                    "mettol": "2016-10-16",
                                    "meddig": "2016-10-21",
                                    "idotartam": "5",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "73",
                                    "FOGLALAS_PK": "1331",
                                    "mettol": "2016-11-29",
                                    "meddig": "2016-12-03",
                                    "idotartam": "4",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "74",
                                    "FOGLALAS_PK": "595",
                                    "mettol": "2016-04-22",
                                    "meddig": "2016-04-29",
                                    "idotartam": "7",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "74",
                                    "FOGLALAS_PK": "877",
                                    "mettol": "2016-05-30",
                                    "meddig": "2016-06-03",
                                    "idotartam": "4",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "74",
                                    "FOGLALAS_PK": "940",
                                    "mettol": "2016-06-09",
                                    "meddig": "2016-06-14",
                                    "idotartam": "5",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "74",
                                    "FOGLALAS_PK": "963",
                                    "mettol": "2016-06-16",
                                    "meddig": "2016-06-17",
                                    "idotartam": "1",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "74",
                                    "FOGLALAS_PK": "797",
                                    "mettol": "2016-08-18",
                                    "meddig": "2016-08-23",
                                    "idotartam": "5",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "74",
                                    "FOGLALAS_PK": "830",
                                    "mettol": "2016-08-28",
                                    "meddig": "2016-08-29",
                                    "idotartam": "1",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "74",
                                    "FOGLALAS_PK": "847",
                                    "mettol": "2016-09-03",
                                    "meddig": "2016-09-06",
                                    "idotartam": "3",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "74",
                                    "FOGLALAS_PK": "1093",
                                    "mettol": "2016-09-30",
                                    "meddig": "2016-10-06",
                                    "idotartam": "6",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "74",
                                    "FOGLALAS_PK": "1179",
                                    "mettol": "2016-10-22",
                                    "meddig": "2016-10-29",
                                    "idotartam": "7",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "75",
                                    "FOGLALAS_PK": "1013",
                                    "mettol": "2016-07-06",
                                    "meddig": "2016-07-11",
                                    "idotartam": "5",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "75",
                                    "FOGLALAS_PK": "1412",
                                    "mettol": "2017-01-01",
                                    "meddig": "2017-01-03",
                                    "idotartam": "2",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "75",
                                    "FOGLALAS_PK": "1458",
                                    "mettol": "2017-01-19",
                                    "meddig": "2017-01-20",
                                    "idotartam": "1",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "76",
                                    "FOGLALAS_PK": "976",
                                    "mettol": "2016-06-22",
                                    "meddig": "2016-06-24",
                                    "idotartam": "2",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "76",
                                    "FOGLALAS_PK": "683",
                                    "mettol": "2016-07-18",
                                    "meddig": "2016-07-25",
                                    "idotartam": "7",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "76",
                                    "FOGLALAS_PK": "1557",
                                    "mettol": "2017-02-21",
                                    "meddig": "2017-02-24",
                                    "idotartam": "3",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "77",
                                    "FOGLALAS_PK": "593",
                                    "mettol": "2016-04-21",
                                    "meddig": "2016-04-24",
                                    "idotartam": "3",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "77",
                                    "FOGLALAS_PK": "982",
                                    "mettol": "2016-06-23",
                                    "meddig": "2016-06-26",
                                    "idotartam": "3",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "77",
                                    "FOGLALAS_PK": "698",
                                    "mettol": "2016-07-20",
                                    "meddig": "2016-07-24",
                                    "idotartam": "4",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "77",
                                    "FOGLALAS_PK": "1104",
                                    "mettol": "2016-10-01",
                                    "meddig": "2016-10-02",
                                    "idotartam": "1",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "77",
                                    "FOGLALAS_PK": "1439",
                                    "mettol": "2017-01-15",
                                    "meddig": "2017-01-21",
                                    "idotartam": "6",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "77",
                                    "FOGLALAS_PK": "1461",
                                    "mettol": "2017-01-22",
                                    "meddig": "2017-01-26",
                                    "idotartam": "4",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "78",
                                    "FOGLALAS_PK": "568",
                                    "mettol": "2016-04-10",
                                    "meddig": "2016-04-11",
                                    "idotartam": "1",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "78",
                                    "FOGLALAS_PK": "646",
                                    "mettol": "2016-05-14",
                                    "meddig": "2016-05-17",
                                    "idotartam": "3",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "78",
                                    "FOGLALAS_PK": "700",
                                    "mettol": "2016-07-20",
                                    "meddig": "2016-07-25",
                                    "idotartam": "5",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "78",
                                    "FOGLALAS_PK": "1268",
                                    "mettol": "2016-11-09",
                                    "meddig": "2016-11-11",
                                    "idotartam": "2",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "78",
                                    "FOGLALAS_PK": "1281",
                                    "mettol": "2016-11-15",
                                    "meddig": "2016-11-18",
                                    "idotartam": "3",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "78",
                                    "FOGLALAS_PK": "1577",
                                    "mettol": "2017-02-27",
                                    "meddig": "2017-03-06",
                                    "idotartam": "7",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "79",
                                    "FOGLALAS_PK": "583",
                                    "mettol": "2016-04-16",
                                    "meddig": "2016-04-22",
                                    "idotartam": "6",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "79",
                                    "FOGLALAS_PK": "1054",
                                    "mettol": "2016-09-15",
                                    "meddig": "2016-09-16",
                                    "idotartam": "1",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "79",
                                    "FOGLALAS_PK": "1229",
                                    "mettol": "2016-10-30",
                                    "meddig": "2016-11-06",
                                    "idotartam": "7",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "79",
                                    "FOGLALAS_PK": "1345",
                                    "mettol": "2016-12-05",
                                    "meddig": "2016-12-08",
                                    "idotartam": "3",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "79",
                                    "FOGLALAS_PK": "1447",
                                    "mettol": "2017-01-16",
                                    "meddig": "2017-01-20",
                                    "idotartam": "4",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "80",
                                    "FOGLALAS_PK": "887",
                                    "mettol": "2016-06-01",
                                    "meddig": "2016-06-07",
                                    "idotartam": "6",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "80",
                                    "FOGLALAS_PK": "929",
                                    "mettol": "2016-06-07",
                                    "meddig": "2016-06-09",
                                    "idotartam": "2",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "80",
                                    "FOGLALAS_PK": "983",
                                    "mettol": "2016-06-23",
                                    "meddig": "2016-06-29",
                                    "idotartam": "6",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "80",
                                    "FOGLALAS_PK": "667",
                                    "mettol": "2016-07-13",
                                    "meddig": "2016-07-19",
                                    "idotartam": "6",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "80",
                                    "FOGLALAS_PK": "1071",
                                    "mettol": "2016-09-20",
                                    "meddig": "2016-09-24",
                                    "idotartam": "4",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "80",
                                    "FOGLALAS_PK": "1279",
                                    "mettol": "2016-11-14",
                                    "meddig": "2016-11-19",
                                    "idotartam": "5",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "80",
                                    "FOGLALAS_PK": "1367",
                                    "mettol": "2016-12-17",
                                    "meddig": "2016-12-20",
                                    "idotartam": "3",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "81",
                                    "FOGLALAS_PK": "1366",
                                    "mettol": "2016-12-16",
                                    "meddig": "2016-12-21",
                                    "idotartam": "5",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "81",
                                    "FOGLALAS_PK": "1443",
                                    "mettol": "2017-01-16",
                                    "meddig": "2017-01-23",
                                    "idotartam": "7",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "81",
                                    "FOGLALAS_PK": "1464",
                                    "mettol": "2017-01-22",
                                    "meddig": "2017-01-29",
                                    "idotartam": "7",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "81",
                                    "FOGLALAS_PK": "1506",
                                    "mettol": "2017-02-06",
                                    "meddig": "2017-02-09",
                                    "idotartam": "3",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "81",
                                    "FOGLALAS_PK": "1562",
                                    "mettol": "2017-02-23",
                                    "meddig": "2017-02-26",
                                    "idotartam": "3",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "82",
                                    "FOGLALAS_PK": "862",
                                    "mettol": "2016-05-27",
                                    "meddig": "2016-05-31",
                                    "idotartam": "4",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "82",
                                    "FOGLALAS_PK": "871",
                                    "mettol": "2016-05-29",
                                    "meddig": "2016-06-03",
                                    "idotartam": "5",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "82",
                                    "FOGLALAS_PK": "997",
                                    "mettol": "2016-07-01",
                                    "meddig": "2016-07-07",
                                    "idotartam": "6",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "82",
                                    "FOGLALAS_PK": "1277",
                                    "mettol": "2016-11-12",
                                    "meddig": "2016-11-17",
                                    "idotartam": "5",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "82",
                                    "FOGLALAS_PK": "1341",
                                    "mettol": "2016-12-04",
                                    "meddig": "2016-12-06",
                                    "idotartam": "2",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "82",
                                    "FOGLALAS_PK": "1406",
                                    "mettol": "2016-12-29",
                                    "meddig": "2016-12-30",
                                    "idotartam": "1",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "83",
                                    "FOGLALAS_PK": "572",
                                    "mettol": "2016-04-10",
                                    "meddig": "2016-04-17",
                                    "idotartam": "7",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "83",
                                    "FOGLALAS_PK": "869",
                                    "mettol": "2016-05-28",
                                    "meddig": "2016-06-03",
                                    "idotartam": "6",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "83",
                                    "FOGLALAS_PK": "878",
                                    "mettol": "2016-05-30",
                                    "meddig": "2016-06-05",
                                    "idotartam": "6",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "83",
                                    "FOGLALAS_PK": "995",
                                    "mettol": "2016-06-30",
                                    "meddig": "2016-07-05",
                                    "idotartam": "5",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "83",
                                    "FOGLALAS_PK": "674",
                                    "mettol": "2016-07-15",
                                    "meddig": "2016-07-19",
                                    "idotartam": "4",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "83",
                                    "FOGLALAS_PK": "798",
                                    "mettol": "2016-08-18",
                                    "meddig": "2016-08-22",
                                    "idotartam": "4",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "83",
                                    "FOGLALAS_PK": "1119",
                                    "mettol": "2016-10-04",
                                    "meddig": "2016-10-10",
                                    "idotartam": "6",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "83",
                                    "FOGLALAS_PK": "1379",
                                    "mettol": "2016-12-19",
                                    "meddig": "2016-12-26",
                                    "idotartam": "7",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "84",
                                    "FOGLALAS_PK": "954",
                                    "mettol": "2016-06-13",
                                    "meddig": "2016-06-18",
                                    "idotartam": "5",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "84",
                                    "FOGLALAS_PK": "819",
                                    "mettol": "2016-08-24",
                                    "meddig": "2016-08-26",
                                    "idotartam": "2",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "84",
                                    "FOGLALAS_PK": "1376",
                                    "mettol": "2016-12-17",
                                    "meddig": "2016-12-22",
                                    "idotartam": "5",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "84",
                                    "FOGLALAS_PK": "1384",
                                    "mettol": "2016-12-22",
                                    "meddig": "2016-12-29",
                                    "idotartam": "7",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "85",
                                    "FOGLALAS_PK": "647",
                                    "mettol": "2016-05-15",
                                    "meddig": "2016-05-18",
                                    "idotartam": "3",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "85",
                                    "FOGLALAS_PK": "1059",
                                    "mettol": "2016-09-17",
                                    "meddig": "2016-09-20",
                                    "idotartam": "3",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "85",
                                    "FOGLALAS_PK": "1320",
                                    "mettol": "2016-11-25",
                                    "meddig": "2016-11-26",
                                    "idotartam": "1",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "85",
                                    "FOGLALAS_PK": "1513",
                                    "mettol": "2017-02-09",
                                    "meddig": "2017-02-16",
                                    "idotartam": "7",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "86",
                                    "FOGLALAS_PK": "859",
                                    "mettol": "2016-05-26",
                                    "meddig": "2016-05-27",
                                    "idotartam": "1",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "86",
                                    "FOGLALAS_PK": "1057",
                                    "mettol": "2016-09-16",
                                    "meddig": "2016-09-21",
                                    "idotartam": "5",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "86",
                                    "FOGLALAS_PK": "1079",
                                    "mettol": "2016-09-24",
                                    "meddig": "2016-09-28",
                                    "idotartam": "4",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "86",
                                    "FOGLALAS_PK": "1108",
                                    "mettol": "2016-10-01",
                                    "meddig": "2016-10-02",
                                    "idotartam": "1",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "86",
                                    "FOGLALAS_PK": "1453",
                                    "mettol": "2017-01-17",
                                    "meddig": "2017-01-18",
                                    "idotartam": "1",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "87",
                                    "FOGLALAS_PK": "558",
                                    "mettol": "2016-04-06",
                                    "meddig": "2016-04-10",
                                    "idotartam": "4",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "87",
                                    "FOGLALAS_PK": "844",
                                    "mettol": "2016-09-02",
                                    "meddig": "2016-09-03",
                                    "idotartam": "1",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "87",
                                    "FOGLALAS_PK": "1103",
                                    "mettol": "2016-10-01",
                                    "meddig": "2016-10-04",
                                    "idotartam": "3",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "87",
                                    "FOGLALAS_PK": "1349",
                                    "mettol": "2016-12-06",
                                    "meddig": "2016-12-11",
                                    "idotartam": "5",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "87",
                                    "FOGLALAS_PK": "1456",
                                    "mettol": "2017-01-19",
                                    "meddig": "2017-01-24",
                                    "idotartam": "5",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "88",
                                    "FOGLALAS_PK": "866",
                                    "mettol": "2016-05-28",
                                    "meddig": "2016-05-30",
                                    "idotartam": "2",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "88",
                                    "FOGLALAS_PK": "757",
                                    "mettol": "2016-08-05",
                                    "meddig": "2016-08-12",
                                    "idotartam": "7",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "88",
                                    "FOGLALAS_PK": "1196",
                                    "mettol": "2016-10-26",
                                    "meddig": "2016-10-29",
                                    "idotartam": "3",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "88",
                                    "FOGLALAS_PK": "1273",
                                    "mettol": "2016-11-10",
                                    "meddig": "2016-11-17",
                                    "idotartam": "7",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "88",
                                    "FOGLALAS_PK": "1300",
                                    "mettol": "2016-11-21",
                                    "meddig": "2016-11-24",
                                    "idotartam": "3",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "88",
                                    "FOGLALAS_PK": "1359",
                                    "mettol": "2016-12-12",
                                    "meddig": "2016-12-14",
                                    "idotartam": "2",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "88",
                                    "FOGLALAS_PK": "1548",
                                    "mettol": "2017-02-18",
                                    "meddig": "2017-02-25",
                                    "idotartam": "7",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "88",
                                    "FOGLALAS_PK": "1575",
                                    "mettol": "2017-02-26",
                                    "meddig": "2017-03-04",
                                    "idotartam": "6",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "89",
                                    "FOGLALAS_PK": "817",
                                    "mettol": "2016-08-24",
                                    "meddig": "2016-08-27",
                                    "idotartam": "3",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "89",
                                    "FOGLALAS_PK": "1037",
                                    "mettol": "2016-09-08",
                                    "meddig": "2016-09-15",
                                    "idotartam": "7",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "89",
                                    "FOGLALAS_PK": "1101",
                                    "mettol": "2016-10-01",
                                    "meddig": "2016-10-06",
                                    "idotartam": "5",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "89",
                                    "FOGLALAS_PK": "1189",
                                    "mettol": "2016-10-24",
                                    "meddig": "2016-10-30",
                                    "idotartam": "6",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "89",
                                    "FOGLALAS_PK": "1253",
                                    "mettol": "2016-11-05",
                                    "meddig": "2016-11-07",
                                    "idotartam": "2",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "89",
                                    "FOGLALAS_PK": "1269",
                                    "mettol": "2016-11-09",
                                    "meddig": "2016-11-11",
                                    "idotartam": "2",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "89",
                                    "FOGLALAS_PK": "1399",
                                    "mettol": "2016-12-26",
                                    "meddig": "2016-12-28",
                                    "idotartam": "2",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "89",
                                    "FOGLALAS_PK": "1521",
                                    "mettol": "2017-02-12",
                                    "meddig": "2017-02-19",
                                    "idotartam": "7",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "90",
                                    "FOGLALAS_PK": "729",
                                    "mettol": "2016-07-28",
                                    "meddig": "2016-07-30",
                                    "idotartam": "2",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "90",
                                    "FOGLALAS_PK": "1174",
                                    "mettol": "2016-10-21",
                                    "meddig": "2016-10-28",
                                    "idotartam": "7",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "90",
                                    "FOGLALAS_PK": "1299",
                                    "mettol": "2016-11-21",
                                    "meddig": "2016-11-27",
                                    "idotartam": "6",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "90",
                                    "FOGLALAS_PK": "1405",
                                    "mettol": "2016-12-29",
                                    "meddig": "2017-01-03",
                                    "idotartam": "5",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "91",
                                    "FOGLALAS_PK": "636",
                                    "mettol": "2016-05-10",
                                    "meddig": "2016-05-16",
                                    "idotartam": "6",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "91",
                                    "FOGLALAS_PK": "732",
                                    "mettol": "2016-07-28",
                                    "meddig": "2016-08-01",
                                    "idotartam": "4",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "91",
                                    "FOGLALAS_PK": "1213",
                                    "mettol": "2016-10-28",
                                    "meddig": "2016-10-31",
                                    "idotartam": "3",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "91",
                                    "FOGLALAS_PK": "1397",
                                    "mettol": "2016-12-25",
                                    "meddig": "2016-12-29",
                                    "idotartam": "4",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "92",
                                    "FOGLALAS_PK": "942",
                                    "mettol": "2016-06-10",
                                    "meddig": "2016-06-16",
                                    "idotartam": "6",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "92",
                                    "FOGLALAS_PK": "1016",
                                    "mettol": "2016-07-07",
                                    "meddig": "2016-07-09",
                                    "idotartam": "2",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "92",
                                    "FOGLALAS_PK": "809",
                                    "mettol": "2016-08-23",
                                    "meddig": "2016-08-26",
                                    "idotartam": "3",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "92",
                                    "FOGLALAS_PK": "841",
                                    "mettol": "2016-08-31",
                                    "meddig": "2016-09-06",
                                    "idotartam": "6",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "92",
                                    "FOGLALAS_PK": "1527",
                                    "mettol": "2017-02-13",
                                    "meddig": "2017-02-15",
                                    "idotartam": "2",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "92",
                                    "FOGLALAS_PK": "1555",
                                    "mettol": "2017-02-20",
                                    "meddig": "2017-02-24",
                                    "idotartam": "4",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "93",
                                    "FOGLALAS_PK": "741",
                                    "mettol": "2016-07-30",
                                    "meddig": "2016-08-06",
                                    "idotartam": "7",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "93",
                                    "FOGLALAS_PK": "1169",
                                    "mettol": "2016-10-20",
                                    "meddig": "2016-10-24",
                                    "idotartam": "4",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "93",
                                    "FOGLALAS_PK": "1217",
                                    "mettol": "2016-10-29",
                                    "meddig": "2016-10-30",
                                    "idotartam": "1",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "93",
                                    "FOGLALAS_PK": "1355",
                                    "mettol": "2016-12-08",
                                    "meddig": "2016-12-10",
                                    "idotartam": "2",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "93",
                                    "FOGLALAS_PK": "1391",
                                    "mettol": "2016-12-25",
                                    "meddig": "2016-12-29",
                                    "idotartam": "4",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "94",
                                    "FOGLALAS_PK": "616",
                                    "mettol": "2016-05-02",
                                    "meddig": "2016-05-06",
                                    "idotartam": "4",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "94",
                                    "FOGLALAS_PK": "975",
                                    "mettol": "2016-06-21",
                                    "meddig": "2016-06-26",
                                    "idotartam": "5",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "94",
                                    "FOGLALAS_PK": "665",
                                    "mettol": "2016-07-13",
                                    "meddig": "2016-07-20",
                                    "idotartam": "7",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "94",
                                    "FOGLALAS_PK": "727",
                                    "mettol": "2016-07-27",
                                    "meddig": "2016-07-30",
                                    "idotartam": "3",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "94",
                                    "FOGLALAS_PK": "1241",
                                    "mettol": "2016-11-03",
                                    "meddig": "2016-11-10",
                                    "idotartam": "7",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "94",
                                    "FOGLALAS_PK": "1305",
                                    "mettol": "2016-11-22",
                                    "meddig": "2016-11-24",
                                    "idotartam": "2",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "94",
                                    "FOGLALAS_PK": "1312",
                                    "mettol": "2016-11-23",
                                    "meddig": "2016-11-26",
                                    "idotartam": "3",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "94",
                                    "FOGLALAS_PK": "1368",
                                    "mettol": "2016-12-17",
                                    "meddig": "2016-12-18",
                                    "idotartam": "1",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "94",
                                    "FOGLALAS_PK": "1518",
                                    "mettol": "2017-02-12",
                                    "meddig": "2017-02-14",
                                    "idotartam": "2",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "94",
                                    "FOGLALAS_PK": "1564",
                                    "mettol": "2017-02-23",
                                    "meddig": "2017-03-02",
                                    "idotartam": "7",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "95",
                                    "FOGLALAS_PK": "656",
                                    "mettol": "2016-05-19",
                                    "meddig": "2016-05-26",
                                    "idotartam": "7",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "95",
                                    "FOGLALAS_PK": "1048",
                                    "mettol": "2016-09-13",
                                    "meddig": "2016-09-16",
                                    "idotartam": "3",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "95",
                                    "FOGLALAS_PK": "1097",
                                    "mettol": "2016-10-01",
                                    "meddig": "2016-10-05",
                                    "idotartam": "4",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "95",
                                    "FOGLALAS_PK": "1543",
                                    "mettol": "2017-02-16",
                                    "meddig": "2017-02-23",
                                    "idotartam": "7",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "96",
                                    "FOGLALAS_PK": "607",
                                    "mettol": "2016-04-28",
                                    "meddig": "2016-05-02",
                                    "idotartam": "4",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "96",
                                    "FOGLALAS_PK": "623",
                                    "mettol": "2016-05-08",
                                    "meddig": "2016-05-15",
                                    "idotartam": "7",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "96",
                                    "FOGLALAS_PK": "671",
                                    "mettol": "2016-07-14",
                                    "meddig": "2016-07-18",
                                    "idotartam": "4",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "96",
                                    "FOGLALAS_PK": "780",
                                    "mettol": "2016-08-15",
                                    "meddig": "2016-08-16",
                                    "idotartam": "1",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "96",
                                    "FOGLALAS_PK": "1378",
                                    "mettol": "2016-12-18",
                                    "meddig": "2016-12-21",
                                    "idotartam": "3",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "96",
                                    "FOGLALAS_PK": "1438",
                                    "mettol": "2017-01-14",
                                    "meddig": "2017-01-16",
                                    "idotartam": "2",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "96",
                                    "FOGLALAS_PK": "1569",
                                    "mettol": "2017-02-24",
                                    "meddig": "2017-03-03",
                                    "idotartam": "7",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "97",
                                    "FOGLALAS_PK": "635",
                                    "mettol": "2016-05-10",
                                    "meddig": "2016-05-13",
                                    "idotartam": "3",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "97",
                                    "FOGLALAS_PK": "726",
                                    "mettol": "2016-07-27",
                                    "meddig": "2016-07-31",
                                    "idotartam": "4",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "97",
                                    "FOGLALAS_PK": "718",
                                    "mettol": "2016-07-27",
                                    "meddig": "2016-08-03",
                                    "idotartam": "7",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "97",
                                    "FOGLALAS_PK": "836",
                                    "mettol": "2016-08-29",
                                    "meddig": "2016-08-31",
                                    "idotartam": "2",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "97",
                                    "FOGLALAS_PK": "1395",
                                    "mettol": "2016-12-25",
                                    "meddig": "2016-12-26",
                                    "idotartam": "1",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "97",
                                    "FOGLALAS_PK": "1417",
                                    "mettol": "2017-01-03",
                                    "meddig": "2017-01-10",
                                    "idotartam": "7",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "97",
                                    "FOGLALAS_PK": "1528",
                                    "mettol": "2017-02-13",
                                    "meddig": "2017-02-15",
                                    "idotartam": "2",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "98",
                                    "FOGLALAS_PK": "631",
                                    "mettol": "2016-05-09",
                                    "meddig": "2016-05-15",
                                    "idotartam": "6",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "98",
                                    "FOGLALAS_PK": "884",
                                    "mettol": "2016-05-30",
                                    "meddig": "2016-06-04",
                                    "idotartam": "5",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "98",
                                    "FOGLALAS_PK": "1050",
                                    "mettol": "2016-09-13",
                                    "meddig": "2016-09-19",
                                    "idotartam": "6",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "98",
                                    "FOGLALAS_PK": "1402",
                                    "mettol": "2016-12-28",
                                    "meddig": "2016-12-30",
                                    "idotartam": "2",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "99",
                                    "FOGLALAS_PK": "632",
                                    "mettol": "2016-05-09",
                                    "meddig": "2016-05-10",
                                    "idotartam": "1",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "99",
                                    "FOGLALAS_PK": "691",
                                    "mettol": "2016-07-20",
                                    "meddig": "2016-07-25",
                                    "idotartam": "5",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "99",
                                    "FOGLALAS_PK": "1072",
                                    "mettol": "2016-09-20",
                                    "meddig": "2016-09-21",
                                    "idotartam": "1",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "99",
                                    "FOGLALAS_PK": "1408",
                                    "mettol": "2016-12-31",
                                    "meddig": "2017-01-01",
                                    "idotartam": "1",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "99",
                                    "FOGLALAS_PK": "1486",
                                    "mettol": "2017-01-31",
                                    "meddig": "2017-02-05",
                                    "idotartam": "5",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "100",
                                    "FOGLALAS_PK": "597",
                                    "mettol": "2016-04-23",
                                    "meddig": "2016-04-24",
                                    "idotartam": "1",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "100",
                                    "FOGLALAS_PK": "637",
                                    "mettol": "2016-05-11",
                                    "meddig": "2016-05-16",
                                    "idotartam": "5",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "100",
                                    "FOGLALAS_PK": "1315",
                                    "mettol": "2016-11-24",
                                    "meddig": "2016-11-29",
                                    "idotartam": "5",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "100",
                                    "FOGLALAS_PK": "1482",
                                    "mettol": "2017-01-29",
                                    "meddig": "2017-02-05",
                                    "idotartam": "7",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "101",
                                    "FOGLALAS_PK": "715",
                                    "mettol": "2016-07-25",
                                    "meddig": "2016-07-28",
                                    "idotartam": "3",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "101",
                                    "FOGLALAS_PK": "1332",
                                    "mettol": "2016-11-29",
                                    "meddig": "2016-12-05",
                                    "idotartam": "6",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "101",
                                    "FOGLALAS_PK": "1516",
                                    "mettol": "2017-02-10",
                                    "meddig": "2017-02-14",
                                    "idotartam": "4",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "102",
                                    "FOGLALAS_PK": "689",
                                    "mettol": "2016-07-19",
                                    "meddig": "2016-07-24",
                                    "idotartam": "5",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "102",
                                    "FOGLALAS_PK": "1343",
                                    "mettol": "2016-12-05",
                                    "meddig": "2016-12-07",
                                    "idotartam": "2",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "103",
                                    "FOGLALAS_PK": "972",
                                    "mettol": "2016-06-19",
                                    "meddig": "2016-06-21",
                                    "idotartam": "2",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "103",
                                    "FOGLALAS_PK": "992",
                                    "mettol": "2016-06-29",
                                    "meddig": "2016-07-06",
                                    "idotartam": "7",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "103",
                                    "FOGLALAS_PK": "1398",
                                    "mettol": "2016-12-26",
                                    "meddig": "2016-12-27",
                                    "idotartam": "1",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "103",
                                    "FOGLALAS_PK": "1485",
                                    "mettol": "2017-01-30",
                                    "meddig": "2017-02-03",
                                    "idotartam": "4",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "104",
                                    "FOGLALAS_PK": "837",
                                    "mettol": "2016-08-29",
                                    "meddig": "2016-09-02",
                                    "idotartam": "4",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "104",
                                    "FOGLALAS_PK": "1180",
                                    "mettol": "2016-10-22",
                                    "meddig": "2016-10-23",
                                    "idotartam": "1",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "104",
                                    "FOGLALAS_PK": "1522",
                                    "mettol": "2017-02-12",
                                    "meddig": "2017-02-14",
                                    "idotartam": "2",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "104",
                                    "FOGLALAS_PK": "1532",
                                    "mettol": "2017-02-14",
                                    "meddig": "2017-02-17",
                                    "idotartam": "3",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "105",
                                    "FOGLALAS_PK": "618",
                                    "mettol": "2016-05-03",
                                    "meddig": "2016-05-04",
                                    "idotartam": "1",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "105",
                                    "FOGLALAS_PK": "1525",
                                    "mettol": "2017-02-12",
                                    "meddig": "2017-02-17",
                                    "idotartam": "5",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "106",
                                    "FOGLALAS_PK": "610",
                                    "mettol": "2016-04-30",
                                    "meddig": "2016-05-03",
                                    "idotartam": "3",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "106",
                                    "FOGLALAS_PK": "708",
                                    "mettol": "2016-07-23",
                                    "meddig": "2016-07-30",
                                    "idotartam": "7",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "106",
                                    "FOGLALAS_PK": "1228",
                                    "mettol": "2016-10-30",
                                    "meddig": "2016-11-06",
                                    "idotartam": "7",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "106",
                                    "FOGLALAS_PK": "1271",
                                    "mettol": "2016-11-10",
                                    "meddig": "2016-11-15",
                                    "idotartam": "5",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "106",
                                    "FOGLALAS_PK": "1372",
                                    "mettol": "2016-12-17",
                                    "meddig": "2016-12-24",
                                    "idotartam": "7",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "106",
                                    "FOGLALAS_PK": "1510",
                                    "mettol": "2017-02-08",
                                    "meddig": "2017-02-14",
                                    "idotartam": "6",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "107",
                                    "FOGLALAS_PK": "586",
                                    "mettol": "2016-04-18",
                                    "meddig": "2016-04-24",
                                    "idotartam": "6",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "107",
                                    "FOGLALAS_PK": "1250",
                                    "mettol": "2016-11-05",
                                    "meddig": "2016-11-09",
                                    "idotartam": "4",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "107",
                                    "FOGLALAS_PK": "1354",
                                    "mettol": "2016-12-07",
                                    "meddig": "2016-12-08",
                                    "idotartam": "1",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "107",
                                    "FOGLALAS_PK": "1452",
                                    "mettol": "2017-01-17",
                                    "meddig": "2017-01-23",
                                    "idotartam": "6",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "107",
                                    "FOGLALAS_PK": "1494",
                                    "mettol": "2017-02-04",
                                    "meddig": "2017-02-06",
                                    "idotartam": "2",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "108",
                                    "FOGLALAS_PK": "1102",
                                    "mettol": "2016-10-01",
                                    "meddig": "2016-10-02",
                                    "idotartam": "1",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "108",
                                    "FOGLALAS_PK": "1392",
                                    "mettol": "2016-12-25",
                                    "meddig": "2016-12-31",
                                    "idotartam": "6",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "109",
                                    "FOGLALAS_PK": "614",
                                    "mettol": "2016-05-01",
                                    "meddig": "2016-05-05",
                                    "idotartam": "4",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "109",
                                    "FOGLALAS_PK": "621",
                                    "mettol": "2016-05-06",
                                    "meddig": "2016-05-13",
                                    "idotartam": "7",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "109",
                                    "FOGLALAS_PK": "654",
                                    "mettol": "2016-05-18",
                                    "meddig": "2016-05-23",
                                    "idotartam": "5",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "109",
                                    "FOGLALAS_PK": "810",
                                    "mettol": "2016-08-23",
                                    "meddig": "2016-08-25",
                                    "idotartam": "2",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "109",
                                    "FOGLALAS_PK": "1083",
                                    "mettol": "2016-09-27",
                                    "meddig": "2016-09-28",
                                    "idotartam": "1",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "109",
                                    "FOGLALAS_PK": "1298",
                                    "mettol": "2016-11-20",
                                    "meddig": "2016-11-24",
                                    "idotartam": "4",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "109",
                                    "FOGLALAS_PK": "1560",
                                    "mettol": "2017-02-23",
                                    "meddig": "2017-02-24",
                                    "idotartam": "1",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "110",
                                    "FOGLALAS_PK": "931",
                                    "mettol": "2016-06-07",
                                    "meddig": "2016-06-12",
                                    "idotartam": "5",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "110",
                                    "FOGLALAS_PK": "964",
                                    "mettol": "2016-06-16",
                                    "meddig": "2016-06-22",
                                    "idotartam": "6",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "110",
                                    "FOGLALAS_PK": "685",
                                    "mettol": "2016-07-18",
                                    "meddig": "2016-07-19",
                                    "idotartam": "1",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "110",
                                    "FOGLALAS_PK": "1041",
                                    "mettol": "2016-09-10",
                                    "meddig": "2016-09-13",
                                    "idotartam": "3",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "110",
                                    "FOGLALAS_PK": "1109",
                                    "mettol": "2016-10-01",
                                    "meddig": "2016-10-06",
                                    "idotartam": "5",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "110",
                                    "FOGLALAS_PK": "1162",
                                    "mettol": "2016-10-17",
                                    "meddig": "2016-10-19",
                                    "idotartam": "2",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "110",
                                    "FOGLALAS_PK": "1424",
                                    "mettol": "2017-01-07",
                                    "meddig": "2017-01-08",
                                    "idotartam": "1",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "110",
                                    "FOGLALAS_PK": "1489",
                                    "mettol": "2017-02-02",
                                    "meddig": "2017-02-08",
                                    "idotartam": "6",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "111",
                                    "FOGLALAS_PK": "605",
                                    "mettol": "2016-04-27",
                                    "meddig": "2016-05-04",
                                    "idotartam": "7",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "111",
                                    "FOGLALAS_PK": "959",
                                    "mettol": "2016-06-14",
                                    "meddig": "2016-06-21",
                                    "idotartam": "7",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "111",
                                    "FOGLALAS_PK": "786",
                                    "mettol": "2016-08-16",
                                    "meddig": "2016-08-20",
                                    "idotartam": "4",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "111",
                                    "FOGLALAS_PK": "1296",
                                    "mettol": "2016-11-19",
                                    "meddig": "2016-11-22",
                                    "idotartam": "3",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "111",
                                    "FOGLALAS_PK": "1353",
                                    "mettol": "2016-12-07",
                                    "meddig": "2016-12-12",
                                    "idotartam": "5",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "112",
                                    "FOGLALAS_PK": "921",
                                    "mettol": "2016-06-06",
                                    "meddig": "2016-06-07",
                                    "idotartam": "1",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "112",
                                    "FOGLALAS_PK": "776",
                                    "mettol": "2016-08-14",
                                    "meddig": "2016-08-18",
                                    "idotartam": "4",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "112",
                                    "FOGLALAS_PK": "801",
                                    "mettol": "2016-08-20",
                                    "meddig": "2016-08-25",
                                    "idotartam": "5",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "112",
                                    "FOGLALAS_PK": "1124",
                                    "mettol": "2016-10-06",
                                    "meddig": "2016-10-12",
                                    "idotartam": "6",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "112",
                                    "FOGLALAS_PK": "1530",
                                    "mettol": "2017-02-13",
                                    "meddig": "2017-02-19",
                                    "idotartam": "6",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "113",
                                    "FOGLALAS_PK": "1029",
                                    "mettol": "2016-09-05",
                                    "meddig": "2016-09-10",
                                    "idotartam": "5",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "113",
                                    "FOGLALAS_PK": "1085",
                                    "mettol": "2016-09-28",
                                    "meddig": "2016-10-02",
                                    "idotartam": "4",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "113",
                                    "FOGLALAS_PK": "1263",
                                    "mettol": "2016-11-08",
                                    "meddig": "2016-11-09",
                                    "idotartam": "1",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "113",
                                    "FOGLALAS_PK": "1495",
                                    "mettol": "2017-02-04",
                                    "meddig": "2017-02-11",
                                    "idotartam": "7",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "113",
                                    "FOGLALAS_PK": "1499",
                                    "mettol": "2017-02-05",
                                    "meddig": "2017-02-07",
                                    "idotartam": "2",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "114",
                                    "FOGLALAS_PK": "966",
                                    "mettol": "2016-06-16",
                                    "meddig": "2016-06-22",
                                    "idotartam": "6",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "114",
                                    "FOGLALAS_PK": "737",
                                    "mettol": "2016-07-29",
                                    "meddig": "2016-07-31",
                                    "idotartam": "2",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "114",
                                    "FOGLALAS_PK": "827",
                                    "mettol": "2016-08-26",
                                    "meddig": "2016-09-02",
                                    "idotartam": "7",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "114",
                                    "FOGLALAS_PK": "1540",
                                    "mettol": "2017-02-16",
                                    "meddig": "2017-02-19",
                                    "idotartam": "3",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "115",
                                    "FOGLALAS_PK": "596",
                                    "mettol": "2016-04-23",
                                    "meddig": "2016-04-30",
                                    "idotartam": "7",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "115",
                                    "FOGLALAS_PK": "943",
                                    "mettol": "2016-06-10",
                                    "meddig": "2016-06-17",
                                    "idotartam": "7",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "115",
                                    "FOGLALAS_PK": "1121",
                                    "mettol": "2016-10-04",
                                    "meddig": "2016-10-11",
                                    "idotartam": "7",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "115",
                                    "FOGLALAS_PK": "1154",
                                    "mettol": "2016-10-15",
                                    "meddig": "2016-10-19",
                                    "idotartam": "4",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "115",
                                    "FOGLALAS_PK": "1352",
                                    "mettol": "2016-12-07",
                                    "meddig": "2016-12-10",
                                    "idotartam": "3",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "115",
                                    "FOGLALAS_PK": "1554",
                                    "mettol": "2017-02-20",
                                    "meddig": "2017-02-23",
                                    "idotartam": "3",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "115",
                                    "FOGLALAS_PK": "1566",
                                    "mettol": "2017-02-24",
                                    "meddig": "2017-02-25",
                                    "idotartam": "1",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "116",
                                    "FOGLALAS_PK": "1455",
                                    "mettol": "2017-01-18",
                                    "meddig": "2017-01-20",
                                    "idotartam": "2",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "116",
                                    "FOGLALAS_PK": "1501",
                                    "mettol": "2017-02-05",
                                    "meddig": "2017-02-09",
                                    "idotartam": "4",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "117",
                                    "FOGLALAS_PK": "612",
                                    "mettol": "2016-05-01",
                                    "meddig": "2016-05-03",
                                    "idotartam": "2",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "117",
                                    "FOGLALAS_PK": "617",
                                    "mettol": "2016-05-02",
                                    "meddig": "2016-05-05",
                                    "idotartam": "3",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "117",
                                    "FOGLALAS_PK": "953",
                                    "mettol": "2016-06-12",
                                    "meddig": "2016-06-17",
                                    "idotartam": "5",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "117",
                                    "FOGLALAS_PK": "962",
                                    "mettol": "2016-06-16",
                                    "meddig": "2016-06-20",
                                    "idotartam": "4",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "117",
                                    "FOGLALAS_PK": "1002",
                                    "mettol": "2016-07-03",
                                    "meddig": "2016-07-04",
                                    "idotartam": "1",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "117",
                                    "FOGLALAS_PK": "1192",
                                    "mettol": "2016-10-26",
                                    "meddig": "2016-10-28",
                                    "idotartam": "2",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "117",
                                    "FOGLALAS_PK": "1247",
                                    "mettol": "2016-11-05",
                                    "meddig": "2016-11-08",
                                    "idotartam": "3",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "117",
                                    "FOGLALAS_PK": "1468",
                                    "mettol": "2017-01-23",
                                    "meddig": "2017-01-30",
                                    "idotartam": "7",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "118",
                                    "FOGLALAS_PK": "864",
                                    "mettol": "2016-05-28",
                                    "meddig": "2016-06-03",
                                    "idotartam": "6",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "118",
                                    "FOGLALAS_PK": "994",
                                    "mettol": "2016-06-30",
                                    "meddig": "2016-07-07",
                                    "idotartam": "7",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "118",
                                    "FOGLALAS_PK": "996",
                                    "mettol": "2016-07-01",
                                    "meddig": "2016-07-04",
                                    "idotartam": "3",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "118",
                                    "FOGLALAS_PK": "716",
                                    "mettol": "2016-07-26",
                                    "meddig": "2016-07-27",
                                    "idotartam": "1",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "118",
                                    "FOGLALAS_PK": "1374",
                                    "mettol": "2016-12-17",
                                    "meddig": "2016-12-22",
                                    "idotartam": "5",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "118",
                                    "FOGLALAS_PK": "1472",
                                    "mettol": "2017-01-24",
                                    "meddig": "2017-01-30",
                                    "idotartam": "6",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "118",
                                    "FOGLALAS_PK": "1481",
                                    "mettol": "2017-01-29",
                                    "meddig": "2017-02-01",
                                    "idotartam": "3",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "119",
                                    "FOGLALAS_PK": "1026",
                                    "mettol": "2016-07-12",
                                    "meddig": "2016-07-15",
                                    "idotartam": "3",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "119",
                                    "FOGLALAS_PK": "706",
                                    "mettol": "2016-07-22",
                                    "meddig": "2016-07-24",
                                    "idotartam": "2",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "119",
                                    "FOGLALAS_PK": "722",
                                    "mettol": "2016-07-27",
                                    "meddig": "2016-07-28",
                                    "idotartam": "1",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "119",
                                    "FOGLALAS_PK": "1413",
                                    "mettol": "2017-01-02",
                                    "meddig": "2017-01-05",
                                    "idotartam": "3",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "119",
                                    "FOGLALAS_PK": "1488",
                                    "mettol": "2017-02-01",
                                    "meddig": "2017-02-04",
                                    "idotartam": "3",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "120",
                                    "FOGLALAS_PK": "998",
                                    "mettol": "2016-07-01",
                                    "meddig": "2016-07-04",
                                    "idotartam": "3",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "120",
                                    "FOGLALAS_PK": "762",
                                    "mettol": "2016-08-07",
                                    "meddig": "2016-08-10",
                                    "idotartam": "3",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "120",
                                    "FOGLALAS_PK": "1089",
                                    "mettol": "2016-09-30",
                                    "meddig": "2016-10-06",
                                    "idotartam": "6",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "120",
                                    "FOGLALAS_PK": "1339",
                                    "mettol": "2016-12-03",
                                    "meddig": "2016-12-09",
                                    "idotartam": "6",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "120",
                                    "FOGLALAS_PK": "1483",
                                    "mettol": "2017-01-30",
                                    "meddig": "2017-01-31",
                                    "idotartam": "1",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "120",
                                    "FOGLALAS_PK": "1493",
                                    "mettol": "2017-02-04",
                                    "meddig": "2017-02-11",
                                    "idotartam": "7",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "121",
                                    "FOGLALAS_PK": "858",
                                    "mettol": "2016-05-25",
                                    "meddig": "2016-05-30",
                                    "idotartam": "5",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "121",
                                    "FOGLALAS_PK": "735",
                                    "mettol": "2016-07-28",
                                    "meddig": "2016-08-03",
                                    "idotartam": "6",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "121",
                                    "FOGLALAS_PK": "739",
                                    "mettol": "2016-07-30",
                                    "meddig": "2016-08-05",
                                    "idotartam": "6",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "121",
                                    "FOGLALAS_PK": "1049",
                                    "mettol": "2016-09-13",
                                    "meddig": "2016-09-16",
                                    "idotartam": "3",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "121",
                                    "FOGLALAS_PK": "1128",
                                    "mettol": "2016-10-08",
                                    "meddig": "2016-10-12",
                                    "idotartam": "4",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "121",
                                    "FOGLALAS_PK": "1215",
                                    "mettol": "2016-10-29",
                                    "meddig": "2016-11-02",
                                    "idotartam": "4",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "121",
                                    "FOGLALAS_PK": "1373",
                                    "mettol": "2016-12-17",
                                    "meddig": "2016-12-22",
                                    "idotartam": "5",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "121",
                                    "FOGLALAS_PK": "1393",
                                    "mettol": "2016-12-25",
                                    "meddig": "2016-12-31",
                                    "idotartam": "6",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "122",
                                    "FOGLALAS_PK": "1007",
                                    "mettol": "2016-07-04",
                                    "meddig": "2016-07-06",
                                    "idotartam": "2",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "122",
                                    "FOGLALAS_PK": "1036",
                                    "mettol": "2016-09-08",
                                    "meddig": "2016-09-10",
                                    "idotartam": "2",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "122",
                                    "FOGLALAS_PK": "1062",
                                    "mettol": "2016-09-17",
                                    "meddig": "2016-09-20",
                                    "idotartam": "3",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "122",
                                    "FOGLALAS_PK": "1166",
                                    "mettol": "2016-10-19",
                                    "meddig": "2016-10-23",
                                    "idotartam": "4",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "122",
                                    "FOGLALAS_PK": "1209",
                                    "mettol": "2016-10-28",
                                    "meddig": "2016-10-29",
                                    "idotartam": "1",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "122",
                                    "FOGLALAS_PK": "1245",
                                    "mettol": "2016-11-04",
                                    "meddig": "2016-11-06",
                                    "idotartam": "2",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "122",
                                    "FOGLALAS_PK": "1337",
                                    "mettol": "2016-12-02",
                                    "meddig": "2016-12-04",
                                    "idotartam": "2",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "122",
                                    "FOGLALAS_PK": "1385",
                                    "mettol": "2016-12-23",
                                    "meddig": "2016-12-28",
                                    "idotartam": "5",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "122",
                                    "FOGLALAS_PK": "1440",
                                    "mettol": "2017-01-15",
                                    "meddig": "2017-01-18",
                                    "idotartam": "3",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "123",
                                    "FOGLALAS_PK": "587",
                                    "mettol": "2016-04-19",
                                    "meddig": "2016-04-26",
                                    "idotartam": "7",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "123",
                                    "FOGLALAS_PK": "923",
                                    "mettol": "2016-06-07",
                                    "meddig": "2016-06-11",
                                    "idotartam": "4",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "123",
                                    "FOGLALAS_PK": "967",
                                    "mettol": "2016-06-16",
                                    "meddig": "2016-06-21",
                                    "idotartam": "5",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "123",
                                    "FOGLALAS_PK": "1223",
                                    "mettol": "2016-10-30",
                                    "meddig": "2016-10-31",
                                    "idotartam": "1",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "123",
                                    "FOGLALAS_PK": "1282",
                                    "mettol": "2016-11-15",
                                    "meddig": "2016-11-21",
                                    "idotartam": "6",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "124",
                                    "FOGLALAS_PK": "861",
                                    "mettol": "2016-05-27",
                                    "meddig": "2016-05-28",
                                    "idotartam": "1",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "124",
                                    "FOGLALAS_PK": "1210",
                                    "mettol": "2016-10-28",
                                    "meddig": "2016-11-01",
                                    "idotartam": "4",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "124",
                                    "FOGLALAS_PK": "1330",
                                    "mettol": "2016-11-29",
                                    "meddig": "2016-12-06",
                                    "idotartam": "7",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "124",
                                    "FOGLALAS_PK": "1403",
                                    "mettol": "2016-12-29",
                                    "meddig": "2017-01-04",
                                    "idotartam": "6",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "124",
                                    "FOGLALAS_PK": "1419",
                                    "mettol": "2017-01-05",
                                    "meddig": "2017-01-08",
                                    "idotartam": "3",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "124",
                                    "FOGLALAS_PK": "1531",
                                    "mettol": "2017-02-13",
                                    "meddig": "2017-02-19",
                                    "idotartam": "6",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "125",
                                    "FOGLALAS_PK": "576",
                                    "mettol": "2016-04-11",
                                    "meddig": "2016-04-12",
                                    "idotartam": "1",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "126",
                                    "FOGLALAS_PK": "754",
                                    "mettol": "2016-08-04",
                                    "meddig": "2016-08-08",
                                    "idotartam": "4",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "126",
                                    "FOGLALAS_PK": "806",
                                    "mettol": "2016-08-21",
                                    "meddig": "2016-08-27",
                                    "idotartam": "6",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "126",
                                    "FOGLALAS_PK": "1134",
                                    "mettol": "2016-10-08",
                                    "meddig": "2016-10-09",
                                    "idotartam": "1",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "126",
                                    "FOGLALAS_PK": "1364",
                                    "mettol": "2016-12-15",
                                    "meddig": "2016-12-21",
                                    "idotartam": "6",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "126",
                                    "FOGLALAS_PK": "1428",
                                    "mettol": "2017-01-09",
                                    "meddig": "2017-01-16",
                                    "idotartam": "7",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "126",
                                    "FOGLALAS_PK": "1500",
                                    "mettol": "2017-02-05",
                                    "meddig": "2017-02-09",
                                    "idotartam": "4",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "127",
                                    "FOGLALAS_PK": "643",
                                    "mettol": "2016-05-14",
                                    "meddig": "2016-05-16",
                                    "idotartam": "2",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "127",
                                    "FOGLALAS_PK": "853",
                                    "mettol": "2016-05-24",
                                    "meddig": "2016-05-29",
                                    "idotartam": "5",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "127",
                                    "FOGLALAS_PK": "879",
                                    "mettol": "2016-05-30",
                                    "meddig": "2016-06-01",
                                    "idotartam": "2",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "127",
                                    "FOGLALAS_PK": "1034",
                                    "mettol": "2016-09-06",
                                    "meddig": "2016-09-12",
                                    "idotartam": "6",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "127",
                                    "FOGLALAS_PK": "1226",
                                    "mettol": "2016-10-30",
                                    "meddig": "2016-11-04",
                                    "idotartam": "5",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "127",
                                    "FOGLALAS_PK": "1286",
                                    "mettol": "2016-11-16",
                                    "meddig": "2016-11-17",
                                    "idotartam": "1",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "127",
                                    "FOGLALAS_PK": "1579",
                                    "mettol": "2017-02-28",
                                    "meddig": "2017-03-05",
                                    "idotartam": "5",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "128",
                                    "FOGLALAS_PK": "717",
                                    "mettol": "2016-07-26",
                                    "meddig": "2016-07-28",
                                    "idotartam": "2",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "128",
                                    "FOGLALAS_PK": "815",
                                    "mettol": "2016-08-24",
                                    "meddig": "2016-08-25",
                                    "idotartam": "1",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "128",
                                    "FOGLALAS_PK": "1290",
                                    "mettol": "2016-11-19",
                                    "meddig": "2016-11-20",
                                    "idotartam": "1",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "128",
                                    "FOGLALAS_PK": "1574",
                                    "mettol": "2017-02-26",
                                    "meddig": "2017-02-27",
                                    "idotartam": "1",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "128",
                                    "FOGLALAS_PK": "1583",
                                    "mettol": "2017-03-03",
                                    "meddig": "2017-03-07",
                                    "idotartam": "4",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "129",
                                    "FOGLALAS_PK": "723",
                                    "mettol": "2016-07-27",
                                    "meddig": "2016-08-03",
                                    "idotartam": "7",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "129",
                                    "FOGLALAS_PK": "1360",
                                    "mettol": "2016-12-13",
                                    "meddig": "2016-12-19",
                                    "idotartam": "6",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "129",
                                    "FOGLALAS_PK": "1445",
                                    "mettol": "2017-01-16",
                                    "meddig": "2017-01-23",
                                    "idotartam": "7",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "129",
                                    "FOGLALAS_PK": "1509",
                                    "mettol": "2017-02-08",
                                    "meddig": "2017-02-14",
                                    "idotartam": "6",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "130",
                                    "FOGLALAS_PK": "580",
                                    "mettol": "2016-04-14",
                                    "meddig": "2016-04-17",
                                    "idotartam": "3",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "130",
                                    "FOGLALAS_PK": "613",
                                    "mettol": "2016-05-01",
                                    "meddig": "2016-05-04",
                                    "idotartam": "3",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "130",
                                    "FOGLALAS_PK": "910",
                                    "mettol": "2016-06-06",
                                    "meddig": "2016-06-08",
                                    "idotartam": "2",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "130",
                                    "FOGLALAS_PK": "779",
                                    "mettol": "2016-08-15",
                                    "meddig": "2016-08-21",
                                    "idotartam": "6",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "130",
                                    "FOGLALAS_PK": "1040",
                                    "mettol": "2016-09-09",
                                    "meddig": "2016-09-10",
                                    "idotartam": "1",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "130",
                                    "FOGLALAS_PK": "1475",
                                    "mettol": "2017-01-26",
                                    "meddig": "2017-02-02",
                                    "idotartam": "7",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "131",
                                    "FOGLALAS_PK": "559",
                                    "mettol": "2016-04-06",
                                    "meddig": "2016-04-08",
                                    "idotartam": "2",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "131",
                                    "FOGLALAS_PK": "655",
                                    "mettol": "2016-05-18",
                                    "meddig": "2016-05-19",
                                    "idotartam": "1",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "131",
                                    "FOGLALAS_PK": "881",
                                    "mettol": "2016-05-30",
                                    "meddig": "2016-06-05",
                                    "idotartam": "6",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "131",
                                    "FOGLALAS_PK": "760",
                                    "mettol": "2016-08-06",
                                    "meddig": "2016-08-10",
                                    "idotartam": "4",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "131",
                                    "FOGLALAS_PK": "1474",
                                    "mettol": "2017-01-25",
                                    "meddig": "2017-01-30",
                                    "idotartam": "5",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "132",
                                    "FOGLALAS_PK": "619",
                                    "mettol": "2016-05-04",
                                    "meddig": "2016-05-11",
                                    "idotartam": "7",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "132",
                                    "FOGLALAS_PK": "999",
                                    "mettol": "2016-07-01",
                                    "meddig": "2016-07-07",
                                    "idotartam": "6",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "132",
                                    "FOGLALAS_PK": "1090",
                                    "mettol": "2016-09-30",
                                    "meddig": "2016-10-07",
                                    "idotartam": "7",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "132",
                                    "FOGLALAS_PK": "1111",
                                    "mettol": "2016-10-01",
                                    "meddig": "2016-10-04",
                                    "idotartam": "3",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "132",
                                    "FOGLALAS_PK": "1301",
                                    "mettol": "2016-11-22",
                                    "meddig": "2016-11-24",
                                    "idotartam": "2",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "132",
                                    "FOGLALAS_PK": "1519",
                                    "mettol": "2017-02-12",
                                    "meddig": "2017-02-14",
                                    "idotartam": "2",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "133",
                                    "FOGLALAS_PK": "909",
                                    "mettol": "2016-06-06",
                                    "meddig": "2016-06-10",
                                    "idotartam": "4",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "133",
                                    "FOGLALAS_PK": "988",
                                    "mettol": "2016-06-27",
                                    "meddig": "2016-06-30",
                                    "idotartam": "3",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "133",
                                    "FOGLALAS_PK": "1149",
                                    "mettol": "2016-10-12",
                                    "meddig": "2016-10-19",
                                    "idotartam": "7",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "133",
                                    "FOGLALAS_PK": "1306",
                                    "mettol": "2016-11-22",
                                    "meddig": "2016-11-25",
                                    "idotartam": "3",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "133",
                                    "FOGLALAS_PK": "1363",
                                    "mettol": "2016-12-15",
                                    "meddig": "2016-12-20",
                                    "idotartam": "5",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "133",
                                    "FOGLALAS_PK": "1409",
                                    "mettol": "2017-01-01",
                                    "meddig": "2017-01-02",
                                    "idotartam": "1",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "134",
                                    "FOGLALAS_PK": "1004",
                                    "mettol": "2016-07-03",
                                    "meddig": "2016-07-08",
                                    "idotartam": "5",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "134",
                                    "FOGLALAS_PK": "1024",
                                    "mettol": "2016-07-11",
                                    "meddig": "2016-07-12",
                                    "idotartam": "1",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "134",
                                    "FOGLALAS_PK": "1045",
                                    "mettol": "2016-09-12",
                                    "meddig": "2016-09-14",
                                    "idotartam": "2",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "134",
                                    "FOGLALAS_PK": "1178",
                                    "mettol": "2016-10-22",
                                    "meddig": "2016-10-29",
                                    "idotartam": "7",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "134",
                                    "FOGLALAS_PK": "1219",
                                    "mettol": "2016-10-30",
                                    "meddig": "2016-11-05",
                                    "idotartam": "6",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "134",
                                    "FOGLALAS_PK": "1535",
                                    "mettol": "2017-02-15",
                                    "meddig": "2017-02-22",
                                    "idotartam": "7",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "135",
                                    "FOGLALAS_PK": "724",
                                    "mettol": "2016-07-27",
                                    "meddig": "2016-08-02",
                                    "idotartam": "6",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "135",
                                    "FOGLALAS_PK": "849",
                                    "mettol": "2016-09-05",
                                    "meddig": "2016-09-12",
                                    "idotartam": "7",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "135",
                                    "FOGLALAS_PK": "1289",
                                    "mettol": "2016-11-18",
                                    "meddig": "2016-11-21",
                                    "idotartam": "3",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "136",
                                    "FOGLALAS_PK": "584",
                                    "mettol": "2016-04-17",
                                    "meddig": "2016-04-19",
                                    "idotartam": "2",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "136",
                                    "FOGLALAS_PK": "661",
                                    "mettol": "2016-05-21",
                                    "meddig": "2016-05-26",
                                    "idotartam": "5",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "136",
                                    "FOGLALAS_PK": "1046",
                                    "mettol": "2016-09-12",
                                    "meddig": "2016-09-16",
                                    "idotartam": "4",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "137",
                                    "FOGLALAS_PK": "582",
                                    "mettol": "2016-04-16",
                                    "meddig": "2016-04-19",
                                    "idotartam": "3",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "137",
                                    "FOGLALAS_PK": "649",
                                    "mettol": "2016-05-17",
                                    "meddig": "2016-05-22",
                                    "idotartam": "5",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "137",
                                    "FOGLALAS_PK": "657",
                                    "mettol": "2016-05-20",
                                    "meddig": "2016-05-26",
                                    "idotartam": "6",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "137",
                                    "FOGLALAS_PK": "1014",
                                    "mettol": "2016-07-06",
                                    "meddig": "2016-07-07",
                                    "idotartam": "1",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "137",
                                    "FOGLALAS_PK": "1201",
                                    "mettol": "2016-10-26",
                                    "meddig": "2016-11-01",
                                    "idotartam": "6",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "137",
                                    "FOGLALAS_PK": "1280",
                                    "mettol": "2016-11-15",
                                    "meddig": "2016-11-18",
                                    "idotartam": "3",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "138",
                                    "FOGLALAS_PK": "768",
                                    "mettol": "2016-08-12",
                                    "meddig": "2016-08-18",
                                    "idotartam": "6",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "138",
                                    "FOGLALAS_PK": "796",
                                    "mettol": "2016-08-17",
                                    "meddig": "2016-08-21",
                                    "idotartam": "4",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "138",
                                    "FOGLALAS_PK": "1256",
                                    "mettol": "2016-11-06",
                                    "meddig": "2016-11-10",
                                    "idotartam": "4",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "138",
                                    "FOGLALAS_PK": "1283",
                                    "mettol": "2016-11-16",
                                    "meddig": "2016-11-18",
                                    "idotartam": "2",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "138",
                                    "FOGLALAS_PK": "1294",
                                    "mettol": "2016-11-19",
                                    "meddig": "2016-11-24",
                                    "idotartam": "5",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "138",
                                    "FOGLALAS_PK": "1358",
                                    "mettol": "2016-12-11",
                                    "meddig": "2016-12-18",
                                    "idotartam": "7",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "138",
                                    "FOGLALAS_PK": "1370",
                                    "mettol": "2016-12-17",
                                    "meddig": "2016-12-22",
                                    "idotartam": "5",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "139",
                                    "FOGLALAS_PK": "579",
                                    "mettol": "2016-04-14",
                                    "meddig": "2016-04-16",
                                    "idotartam": "2",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "139",
                                    "FOGLALAS_PK": "745",
                                    "mettol": "2016-08-01",
                                    "meddig": "2016-08-02",
                                    "idotartam": "1",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "139",
                                    "FOGLALAS_PK": "751",
                                    "mettol": "2016-08-03",
                                    "meddig": "2016-08-07",
                                    "idotartam": "4",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "139",
                                    "FOGLALAS_PK": "1042",
                                    "mettol": "2016-09-10",
                                    "meddig": "2016-09-12",
                                    "idotartam": "2",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "139",
                                    "FOGLALAS_PK": "1064",
                                    "mettol": "2016-09-18",
                                    "meddig": "2016-09-24",
                                    "idotartam": "6",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "139",
                                    "FOGLALAS_PK": "1433",
                                    "mettol": "2017-01-11",
                                    "meddig": "2017-01-17",
                                    "idotartam": "6",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "139",
                                    "FOGLALAS_PK": "1450",
                                    "mettol": "2017-01-17",
                                    "meddig": "2017-01-24",
                                    "idotartam": "7",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "140",
                                    "FOGLALAS_PK": "915",
                                    "mettol": "2016-06-06",
                                    "meddig": "2016-06-08",
                                    "idotartam": "2",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "140",
                                    "FOGLALAS_PK": "733",
                                    "mettol": "2016-07-28",
                                    "meddig": "2016-07-29",
                                    "idotartam": "1",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "140",
                                    "FOGLALAS_PK": "1098",
                                    "mettol": "2016-10-01",
                                    "meddig": "2016-10-03",
                                    "idotartam": "2",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "140",
                                    "FOGLALAS_PK": "1156",
                                    "mettol": "2016-10-15",
                                    "meddig": "2016-10-18",
                                    "idotartam": "3",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "140",
                                    "FOGLALAS_PK": "1259",
                                    "mettol": "2016-11-07",
                                    "meddig": "2016-11-14",
                                    "idotartam": "7",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "140",
                                    "FOGLALAS_PK": "1357",
                                    "mettol": "2016-12-10",
                                    "meddig": "2016-12-14",
                                    "idotartam": "4",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "140",
                                    "FOGLALAS_PK": "1361",
                                    "mettol": "2016-12-14",
                                    "meddig": "2016-12-17",
                                    "idotartam": "3",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "140",
                                    "FOGLALAS_PK": "1371",
                                    "mettol": "2016-12-17",
                                    "meddig": "2016-12-18",
                                    "idotartam": "1",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "141",
                                    "FOGLALAS_PK": "565",
                                    "mettol": "2016-04-08",
                                    "meddig": "2016-04-14",
                                    "idotartam": "6",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "141",
                                    "FOGLALAS_PK": "908",
                                    "mettol": "2016-06-05",
                                    "meddig": "2016-06-07",
                                    "idotartam": "2",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "141",
                                    "FOGLALAS_PK": "761",
                                    "mettol": "2016-08-06",
                                    "meddig": "2016-08-09",
                                    "idotartam": "3",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "141",
                                    "FOGLALAS_PK": "784",
                                    "mettol": "2016-08-16",
                                    "meddig": "2016-08-23",
                                    "idotartam": "7",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "141",
                                    "FOGLALAS_PK": "1254",
                                    "mettol": "2016-11-06",
                                    "meddig": "2016-11-10",
                                    "idotartam": "4",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "141",
                                    "FOGLALAS_PK": "1401",
                                    "mettol": "2016-12-27",
                                    "meddig": "2017-01-02",
                                    "idotartam": "6",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "142",
                                    "FOGLALAS_PK": "1369",
                                    "mettol": "2016-12-17",
                                    "meddig": "2016-12-23",
                                    "idotartam": "6",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "142",
                                    "FOGLALAS_PK": "1545",
                                    "mettol": "2017-02-17",
                                    "meddig": "2017-02-20",
                                    "idotartam": "3",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "143",
                                    "FOGLALAS_PK": "980",
                                    "mettol": "2016-06-23",
                                    "meddig": "2016-06-26",
                                    "idotartam": "3",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "143",
                                    "FOGLALAS_PK": "1155",
                                    "mettol": "2016-10-15",
                                    "meddig": "2016-10-22",
                                    "idotartam": "7",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "143",
                                    "FOGLALAS_PK": "1193",
                                    "mettol": "2016-10-26",
                                    "meddig": "2016-11-01",
                                    "idotartam": "6",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "143",
                                    "FOGLALAS_PK": "1222",
                                    "mettol": "2016-10-30",
                                    "meddig": "2016-11-01",
                                    "idotartam": "2",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "143",
                                    "FOGLALAS_PK": "1313",
                                    "mettol": "2016-11-23",
                                    "meddig": "2016-11-27",
                                    "idotartam": "4",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "143",
                                    "FOGLALAS_PK": "1394",
                                    "mettol": "2016-12-25",
                                    "meddig": "2016-12-28",
                                    "idotartam": "3",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "143",
                                    "FOGLALAS_PK": "1448",
                                    "mettol": "2017-01-16",
                                    "meddig": "2017-01-22",
                                    "idotartam": "6",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "144",
                                    "FOGLALAS_PK": "581",
                                    "mettol": "2016-04-15",
                                    "meddig": "2016-04-19",
                                    "idotartam": "4",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "144",
                                    "FOGLALAS_PK": "1087",
                                    "mettol": "2016-09-29",
                                    "meddig": "2016-10-01",
                                    "idotartam": "2",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "144",
                                    "FOGLALAS_PK": "1199",
                                    "mettol": "2016-10-26",
                                    "meddig": "2016-11-02",
                                    "idotartam": "7",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "144",
                                    "FOGLALAS_PK": "1297",
                                    "mettol": "2016-11-19",
                                    "meddig": "2016-11-20",
                                    "idotartam": "1",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "144",
                                    "FOGLALAS_PK": "1572",
                                    "mettol": "2017-02-25",
                                    "meddig": "2017-02-27",
                                    "idotartam": "2",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "145",
                                    "FOGLALAS_PK": "703",
                                    "mettol": "2016-07-22",
                                    "meddig": "2016-07-26",
                                    "idotartam": "4",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "145",
                                    "FOGLALAS_PK": "1077",
                                    "mettol": "2016-09-23",
                                    "meddig": "2016-09-24",
                                    "idotartam": "1",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "145",
                                    "FOGLALAS_PK": "1120",
                                    "mettol": "2016-10-04",
                                    "meddig": "2016-10-05",
                                    "idotartam": "1",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "145",
                                    "FOGLALAS_PK": "1145",
                                    "mettol": "2016-10-09",
                                    "meddig": "2016-10-13",
                                    "idotartam": "4",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "145",
                                    "FOGLALAS_PK": "1338",
                                    "mettol": "2016-12-02",
                                    "meddig": "2016-12-04",
                                    "idotartam": "2",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "145",
                                    "FOGLALAS_PK": "1471",
                                    "mettol": "2017-01-23",
                                    "meddig": "2017-01-24",
                                    "idotartam": "1",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "146",
                                    "FOGLALAS_PK": "890",
                                    "mettol": "2016-06-02",
                                    "meddig": "2016-06-05",
                                    "idotartam": "3",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "146",
                                    "FOGLALAS_PK": "664",
                                    "mettol": "2016-07-13",
                                    "meddig": "2016-07-16",
                                    "idotartam": "3",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "146",
                                    "FOGLALAS_PK": "789",
                                    "mettol": "2016-08-16",
                                    "meddig": "2016-08-23",
                                    "idotartam": "7",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "146",
                                    "FOGLALAS_PK": "804",
                                    "mettol": "2016-08-20",
                                    "meddig": "2016-08-27",
                                    "idotartam": "7",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "146",
                                    "FOGLALAS_PK": "1032",
                                    "mettol": "2016-09-05",
                                    "meddig": "2016-09-10",
                                    "idotartam": "5",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "146",
                                    "FOGLALAS_PK": "1479",
                                    "mettol": "2017-01-28",
                                    "meddig": "2017-02-03",
                                    "idotartam": "6",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "147",
                                    "FOGLALAS_PK": "771",
                                    "mettol": "2016-08-12",
                                    "meddig": "2016-08-16",
                                    "idotartam": "4",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "148",
                                    "FOGLALAS_PK": "678",
                                    "mettol": "2016-07-17",
                                    "meddig": "2016-07-21",
                                    "idotartam": "4",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "148",
                                    "FOGLALAS_PK": "765",
                                    "mettol": "2016-08-09",
                                    "meddig": "2016-08-12",
                                    "idotartam": "3",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "148",
                                    "FOGLALAS_PK": "783",
                                    "mettol": "2016-08-16",
                                    "meddig": "2016-08-23",
                                    "idotartam": "7",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "148",
                                    "FOGLALAS_PK": "808",
                                    "mettol": "2016-08-23",
                                    "meddig": "2016-08-25",
                                    "idotartam": "2",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "148",
                                    "FOGLALAS_PK": "812",
                                    "mettol": "2016-08-23",
                                    "meddig": "2016-08-29",
                                    "idotartam": "6",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "148",
                                    "FOGLALAS_PK": "1578",
                                    "mettol": "2017-02-27",
                                    "meddig": "2017-03-06",
                                    "idotartam": "7",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "149",
                                    "FOGLALAS_PK": "591",
                                    "mettol": "2016-04-20",
                                    "meddig": "2016-04-21",
                                    "idotartam": "1",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "149",
                                    "FOGLALAS_PK": "652",
                                    "mettol": "2016-05-18",
                                    "meddig": "2016-05-19",
                                    "idotartam": "1",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "149",
                                    "FOGLALAS_PK": "833",
                                    "mettol": "2016-08-28",
                                    "meddig": "2016-08-30",
                                    "idotartam": "2",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "149",
                                    "FOGLALAS_PK": "834",
                                    "mettol": "2016-08-29",
                                    "meddig": "2016-09-03",
                                    "idotartam": "5",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "149",
                                    "FOGLALAS_PK": "843",
                                    "mettol": "2016-09-01",
                                    "meddig": "2016-09-05",
                                    "idotartam": "4",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "149",
                                    "FOGLALAS_PK": "1146",
                                    "mettol": "2016-10-10",
                                    "meddig": "2016-10-16",
                                    "idotartam": "6",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "149",
                                    "FOGLALAS_PK": "1514",
                                    "mettol": "2017-02-09",
                                    "meddig": "2017-02-14",
                                    "idotartam": "5",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "150",
                                    "FOGLALAS_PK": "641",
                                    "mettol": "2016-05-13",
                                    "meddig": "2016-05-16",
                                    "idotartam": "3",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "150",
                                    "FOGLALAS_PK": "1100",
                                    "mettol": "2016-10-01",
                                    "meddig": "2016-10-06",
                                    "idotartam": "5",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "150",
                                    "FOGLALAS_PK": "1105",
                                    "mettol": "2016-10-01",
                                    "meddig": "2016-10-02",
                                    "idotartam": "1",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "150",
                                    "FOGLALAS_PK": "1177",
                                    "mettol": "2016-10-22",
                                    "meddig": "2016-10-23",
                                    "idotartam": "1",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "150",
                                    "FOGLALAS_PK": "1203",
                                    "mettol": "2016-10-26",
                                    "meddig": "2016-10-30",
                                    "idotartam": "4",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "150",
                                    "FOGLALAS_PK": "1432",
                                    "mettol": "2017-01-10",
                                    "meddig": "2017-01-13",
                                    "idotartam": "3",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "151",
                                    "FOGLALAS_PK": "893",
                                    "mettol": "2016-06-03",
                                    "meddig": "2016-06-06",
                                    "idotartam": "3",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "151",
                                    "FOGLALAS_PK": "1058",
                                    "mettol": "2016-09-16",
                                    "meddig": "2016-09-19",
                                    "idotartam": "3",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "151",
                                    "FOGLALAS_PK": "1115",
                                    "mettol": "2016-10-02",
                                    "meddig": "2016-10-05",
                                    "idotartam": "3",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "152",
                                    "FOGLALAS_PK": "730",
                                    "mettol": "2016-07-28",
                                    "meddig": "2016-07-30",
                                    "idotartam": "2",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "152",
                                    "FOGLALAS_PK": "1160",
                                    "mettol": "2016-10-16",
                                    "meddig": "2016-10-23",
                                    "idotartam": "7",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "152",
                                    "FOGLALAS_PK": "1197",
                                    "mettol": "2016-10-26",
                                    "meddig": "2016-11-01",
                                    "idotartam": "6",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "152",
                                    "FOGLALAS_PK": "1558",
                                    "mettol": "2017-02-21",
                                    "meddig": "2017-02-23",
                                    "idotartam": "2",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "153",
                                    "FOGLALAS_PK": "594",
                                    "mettol": "2016-04-22",
                                    "meddig": "2016-04-25",
                                    "idotartam": "3",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "153",
                                    "FOGLALAS_PK": "969",
                                    "mettol": "2016-06-17",
                                    "meddig": "2016-06-23",
                                    "idotartam": "6",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "153",
                                    "FOGLALAS_PK": "1460",
                                    "mettol": "2017-01-21",
                                    "meddig": "2017-01-24",
                                    "idotartam": "3",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "153",
                                    "FOGLALAS_PK": "1470",
                                    "mettol": "2017-01-23",
                                    "meddig": "2017-01-28",
                                    "idotartam": "5",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "153",
                                    "FOGLALAS_PK": "1507",
                                    "mettol": "2017-02-07",
                                    "meddig": "2017-02-10",
                                    "idotartam": "3",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "154",
                                    "FOGLALAS_PK": "968",
                                    "mettol": "2016-06-16",
                                    "meddig": "2016-06-17",
                                    "idotartam": "1",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "154",
                                    "FOGLALAS_PK": "1061",
                                    "mettol": "2016-09-17",
                                    "meddig": "2016-09-24",
                                    "idotartam": "7",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "154",
                                    "FOGLALAS_PK": "1168",
                                    "mettol": "2016-10-19",
                                    "meddig": "2016-10-25",
                                    "idotartam": "6",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "154",
                                    "FOGLALAS_PK": "1262",
                                    "mettol": "2016-11-07",
                                    "meddig": "2016-11-08",
                                    "idotartam": "1",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "154",
                                    "FOGLALAS_PK": "1539",
                                    "mettol": "2017-02-16",
                                    "meddig": "2017-02-18",
                                    "idotartam": "2",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "155",
                                    "FOGLALAS_PK": "575",
                                    "mettol": "2016-04-10",
                                    "meddig": "2016-04-11",
                                    "idotartam": "1",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "155",
                                    "FOGLALAS_PK": "577",
                                    "mettol": "2016-04-12",
                                    "meddig": "2016-04-15",
                                    "idotartam": "3",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "155",
                                    "FOGLALAS_PK": "1112",
                                    "mettol": "2016-10-01",
                                    "meddig": "2016-10-05",
                                    "idotartam": "4",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "155",
                                    "FOGLALAS_PK": "1310",
                                    "mettol": "2016-11-23",
                                    "meddig": "2016-11-24",
                                    "idotartam": "1",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "155",
                                    "FOGLALAS_PK": "1541",
                                    "mettol": "2017-02-16",
                                    "meddig": "2017-02-17",
                                    "idotartam": "1",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "156",
                                    "FOGLALAS_PK": "588",
                                    "mettol": "2016-04-19",
                                    "meddig": "2016-04-26",
                                    "idotartam": "7",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "156",
                                    "FOGLALAS_PK": "907",
                                    "mettol": "2016-06-05",
                                    "meddig": "2016-06-08",
                                    "idotartam": "3",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "156",
                                    "FOGLALAS_PK": "956",
                                    "mettol": "2016-06-13",
                                    "meddig": "2016-06-19",
                                    "idotartam": "6",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "156",
                                    "FOGLALAS_PK": "692",
                                    "mettol": "2016-07-20",
                                    "meddig": "2016-07-26",
                                    "idotartam": "6",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "156",
                                    "FOGLALAS_PK": "1462",
                                    "mettol": "2017-01-22",
                                    "meddig": "2017-01-29",
                                    "idotartam": "7",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "156",
                                    "FOGLALAS_PK": "1490",
                                    "mettol": "2017-02-03",
                                    "meddig": "2017-02-04",
                                    "idotartam": "1",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "156",
                                    "FOGLALAS_PK": "1561",
                                    "mettol": "2017-02-23",
                                    "meddig": "2017-02-27",
                                    "idotartam": "4",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "157",
                                    "FOGLALAS_PK": "648",
                                    "mettol": "2016-05-16",
                                    "meddig": "2016-05-20",
                                    "idotartam": "4",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "157",
                                    "FOGLALAS_PK": "1025",
                                    "mettol": "2016-07-12",
                                    "meddig": "2016-07-15",
                                    "idotartam": "3",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "157",
                                    "FOGLALAS_PK": "1047",
                                    "mettol": "2016-09-13",
                                    "meddig": "2016-09-17",
                                    "idotartam": "4",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "157",
                                    "FOGLALAS_PK": "1240",
                                    "mettol": "2016-11-03",
                                    "meddig": "2016-11-10",
                                    "idotartam": "7",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "157",
                                    "FOGLALAS_PK": "1551",
                                    "mettol": "2017-02-19",
                                    "meddig": "2017-02-22",
                                    "idotartam": "3",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "158",
                                    "FOGLALAS_PK": "825",
                                    "mettol": "2016-08-25",
                                    "meddig": "2016-08-29",
                                    "idotartam": "4",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "158",
                                    "FOGLALAS_PK": "840",
                                    "mettol": "2016-08-30",
                                    "meddig": "2016-09-03",
                                    "idotartam": "4",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "158",
                                    "FOGLALAS_PK": "1117",
                                    "mettol": "2016-10-03",
                                    "meddig": "2016-10-06",
                                    "idotartam": "3",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "160",
                                    "FOGLALAS_PK": "922",
                                    "mettol": "2016-06-06",
                                    "meddig": "2016-06-08",
                                    "idotartam": "2",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "160",
                                    "FOGLALAS_PK": "927",
                                    "mettol": "2016-06-07",
                                    "meddig": "2016-06-11",
                                    "idotartam": "4",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "160",
                                    "FOGLALAS_PK": "933",
                                    "mettol": "2016-06-07",
                                    "meddig": "2016-06-11",
                                    "idotartam": "4",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "160",
                                    "FOGLALAS_PK": "720",
                                    "mettol": "2016-07-27",
                                    "meddig": "2016-07-29",
                                    "idotartam": "2",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "160",
                                    "FOGLALAS_PK": "1565",
                                    "mettol": "2017-02-23",
                                    "meddig": "2017-02-26",
                                    "idotartam": "3",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "161",
                                    "FOGLALAS_PK": "639",
                                    "mettol": "2016-05-12",
                                    "meddig": "2016-05-16",
                                    "idotartam": "4",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "161",
                                    "FOGLALAS_PK": "653",
                                    "mettol": "2016-05-18",
                                    "meddig": "2016-05-25",
                                    "idotartam": "7",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "161",
                                    "FOGLALAS_PK": "911",
                                    "mettol": "2016-06-06",
                                    "meddig": "2016-06-10",
                                    "idotartam": "4",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "161",
                                    "FOGLALAS_PK": "1068",
                                    "mettol": "2016-09-19",
                                    "meddig": "2016-09-25",
                                    "idotartam": "6",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "161",
                                    "FOGLALAS_PK": "1190",
                                    "mettol": "2016-10-24",
                                    "meddig": "2016-10-31",
                                    "idotartam": "7",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "161",
                                    "FOGLALAS_PK": "1571",
                                    "mettol": "2017-02-25",
                                    "meddig": "2017-03-01",
                                    "idotartam": "4",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "162",
                                    "FOGLALAS_PK": "599",
                                    "mettol": "2016-04-24",
                                    "meddig": "2016-04-28",
                                    "idotartam": "4",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "162",
                                    "FOGLALAS_PK": "1205",
                                    "mettol": "2016-10-27",
                                    "meddig": "2016-11-02",
                                    "idotartam": "6",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "162",
                                    "FOGLALAS_PK": "1400",
                                    "mettol": "2016-12-26",
                                    "meddig": "2016-12-27",
                                    "idotartam": "1",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "163",
                                    "FOGLALAS_PK": "630",
                                    "mettol": "2016-05-09",
                                    "meddig": "2016-05-11",
                                    "idotartam": "2",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "163",
                                    "FOGLALAS_PK": "941",
                                    "mettol": "2016-06-10",
                                    "meddig": "2016-06-11",
                                    "idotartam": "1",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "163",
                                    "FOGLALAS_PK": "782",
                                    "mettol": "2016-08-16",
                                    "meddig": "2016-08-19",
                                    "idotartam": "3",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "163",
                                    "FOGLALAS_PK": "1075",
                                    "mettol": "2016-09-23",
                                    "meddig": "2016-09-27",
                                    "idotartam": "4",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "163",
                                    "FOGLALAS_PK": "1107",
                                    "mettol": "2016-10-01",
                                    "meddig": "2016-10-04",
                                    "idotartam": "3",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "163",
                                    "FOGLALAS_PK": "1265",
                                    "mettol": "2016-11-08",
                                    "meddig": "2016-11-13",
                                    "idotartam": "5",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "163",
                                    "FOGLALAS_PK": "1487",
                                    "mettol": "2017-02-01",
                                    "meddig": "2017-02-04",
                                    "idotartam": "3",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "164",
                                    "FOGLALAS_PK": "570",
                                    "mettol": "2016-04-10",
                                    "meddig": "2016-04-17",
                                    "idotartam": "7",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "164",
                                    "FOGLALAS_PK": "1010",
                                    "mettol": "2016-07-04",
                                    "meddig": "2016-07-06",
                                    "idotartam": "2",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "164",
                                    "FOGLALAS_PK": "742",
                                    "mettol": "2016-07-31",
                                    "meddig": "2016-08-06",
                                    "idotartam": "6",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "164",
                                    "FOGLALAS_PK": "1284",
                                    "mettol": "2016-11-16",
                                    "meddig": "2016-11-20",
                                    "idotartam": "4",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "164",
                                    "FOGLALAS_PK": "1292",
                                    "mettol": "2016-11-19",
                                    "meddig": "2016-11-21",
                                    "idotartam": "2",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "165",
                                    "FOGLALAS_PK": "640",
                                    "mettol": "2016-05-12",
                                    "meddig": "2016-05-15",
                                    "idotartam": "3",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "165",
                                    "FOGLALAS_PK": "857",
                                    "mettol": "2016-05-25",
                                    "meddig": "2016-05-30",
                                    "idotartam": "5",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "165",
                                    "FOGLALAS_PK": "900",
                                    "mettol": "2016-06-03",
                                    "meddig": "2016-06-09",
                                    "idotartam": "6",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "165",
                                    "FOGLALAS_PK": "897",
                                    "mettol": "2016-06-03",
                                    "meddig": "2016-06-09",
                                    "idotartam": "6",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "165",
                                    "FOGLALAS_PK": "892",
                                    "mettol": "2016-06-03",
                                    "meddig": "2016-06-06",
                                    "idotartam": "3",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "165",
                                    "FOGLALAS_PK": "1141",
                                    "mettol": "2016-10-09",
                                    "meddig": "2016-10-10",
                                    "idotartam": "1",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "165",
                                    "FOGLALAS_PK": "1375",
                                    "mettol": "2016-12-17",
                                    "meddig": "2016-12-21",
                                    "idotartam": "4",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "166",
                                    "FOGLALAS_PK": "644",
                                    "mettol": "2016-05-14",
                                    "meddig": "2016-05-21",
                                    "idotartam": "7",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "166",
                                    "FOGLALAS_PK": "781",
                                    "mettol": "2016-08-16",
                                    "meddig": "2016-08-23",
                                    "idotartam": "7",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "166",
                                    "FOGLALAS_PK": "1526",
                                    "mettol": "2017-02-12",
                                    "meddig": "2017-02-14",
                                    "idotartam": "2",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "167",
                                    "FOGLALAS_PK": "854",
                                    "mettol": "2016-05-24",
                                    "meddig": "2016-05-31",
                                    "idotartam": "7",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "167",
                                    "FOGLALAS_PK": "1414",
                                    "mettol": "2017-01-02",
                                    "meddig": "2017-01-05",
                                    "idotartam": "3",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "168",
                                    "FOGLALAS_PK": "930",
                                    "mettol": "2016-06-07",
                                    "meddig": "2016-06-10",
                                    "idotartam": "3",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "168",
                                    "FOGLALAS_PK": "792",
                                    "mettol": "2016-08-16",
                                    "meddig": "2016-08-19",
                                    "idotartam": "3",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "168",
                                    "FOGLALAS_PK": "794",
                                    "mettol": "2016-08-17",
                                    "meddig": "2016-08-21",
                                    "idotartam": "4",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "168",
                                    "FOGLALAS_PK": "1249",
                                    "mettol": "2016-11-05",
                                    "meddig": "2016-11-09",
                                    "idotartam": "4",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "168",
                                    "FOGLALAS_PK": "1266",
                                    "mettol": "2016-11-08",
                                    "meddig": "2016-11-12",
                                    "idotartam": "4",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "169",
                                    "FOGLALAS_PK": "573",
                                    "mettol": "2016-04-10",
                                    "meddig": "2016-04-15",
                                    "idotartam": "5",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "169",
                                    "FOGLALAS_PK": "659",
                                    "mettol": "2016-05-21",
                                    "meddig": "2016-05-27",
                                    "idotartam": "6",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "169",
                                    "FOGLALAS_PK": "974",
                                    "mettol": "2016-06-20",
                                    "meddig": "2016-06-21",
                                    "idotartam": "1",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "169",
                                    "FOGLALAS_PK": "746",
                                    "mettol": "2016-08-01",
                                    "meddig": "2016-08-08",
                                    "idotartam": "7",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "169",
                                    "FOGLALAS_PK": "1356",
                                    "mettol": "2016-12-09",
                                    "meddig": "2016-12-13",
                                    "idotartam": "4",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "169",
                                    "FOGLALAS_PK": "1427",
                                    "mettol": "2017-01-09",
                                    "meddig": "2017-01-10",
                                    "idotartam": "1",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "170",
                                    "FOGLALAS_PK": "567",
                                    "mettol": "2016-04-10",
                                    "meddig": "2016-04-17",
                                    "idotartam": "7",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "170",
                                    "FOGLALAS_PK": "944",
                                    "mettol": "2016-06-10",
                                    "meddig": "2016-06-14",
                                    "idotartam": "4",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "170",
                                    "FOGLALAS_PK": "1194",
                                    "mettol": "2016-10-26",
                                    "meddig": "2016-10-30",
                                    "idotartam": "4",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "170",
                                    "FOGLALAS_PK": "1267",
                                    "mettol": "2016-11-09",
                                    "meddig": "2016-11-16",
                                    "idotartam": "7",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "170",
                                    "FOGLALAS_PK": "1342",
                                    "mettol": "2016-12-04",
                                    "meddig": "2016-12-10",
                                    "idotartam": "6",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "171",
                                    "FOGLALAS_PK": "574",
                                    "mettol": "2016-04-10",
                                    "meddig": "2016-04-12",
                                    "idotartam": "2",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "171",
                                    "FOGLALAS_PK": "981",
                                    "mettol": "2016-06-23",
                                    "meddig": "2016-06-27",
                                    "idotartam": "4",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "171",
                                    "FOGLALAS_PK": "1181",
                                    "mettol": "2016-10-23",
                                    "meddig": "2016-10-29",
                                    "idotartam": "6",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "171",
                                    "FOGLALAS_PK": "1329",
                                    "mettol": "2016-11-29",
                                    "meddig": "2016-12-04",
                                    "idotartam": "5",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "171",
                                    "FOGLALAS_PK": "1567",
                                    "mettol": "2017-02-24",
                                    "meddig": "2017-03-02",
                                    "idotartam": "6",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "172",
                                    "FOGLALAS_PK": "984",
                                    "mettol": "2016-06-24",
                                    "meddig": "2016-06-28",
                                    "idotartam": "4",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "172",
                                    "FOGLALAS_PK": "709",
                                    "mettol": "2016-07-24",
                                    "meddig": "2016-07-29",
                                    "idotartam": "5",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "172",
                                    "FOGLALAS_PK": "749",
                                    "mettol": "2016-08-02",
                                    "meddig": "2016-08-08",
                                    "idotartam": "6",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "172",
                                    "FOGLALAS_PK": "839",
                                    "mettol": "2016-08-29",
                                    "meddig": "2016-09-03",
                                    "idotartam": "5",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "172",
                                    "FOGLALAS_PK": "1142",
                                    "mettol": "2016-10-09",
                                    "meddig": "2016-10-13",
                                    "idotartam": "4",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "172",
                                    "FOGLALAS_PK": "1171",
                                    "mettol": "2016-10-20",
                                    "meddig": "2016-10-25",
                                    "idotartam": "5",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "172",
                                    "FOGLALAS_PK": "1336",
                                    "mettol": "2016-12-02",
                                    "meddig": "2016-12-07",
                                    "idotartam": "5",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "172",
                                    "FOGLALAS_PK": "1421",
                                    "mettol": "2017-01-05",
                                    "meddig": "2017-01-10",
                                    "idotartam": "5",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "172",
                                    "FOGLALAS_PK": "1491",
                                    "mettol": "2017-02-03",
                                    "meddig": "2017-02-05",
                                    "idotartam": "2",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "173",
                                    "FOGLALAS_PK": "913",
                                    "mettol": "2016-06-06",
                                    "meddig": "2016-06-07",
                                    "idotartam": "1",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "173",
                                    "FOGLALAS_PK": "669",
                                    "mettol": "2016-07-14",
                                    "meddig": "2016-07-21",
                                    "idotartam": "7",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "173",
                                    "FOGLALAS_PK": "1350",
                                    "mettol": "2016-12-06",
                                    "meddig": "2016-12-09",
                                    "idotartam": "3",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "173",
                                    "FOGLALAS_PK": "1429",
                                    "mettol": "2017-01-09",
                                    "meddig": "2017-01-13",
                                    "idotartam": "4",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "174",
                                    "FOGLALAS_PK": "917",
                                    "mettol": "2016-06-06",
                                    "meddig": "2016-06-08",
                                    "idotartam": "2",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "174",
                                    "FOGLALAS_PK": "1015",
                                    "mettol": "2016-07-06",
                                    "meddig": "2016-07-11",
                                    "idotartam": "5",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "174",
                                    "FOGLALAS_PK": "682",
                                    "mettol": "2016-07-18",
                                    "meddig": "2016-07-21",
                                    "idotartam": "3",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "174",
                                    "FOGLALAS_PK": "1276",
                                    "mettol": "2016-11-12",
                                    "meddig": "2016-11-13",
                                    "idotartam": "1",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "175",
                                    "FOGLALAS_PK": "867",
                                    "mettol": "2016-05-28",
                                    "meddig": "2016-06-03",
                                    "idotartam": "6",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "175",
                                    "FOGLALAS_PK": "799",
                                    "mettol": "2016-08-19",
                                    "meddig": "2016-08-23",
                                    "idotartam": "4",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "175",
                                    "FOGLALAS_PK": "1094",
                                    "mettol": "2016-09-30",
                                    "meddig": "2016-10-05",
                                    "idotartam": "5",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "175",
                                    "FOGLALAS_PK": "1133",
                                    "mettol": "2016-10-08",
                                    "meddig": "2016-10-10",
                                    "idotartam": "2",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "175",
                                    "FOGLALAS_PK": "1407",
                                    "mettol": "2016-12-30",
                                    "meddig": "2017-01-06",
                                    "idotartam": "7",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "176",
                                    "FOGLALAS_PK": "592",
                                    "mettol": "2016-04-21",
                                    "meddig": "2016-04-26",
                                    "idotartam": "5",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "176",
                                    "FOGLALAS_PK": "1143",
                                    "mettol": "2016-10-09",
                                    "meddig": "2016-10-15",
                                    "idotartam": "6",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "176",
                                    "FOGLALAS_PK": "1278",
                                    "mettol": "2016-11-13",
                                    "meddig": "2016-11-19",
                                    "idotartam": "6",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "176",
                                    "FOGLALAS_PK": "1383",
                                    "mettol": "2016-12-22",
                                    "meddig": "2016-12-26",
                                    "idotartam": "4",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "176",
                                    "FOGLALAS_PK": "1511",
                                    "mettol": "2017-02-08",
                                    "meddig": "2017-02-10",
                                    "idotartam": "2",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "176",
                                    "FOGLALAS_PK": "1570",
                                    "mettol": "2017-02-24",
                                    "meddig": "2017-02-27",
                                    "idotartam": "3",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "177",
                                    "FOGLALAS_PK": "785",
                                    "mettol": "2016-08-16",
                                    "meddig": "2016-08-19",
                                    "idotartam": "3",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "177",
                                    "FOGLALAS_PK": "831",
                                    "mettol": "2016-08-28",
                                    "meddig": "2016-09-04",
                                    "idotartam": "7",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "177",
                                    "FOGLALAS_PK": "1176",
                                    "mettol": "2016-10-21",
                                    "meddig": "2016-10-24",
                                    "idotartam": "3",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "177",
                                    "FOGLALAS_PK": "1503",
                                    "mettol": "2017-02-05",
                                    "meddig": "2017-02-08",
                                    "idotartam": "3",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "178",
                                    "FOGLALAS_PK": "991",
                                    "mettol": "2016-06-28",
                                    "meddig": "2016-07-05",
                                    "idotartam": "7",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "178",
                                    "FOGLALAS_PK": "816",
                                    "mettol": "2016-08-24",
                                    "meddig": "2016-08-28",
                                    "idotartam": "4",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "178",
                                    "FOGLALAS_PK": "1211",
                                    "mettol": "2016-10-28",
                                    "meddig": "2016-10-31",
                                    "idotartam": "3",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "178",
                                    "FOGLALAS_PK": "1242",
                                    "mettol": "2016-11-03",
                                    "meddig": "2016-11-04",
                                    "idotartam": "1",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "179",
                                    "FOGLALAS_PK": "662",
                                    "mettol": "2016-05-21",
                                    "meddig": "2016-05-23",
                                    "idotartam": "2",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "179",
                                    "FOGLALAS_PK": "1021",
                                    "mettol": "2016-07-09",
                                    "meddig": "2016-07-10",
                                    "idotartam": "1",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "179",
                                    "FOGLALAS_PK": "1497",
                                    "mettol": "2017-02-04",
                                    "meddig": "2017-02-05",
                                    "idotartam": "1",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "180",
                                    "FOGLALAS_PK": "905",
                                    "mettol": "2016-06-04",
                                    "meddig": "2016-06-09",
                                    "idotartam": "5",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "180",
                                    "FOGLALAS_PK": "1559",
                                    "mettol": "2017-02-22",
                                    "meddig": "2017-02-25",
                                    "idotartam": "3",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "180",
                                    "FOGLALAS_PK": "1563",
                                    "mettol": "2017-02-23",
                                    "meddig": "2017-03-01",
                                    "idotartam": "6",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "181",
                                    "FOGLALAS_PK": "937",
                                    "mettol": "2016-06-08",
                                    "meddig": "2016-06-11",
                                    "idotartam": "3",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "181",
                                    "FOGLALAS_PK": "958",
                                    "mettol": "2016-06-13",
                                    "meddig": "2016-06-18",
                                    "idotartam": "5",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "181",
                                    "FOGLALAS_PK": "1022",
                                    "mettol": "2016-07-10",
                                    "meddig": "2016-07-11",
                                    "idotartam": "1",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "181",
                                    "FOGLALAS_PK": "677",
                                    "mettol": "2016-07-16",
                                    "meddig": "2016-07-20",
                                    "idotartam": "4",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "181",
                                    "FOGLALAS_PK": "731",
                                    "mettol": "2016-07-28",
                                    "meddig": "2016-08-03",
                                    "idotartam": "6",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "181",
                                    "FOGLALAS_PK": "1346",
                                    "mettol": "2016-12-05",
                                    "meddig": "2016-12-11",
                                    "idotartam": "6",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "182",
                                    "FOGLALAS_PK": "571",
                                    "mettol": "2016-04-10",
                                    "meddig": "2016-04-12",
                                    "idotartam": "2",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "182",
                                    "FOGLALAS_PK": "928",
                                    "mettol": "2016-06-07",
                                    "meddig": "2016-06-09",
                                    "idotartam": "2",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "182",
                                    "FOGLALAS_PK": "1008",
                                    "mettol": "2016-07-04",
                                    "meddig": "2016-07-10",
                                    "idotartam": "6",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "182",
                                    "FOGLALAS_PK": "740",
                                    "mettol": "2016-07-30",
                                    "meddig": "2016-08-02",
                                    "idotartam": "3",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "182",
                                    "FOGLALAS_PK": "1188",
                                    "mettol": "2016-10-24",
                                    "meddig": "2016-10-25",
                                    "idotartam": "1",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "182",
                                    "FOGLALAS_PK": "1230",
                                    "mettol": "2016-10-30",
                                    "meddig": "2016-11-06",
                                    "idotartam": "7",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "182",
                                    "FOGLALAS_PK": "1231",
                                    "mettol": "2016-10-30",
                                    "meddig": "2016-11-03",
                                    "idotartam": "4",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "182",
                                    "FOGLALAS_PK": "1308",
                                    "mettol": "2016-11-23",
                                    "meddig": "2016-11-24",
                                    "idotartam": "1",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "182",
                                    "FOGLALAS_PK": "1317",
                                    "mettol": "2016-11-25",
                                    "meddig": "2016-11-28",
                                    "idotartam": "3",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "182",
                                    "FOGLALAS_PK": "1326",
                                    "mettol": "2016-11-28",
                                    "meddig": "2016-12-02",
                                    "idotartam": "4",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "182",
                                    "FOGLALAS_PK": "1410",
                                    "mettol": "2017-01-01",
                                    "meddig": "2017-01-05",
                                    "idotartam": "4",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "182",
                                    "FOGLALAS_PK": "1422",
                                    "mettol": "2017-01-06",
                                    "meddig": "2017-01-09",
                                    "idotartam": "3",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "183",
                                    "FOGLALAS_PK": "939",
                                    "mettol": "2016-06-09",
                                    "meddig": "2016-06-13",
                                    "idotartam": "4",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "183",
                                    "FOGLALAS_PK": "1067",
                                    "mettol": "2016-09-19",
                                    "meddig": "2016-09-26",
                                    "idotartam": "7",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "183",
                                    "FOGLALAS_PK": "1147",
                                    "mettol": "2016-10-10",
                                    "meddig": "2016-10-14",
                                    "idotartam": "4",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "183",
                                    "FOGLALAS_PK": "1437",
                                    "mettol": "2017-01-13",
                                    "meddig": "2017-01-17",
                                    "idotartam": "4",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "184",
                                    "FOGLALAS_PK": "608",
                                    "mettol": "2016-04-28",
                                    "meddig": "2016-04-30",
                                    "idotartam": "2",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "184",
                                    "FOGLALAS_PK": "880",
                                    "mettol": "2016-05-30",
                                    "meddig": "2016-06-03",
                                    "idotartam": "4",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "184",
                                    "FOGLALAS_PK": "684",
                                    "mettol": "2016-07-18",
                                    "meddig": "2016-07-21",
                                    "idotartam": "3",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "184",
                                    "FOGLALAS_PK": "1251",
                                    "mettol": "2016-11-05",
                                    "meddig": "2016-11-09",
                                    "idotartam": "4",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "185",
                                    "FOGLALAS_PK": "578",
                                    "mettol": "2016-04-13",
                                    "meddig": "2016-04-19",
                                    "idotartam": "6",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "185",
                                    "FOGLALAS_PK": "863",
                                    "mettol": "2016-05-28",
                                    "meddig": "2016-06-01",
                                    "idotartam": "4",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "185",
                                    "FOGLALAS_PK": "898",
                                    "mettol": "2016-06-03",
                                    "meddig": "2016-06-07",
                                    "idotartam": "4",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "185",
                                    "FOGLALAS_PK": "925",
                                    "mettol": "2016-06-07",
                                    "meddig": "2016-06-13",
                                    "idotartam": "6",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "185",
                                    "FOGLALAS_PK": "672",
                                    "mettol": "2016-07-14",
                                    "meddig": "2016-07-17",
                                    "idotartam": "3",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "185",
                                    "FOGLALAS_PK": "679",
                                    "mettol": "2016-07-17",
                                    "meddig": "2016-07-22",
                                    "idotartam": "5",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "185",
                                    "FOGLALAS_PK": "693",
                                    "mettol": "2016-07-20",
                                    "meddig": "2016-07-22",
                                    "idotartam": "2",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "185",
                                    "FOGLALAS_PK": "711",
                                    "mettol": "2016-07-24",
                                    "meddig": "2016-07-27",
                                    "idotartam": "3",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "185",
                                    "FOGLALAS_PK": "1125",
                                    "mettol": "2016-10-06",
                                    "meddig": "2016-10-09",
                                    "idotartam": "3",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "185",
                                    "FOGLALAS_PK": "1183",
                                    "mettol": "2016-10-23",
                                    "meddig": "2016-10-28",
                                    "idotartam": "5",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "185",
                                    "FOGLALAS_PK": "1441",
                                    "mettol": "2017-01-16",
                                    "meddig": "2017-01-23",
                                    "idotartam": "7",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "185",
                                    "FOGLALAS_PK": "1463",
                                    "mettol": "2017-01-22",
                                    "meddig": "2017-01-29",
                                    "idotartam": "7",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "186",
                                    "FOGLALAS_PK": "615",
                                    "mettol": "2016-05-01",
                                    "meddig": "2016-05-04",
                                    "idotartam": "3",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "186",
                                    "FOGLALAS_PK": "1153",
                                    "mettol": "2016-10-15",
                                    "meddig": "2016-10-18",
                                    "idotartam": "3",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "186",
                                    "FOGLALAS_PK": "1248",
                                    "mettol": "2016-11-05",
                                    "meddig": "2016-11-07",
                                    "idotartam": "2",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "186",
                                    "FOGLALAS_PK": "1467",
                                    "mettol": "2017-01-22",
                                    "meddig": "2017-01-25",
                                    "idotartam": "3",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "187",
                                    "FOGLALAS_PK": "633",
                                    "mettol": "2016-05-09",
                                    "meddig": "2016-05-15",
                                    "idotartam": "6",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "187",
                                    "FOGLALAS_PK": "868",
                                    "mettol": "2016-05-28",
                                    "meddig": "2016-06-01",
                                    "idotartam": "4",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "187",
                                    "FOGLALAS_PK": "957",
                                    "mettol": "2016-06-13",
                                    "meddig": "2016-06-17",
                                    "idotartam": "4",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "187",
                                    "FOGLALAS_PK": "695",
                                    "mettol": "2016-07-20",
                                    "meddig": "2016-07-26",
                                    "idotartam": "6",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "187",
                                    "FOGLALAS_PK": "743",
                                    "mettol": "2016-07-31",
                                    "meddig": "2016-08-02",
                                    "idotartam": "2",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "187",
                                    "FOGLALAS_PK": "766",
                                    "mettol": "2016-08-10",
                                    "meddig": "2016-08-11",
                                    "idotartam": "1",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "187",
                                    "FOGLALAS_PK": "1404",
                                    "mettol": "2016-12-29",
                                    "meddig": "2016-12-31",
                                    "idotartam": "2",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "188",
                                    "FOGLALAS_PK": "912",
                                    "mettol": "2016-06-06",
                                    "meddig": "2016-06-07",
                                    "idotartam": "1",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "188",
                                    "FOGLALAS_PK": "690",
                                    "mettol": "2016-07-19",
                                    "meddig": "2016-07-23",
                                    "idotartam": "4",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "188",
                                    "FOGLALAS_PK": "710",
                                    "mettol": "2016-07-24",
                                    "meddig": "2016-07-31",
                                    "idotartam": "7",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "188",
                                    "FOGLALAS_PK": "747",
                                    "mettol": "2016-08-01",
                                    "meddig": "2016-08-04",
                                    "idotartam": "3",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "188",
                                    "FOGLALAS_PK": "1030",
                                    "mettol": "2016-09-05",
                                    "meddig": "2016-09-09",
                                    "idotartam": "4",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "188",
                                    "FOGLALAS_PK": "1390",
                                    "mettol": "2016-12-25",
                                    "meddig": "2016-12-30",
                                    "idotartam": "5",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "189",
                                    "FOGLALAS_PK": "699",
                                    "mettol": "2016-07-20",
                                    "meddig": "2016-07-22",
                                    "idotartam": "2",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "189",
                                    "FOGLALAS_PK": "753",
                                    "mettol": "2016-08-03",
                                    "meddig": "2016-08-04",
                                    "idotartam": "1",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "189",
                                    "FOGLALAS_PK": "1204",
                                    "mettol": "2016-10-27",
                                    "meddig": "2016-10-29",
                                    "idotartam": "2",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "189",
                                    "FOGLALAS_PK": "1449",
                                    "mettol": "2017-01-17",
                                    "meddig": "2017-01-19",
                                    "idotartam": "2",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "189",
                                    "FOGLALAS_PK": "1576",
                                    "mettol": "2017-02-26",
                                    "meddig": "2017-03-01",
                                    "idotartam": "3",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "190",
                                    "FOGLALAS_PK": "600",
                                    "mettol": "2016-04-24",
                                    "meddig": "2016-05-01",
                                    "idotartam": "7",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "190",
                                    "FOGLALAS_PK": "989",
                                    "mettol": "2016-06-27",
                                    "meddig": "2016-06-28",
                                    "idotartam": "1",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "190",
                                    "FOGLALAS_PK": "1017",
                                    "mettol": "2016-07-08",
                                    "meddig": "2016-07-09",
                                    "idotartam": "1",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "190",
                                    "FOGLALAS_PK": "774",
                                    "mettol": "2016-08-13",
                                    "meddig": "2016-08-18",
                                    "idotartam": "5",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "190",
                                    "FOGLALAS_PK": "1517",
                                    "mettol": "2017-02-11",
                                    "meddig": "2017-02-16",
                                    "idotartam": "5",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "191",
                                    "FOGLALAS_PK": "1039",
                                    "mettol": "2016-09-09",
                                    "meddig": "2016-09-15",
                                    "idotartam": "6",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "191",
                                    "FOGLALAS_PK": "1302",
                                    "mettol": "2016-11-22",
                                    "meddig": "2016-11-23",
                                    "idotartam": "1",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "191",
                                    "FOGLALAS_PK": "1323",
                                    "mettol": "2016-11-27",
                                    "meddig": "2016-12-04",
                                    "idotartam": "7",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "191",
                                    "FOGLALAS_PK": "1502",
                                    "mettol": "2017-02-05",
                                    "meddig": "2017-02-07",
                                    "idotartam": "2",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "191",
                                    "FOGLALAS_PK": "1508",
                                    "mettol": "2017-02-08",
                                    "meddig": "2017-02-15",
                                    "idotartam": "7",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "192",
                                    "FOGLALAS_PK": "903",
                                    "mettol": "2016-06-04",
                                    "meddig": "2016-06-11",
                                    "idotartam": "7",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "192",
                                    "FOGLALAS_PK": "680",
                                    "mettol": "2016-07-17",
                                    "meddig": "2016-07-21",
                                    "idotartam": "4",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "193",
                                    "FOGLALAS_PK": "634",
                                    "mettol": "2016-05-09",
                                    "meddig": "2016-05-15",
                                    "idotartam": "6",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "193",
                                    "FOGLALAS_PK": "926",
                                    "mettol": "2016-06-07",
                                    "meddig": "2016-06-08",
                                    "idotartam": "1",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "193",
                                    "FOGLALAS_PK": "977",
                                    "mettol": "2016-06-22",
                                    "meddig": "2016-06-24",
                                    "idotartam": "2",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "193",
                                    "FOGLALAS_PK": "675",
                                    "mettol": "2016-07-15",
                                    "meddig": "2016-07-17",
                                    "idotartam": "2",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "193",
                                    "FOGLALAS_PK": "835",
                                    "mettol": "2016-08-29",
                                    "meddig": "2016-08-31",
                                    "idotartam": "2",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "193",
                                    "FOGLALAS_PK": "1043",
                                    "mettol": "2016-09-11",
                                    "meddig": "2016-09-17",
                                    "idotartam": "6",
                                    "(No column name)": "2"
                                },
                                {
                                    "SZOBA_FK": "193",
                                    "FOGLALAS_PK": "1238",
                                    "mettol": "2016-11-03",
                                    "meddig": "2016-11-09",
                                    "idotartam": "6",
                                    "(No column name)": "6"
                                },
                                {
                                    "SZOBA_FK": "194",
                                    "FOGLALAS_PK": "1095",
                                    "mettol": "2016-09-30",
                                    "meddig": "2016-10-05",
                                    "idotartam": "5",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "195",
                                    "FOGLALAS_PK": "721",
                                    "mettol": "2016-07-27",
                                    "meddig": "2016-07-31",
                                    "idotartam": "4",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "195",
                                    "FOGLALAS_PK": "842",
                                    "mettol": "2016-08-31",
                                    "meddig": "2016-09-04",
                                    "idotartam": "4",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "195",
                                    "FOGLALAS_PK": "1074",
                                    "mettol": "2016-09-22",
                                    "meddig": "2016-09-29",
                                    "idotartam": "7",
                                    "(No column name)": "4"
                                },
                                {
                                    "SZOBA_FK": "195",
                                    "FOGLALAS_PK": "1184",
                                    "mettol": "2016-10-23",
                                    "meddig": "2016-10-28",
                                    "idotartam": "5",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "195",
                                    "FOGLALAS_PK": "1473",
                                    "mettol": "2017-01-24",
                                    "meddig": "2017-01-31",
                                    "idotartam": "7",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "195",
                                    "FOGLALAS_PK": "1484",
                                    "mettol": "2017-01-30",
                                    "meddig": "2017-01-31",
                                    "idotartam": "1",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "196",
                                    "FOGLALAS_PK": "952",
                                    "mettol": "2016-06-11",
                                    "meddig": "2016-06-14",
                                    "idotartam": "3",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "196",
                                    "FOGLALAS_PK": "673",
                                    "mettol": "2016-07-14",
                                    "meddig": "2016-07-19",
                                    "idotartam": "5",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "196",
                                    "FOGLALAS_PK": "1314",
                                    "mettol": "2016-11-23",
                                    "meddig": "2016-11-28",
                                    "idotartam": "5",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "196",
                                    "FOGLALAS_PK": "1340",
                                    "mettol": "2016-12-04",
                                    "meddig": "2016-12-09",
                                    "idotartam": "5",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "197",
                                    "FOGLALAS_PK": "993",
                                    "mettol": "2016-06-30",
                                    "meddig": "2016-07-07",
                                    "idotartam": "7",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "197",
                                    "FOGLALAS_PK": "764",
                                    "mettol": "2016-08-09",
                                    "meddig": "2016-08-16",
                                    "idotartam": "7",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "197",
                                    "FOGLALAS_PK": "1091",
                                    "mettol": "2016-09-30",
                                    "meddig": "2016-10-07",
                                    "idotartam": "7",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "197",
                                    "FOGLALAS_PK": "1172",
                                    "mettol": "2016-10-20",
                                    "meddig": "2016-10-27",
                                    "idotartam": "7",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "197",
                                    "FOGLALAS_PK": "1304",
                                    "mettol": "2016-11-22",
                                    "meddig": "2016-11-29",
                                    "idotartam": "7",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "197",
                                    "FOGLALAS_PK": "1387",
                                    "mettol": "2016-12-24",
                                    "meddig": "2016-12-27",
                                    "idotartam": "3",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "198",
                                    "FOGLALAS_PK": "978",
                                    "mettol": "2016-06-22",
                                    "meddig": "2016-06-23",
                                    "idotartam": "1",
                                    "(No column name)": "0"
                                },
                                {
                                    "SZOBA_FK": "198",
                                    "FOGLALAS_PK": "1011",
                                    "mettol": "2016-07-04",
                                    "meddig": "2016-07-11",
                                    "idotartam": "7",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "198",
                                    "FOGLALAS_PK": "1065",
                                    "mettol": "2016-09-18",
                                    "meddig": "2016-09-21",
                                    "idotartam": "3",
                                    "(No column name)": "7"
                                },
                                {
                                    "SZOBA_FK": "198",
                                    "FOGLALAS_PK": "1116",
                                    "mettol": "2016-10-03",
                                    "meddig": "2016-10-04",
                                    "idotartam": "1",
                                    "(No column name)": "3"
                                },
                                {
                                    "SZOBA_FK": "198",
                                    "FOGLALAS_PK": "1138",
                                    "mettol": "2016-10-09",
                                    "meddig": "2016-10-14",
                                    "idotartam": "5",
                                    "(No column name)": "1"
                                },
                                {
                                    "SZOBA_FK": "198",
                                    "FOGLALAS_PK": "1161",
                                    "mettol": "2016-10-17",
                                    "meddig": "2016-10-22",
                                    "idotartam": "5",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "198",
                                    "FOGLALAS_PK": "1216",
                                    "mettol": "2016-10-29",
                                    "meddig": "2016-11-05",
                                    "idotartam": "7",
                                    "(No column name)": "5"
                                },
                                {
                                    "SZOBA_FK": "198",
                                    "FOGLALAS_PK": "1420",
                                    "mettol": "2017-01-05",
                                    "meddig": "2017-01-10",
                                    "idotartam": "5",
                                    "(No column name)": "7"
                                }
                            ]
                        },
                        "text/html": "<table><tr><th>SZOBA_FK</th><th>FOGLALAS_PK</th><th>mettol</th><th>meddig</th><th>idotartam</th><th>(No column name)</th></tr><tr><td>1</td><td>620</td><td>2016-05-05</td><td>2016-05-10</td><td>5</td><td>0</td></tr><tr><td>1</td><td>949</td><td>2016-06-10</td><td>2016-06-11</td><td>1</td><td>5</td></tr><tr><td>1</td><td>738</td><td>2016-07-30</td><td>2016-08-06</td><td>7</td><td>1</td></tr><tr><td>1</td><td>803</td><td>2016-08-20</td><td>2016-08-24</td><td>4</td><td>7</td></tr><tr><td>1</td><td>1137</td><td>2016-10-09</td><td>2016-10-11</td><td>2</td><td>4</td></tr><tr><td>1</td><td>1152</td><td>2016-10-15</td><td>2016-10-16</td><td>1</td><td>2</td></tr><tr><td>1</td><td>1274</td><td>2016-11-11</td><td>2016-11-12</td><td>1</td><td>1</td></tr><tr><td>1</td><td>1334</td><td>2016-12-01</td><td>2016-12-05</td><td>4</td><td>1</td></tr><tr><td>2</td><td>828</td><td>2016-08-27</td><td>2016-08-30</td><td>3</td><td>0</td></tr><tr><td>2</td><td>1051</td><td>2016-09-14</td><td>2016-09-15</td><td>1</td><td>3</td></tr><tr><td>2</td><td>1069</td><td>2016-09-19</td><td>2016-09-26</td><td>7</td><td>1</td></tr><tr><td>2</td><td>1311</td><td>2016-11-23</td><td>2016-11-30</td><td>7</td><td>7</td></tr><tr><td>3</td><td>629</td><td>2016-05-09</td><td>2016-05-13</td><td>4</td><td>0</td></tr><tr><td>3</td><td>666</td><td>2016-07-13</td><td>2016-07-19</td><td>6</td><td>4</td></tr><tr><td>3</td><td>788</td><td>2016-08-16</td><td>2016-08-22</td><td>6</td><td>6</td></tr><tr><td>3</td><td>1038</td><td>2016-09-08</td><td>2016-09-11</td><td>3</td><td>6</td></tr><tr><td>3</td><td>1110</td><td>2016-10-01</td><td>2016-10-08</td><td>7</td><td>3</td></tr><tr><td>3</td><td>1151</td><td>2016-10-14</td><td>2016-10-15</td><td>1</td><td>7</td></tr><tr><td>3</td><td>1434</td><td>2017-01-12</td><td>2017-01-17</td><td>5</td><td>1</td></tr><tr><td>3</td><td>1544</td><td>2017-02-16</td><td>2017-02-21</td><td>5</td><td>5</td></tr><tr><td>4</td><td>651</td><td>2016-05-17</td><td>2016-05-24</td><td>7</td><td>0</td></tr><tr><td>4</td><td>946</td><td>2016-06-10</td><td>2016-06-15</td><td>5</td><td>7</td></tr><tr><td>4</td><td>1001</td><td>2016-07-02</td><td>2016-07-09</td><td>7</td><td>5</td></tr><tr><td>4</td><td>1127</td><td>2016-10-07</td><td>2016-10-10</td><td>3</td><td>7</td></tr><tr><td>4</td><td>1132</td><td>2016-10-08</td><td>2016-10-14</td><td>6</td><td>3</td></tr><tr><td>4</td><td>1492</td><td>2017-02-03</td><td>2017-02-09</td><td>6</td><td>6</td></tr><tr><td>5</td><td>564</td><td>2016-04-08</td><td>2016-04-10</td><td>2</td><td>0</td></tr><tr><td>5</td><td>965</td><td>2016-06-16</td><td>2016-06-23</td><td>7</td><td>2</td></tr><tr><td>5</td><td>1073</td><td>2016-09-21</td><td>2016-09-26</td><td>5</td><td>7</td></tr><tr><td>5</td><td>1257</td><td>2016-11-07</td><td>2016-11-10</td><td>3</td><td>5</td></tr><tr><td>6</td><td>560</td><td>2016-04-06</td><td>2016-04-12</td><td>6</td><td>0</td></tr><tr><td>6</td><td>873</td><td>2016-05-29</td><td>2016-06-01</td><td>3</td><td>6</td></tr><tr><td>6</td><td>990</td><td>2016-06-27</td><td>2016-07-01</td><td>4</td><td>3</td></tr><tr><td>6</td><td>772</td><td>2016-08-12</td><td>2016-08-18</td><td>6</td><td>4</td></tr><tr><td>6</td><td>850</td><td>2016-09-05</td><td>2016-09-07</td><td>2</td><td>6</td></tr><tr><td>6</td><td>1099</td><td>2016-10-01</td><td>2016-10-05</td><td>4</td><td>2</td></tr><tr><td>7</td><td>562</td><td>2016-04-06</td><td>2016-04-10</td><td>4</td><td>0</td></tr><tr><td>7</td><td>759</td><td>2016-08-06</td><td>2016-08-13</td><td>7</td><td>4</td></tr><tr><td>7</td><td>1131</td><td>2016-10-08</td><td>2016-10-09</td><td>1</td><td>7</td></tr><tr><td>7</td><td>1175</td><td>2016-10-21</td><td>2016-10-25</td><td>4</td><td>1</td></tr><tr><td>7</td><td>1182</td><td>2016-10-23</td><td>2016-10-27</td><td>4</td><td>4</td></tr><tr><td>7</td><td>1252</td><td>2016-11-05</td><td>2016-11-07</td><td>2</td><td>4</td></tr><tr><td>8</td><td>882</td><td>2016-05-30</td><td>2016-05-31</td><td>1</td><td>0</td></tr><tr><td>8</td><td>947</td><td>2016-06-10</td><td>2016-06-13</td><td>3</td><td>1</td></tr><tr><td>8</td><td>694</td><td>2016-07-20</td><td>2016-07-24</td><td>4</td><td>3</td></tr><tr><td>8</td><td>818</td><td>2016-08-24</td><td>2016-08-28</td><td>4</td><td>4</td></tr><tr><td>8</td><td>832</td><td>2016-08-28</td><td>2016-09-01</td><td>4</td><td>4</td></tr><tr><td>9</td><td>609</td><td>2016-04-29</td><td>2016-05-01</td><td>2</td><td>0</td></tr><tr><td>9</td><td>1157</td><td>2016-10-15</td><td>2016-10-21</td><td>6</td><td>2</td></tr><tr><td>9</td><td>1220</td><td>2016-10-30</td><td>2016-11-02</td><td>3</td><td>6</td></tr><tr><td>9</td><td>1260</td><td>2016-11-07</td><td>2016-11-13</td><td>6</td><td>3</td></tr><tr><td>9</td><td>1423</td><td>2017-01-06</td><td>2017-01-09</td><td>3</td><td>6</td></tr><tr><td>9</td><td>1537</td><td>2017-02-16</td><td>2017-02-19</td><td>3</td><td>3</td></tr><tr><td>10</td><td>569</td><td>2016-04-10</td><td>2016-04-13</td><td>3</td><td>0</td></tr><tr><td>10</td><td>790</td><td>2016-08-16</td><td>2016-08-21</td><td>5</td><td>3</td></tr><tr><td>10</td><td>795</td><td>2016-08-17</td><td>2016-08-21</td><td>4</td><td>5</td></tr><tr><td>10</td><td>1319</td><td>2016-11-25</td><td>2016-12-01</td><td>6</td><td>4</td></tr><tr><td>11</td><td>918</td><td>2016-06-06</td><td>2016-06-12</td><td>6</td><td>0</td></tr><tr><td>11</td><td>1123</td><td>2016-10-05</td><td>2016-10-10</td><td>5</td><td>6</td></tr><tr><td>11</td><td>1236</td><td>2016-11-01</td><td>2016-11-02</td><td>1</td><td>5</td></tr><tr><td>11</td><td>1523</td><td>2017-02-12</td><td>2017-02-13</td><td>1</td><td>1</td></tr><tr><td>12</td><td>876</td><td>2016-05-30</td><td>2016-06-06</td><td>7</td><td>0</td></tr><tr><td>12</td><td>951</td><td>2016-06-11</td><td>2016-06-14</td><td>3</td><td>7</td></tr><tr><td>12</td><td>970</td><td>2016-06-17</td><td>2016-06-19</td><td>2</td><td>3</td></tr><tr><td>12</td><td>1020</td><td>2016-07-09</td><td>2016-07-14</td><td>5</td><td>2</td></tr><tr><td>12</td><td>697</td><td>2016-07-20</td><td>2016-07-22</td><td>2</td><td>5</td></tr><tr><td>12</td><td>775</td><td>2016-08-13</td><td>2016-08-17</td><td>4</td><td>2</td></tr><tr><td>12</td><td>1140</td><td>2016-10-09</td><td>2016-10-12</td><td>3</td><td>4</td></tr><tr><td>12</td><td>1164</td><td>2016-10-18</td><td>2016-10-23</td><td>5</td><td>3</td></tr><tr><td>12</td><td>1430</td><td>2017-01-09</td><td>2017-01-11</td><td>2</td><td>5</td></tr><tr><td>13</td><td>763</td><td>2016-08-08</td><td>2016-08-12</td><td>4</td><td>0</td></tr><tr><td>13</td><td>1044</td><td>2016-09-12</td><td>2016-09-18</td><td>6</td><td>4</td></tr><tr><td>13</td><td>1347</td><td>2016-12-06</td><td>2016-12-09</td><td>3</td><td>6</td></tr><tr><td>13</td><td>1469</td><td>2017-01-23</td><td>2017-01-25</td><td>2</td><td>3</td></tr><tr><td>14</td><td>663</td><td>2016-05-22</td><td>2016-05-23</td><td>1</td><td>0</td></tr><tr><td>14</td><td>813</td><td>2016-08-24</td><td>2016-08-27</td><td>3</td><td>1</td></tr><tr><td>14</td><td>1542</td><td>2017-02-16</td><td>2017-02-20</td><td>4</td><td>3</td></tr><tr><td>15</td><td>1028</td><td>2016-07-13</td><td>2016-07-15</td><td>2</td><td>0</td></tr><tr><td>15</td><td>791</td><td>2016-08-16</td><td>2016-08-21</td><td>5</td><td>2</td></tr><tr><td>15</td><td>1129</td><td>2016-10-08</td><td>2016-10-12</td><td>4</td><td>5</td></tr><tr><td>15</td><td>1244</td><td>2016-11-03</td><td>2016-11-04</td><td>1</td><td>4</td></tr><tr><td>15</td><td>1418</td><td>2017-01-04</td><td>2017-01-08</td><td>4</td><td>1</td></tr><tr><td>15</td><td>1442</td><td>2017-01-16</td><td>2017-01-19</td><td>3</td><td>4</td></tr><tr><td>16</td><td>856</td><td>2016-05-24</td><td>2016-05-30</td><td>6</td><td>0</td></tr><tr><td>16</td><td>896</td><td>2016-06-03</td><td>2016-06-04</td><td>1</td><td>6</td></tr><tr><td>16</td><td>973</td><td>2016-06-20</td><td>2016-06-21</td><td>1</td><td>1</td></tr><tr><td>16</td><td>687</td><td>2016-07-18</td><td>2016-07-21</td><td>3</td><td>1</td></tr><tr><td>16</td><td>1498</td><td>2017-02-04</td><td>2017-02-11</td><td>7</td><td>3</td></tr><tr><td>17</td><td>602</td><td>2016-04-26</td><td>2016-05-02</td><td>6</td><td>0</td></tr><tr><td>17</td><td>916</td><td>2016-06-06</td><td>2016-06-08</td><td>2</td><td>6</td></tr><tr><td>17</td><td>713</td><td>2016-07-24</td><td>2016-07-30</td><td>6</td><td>2</td></tr><tr><td>17</td><td>744</td><td>2016-08-01</td><td>2016-08-02</td><td>1</td><td>6</td></tr><tr><td>17</td><td>1316</td><td>2016-11-25</td><td>2016-11-30</td><td>5</td><td>1</td></tr><tr><td>17</td><td>1549</td><td>2017-02-18</td><td>2017-02-21</td><td>3</td><td>5</td></tr><tr><td>18</td><td>626</td><td>2016-05-08</td><td>2016-05-11</td><td>3</td><td>0</td></tr><tr><td>18</td><td>767</td><td>2016-08-11</td><td>2016-08-14</td><td>3</td><td>3</td></tr><tr><td>18</td><td>1035</td><td>2016-09-07</td><td>2016-09-13</td><td>6</td><td>3</td></tr><tr><td>18</td><td>1173</td><td>2016-10-21</td><td>2016-10-27</td><td>6</td><td>6</td></tr><tr><td>18</td><td>1198</td><td>2016-10-26</td><td>2016-10-30</td><td>4</td><td>6</td></tr><tr><td>18</td><td>1505</td><td>2017-02-06</td><td>2017-02-12</td><td>6</td><td>4</td></tr><tr><td>19</td><td>948</td><td>2016-06-10</td><td>2016-06-12</td><td>2</td><td>0</td></tr><tr><td>19</td><td>696</td><td>2016-07-20</td><td>2016-07-21</td><td>1</td><td>2</td></tr><tr><td>19</td><td>778</td><td>2016-08-14</td><td>2016-08-15</td><td>1</td><td>1</td></tr><tr><td>19</td><td>1139</td><td>2016-10-09</td><td>2016-10-16</td><td>7</td><td>1</td></tr><tr><td>19</td><td>1237</td><td>2016-11-02</td><td>2016-11-03</td><td>1</td><td>7</td></tr><tr><td>19</td><td>1533</td><td>2017-02-14</td><td>2017-02-15</td><td>1</td><td>1</td></tr><tr><td>20</td><td>755</td><td>2016-08-04</td><td>2016-08-10</td><td>6</td><td>0</td></tr><tr><td>20</td><td>820</td><td>2016-08-24</td><td>2016-08-25</td><td>1</td><td>6</td></tr><tr><td>20</td><td>1070</td><td>2016-09-19</td><td>2016-09-20</td><td>1</td><td>1</td></tr><tr><td>20</td><td>1114</td><td>2016-10-01</td><td>2016-10-06</td><td>5</td><td>1</td></tr><tr><td>20</td><td>1106</td><td>2016-10-01</td><td>2016-10-03</td><td>2</td><td>5</td></tr><tr><td>21</td><td>566</td><td>2016-04-09</td><td>2016-04-15</td><td>6</td><td>0</td></tr><tr><td>21</td><td>660</td><td>2016-05-21</td><td>2016-05-26</td><td>5</td><td>6</td></tr><tr><td>21</td><td>805</td><td>2016-08-21</td><td>2016-08-22</td><td>1</td><td>5</td></tr><tr><td>21</td><td>1212</td><td>2016-10-28</td><td>2016-11-03</td><td>6</td><td>1</td></tr><tr><td>22</td><td>906</td><td>2016-06-04</td><td>2016-06-05</td><td>1</td><td>0</td></tr><tr><td>22</td><td>1005</td><td>2016-07-03</td><td>2016-07-06</td><td>3</td><td>1</td></tr><tr><td>22</td><td>1130</td><td>2016-10-08</td><td>2016-10-09</td><td>1</td><td>3</td></tr><tr><td>22</td><td>1195</td><td>2016-10-26</td><td>2016-11-01</td><td>6</td><td>1</td></tr><tr><td>22</td><td>1206</td><td>2016-10-27</td><td>2016-11-03</td><td>7</td><td>6</td></tr><tr><td>22</td><td>1287</td><td>2016-11-17</td><td>2016-11-20</td><td>3</td><td>7</td></tr><tr><td>23</td><td>934</td><td>2016-06-08</td><td>2016-06-09</td><td>1</td><td>0</td></tr><tr><td>23</td><td>945</td><td>2016-06-10</td><td>2016-06-17</td><td>7</td><td>1</td></tr><tr><td>23</td><td>848</td><td>2016-09-04</td><td>2016-09-05</td><td>1</td><td>7</td></tr><tr><td>24</td><td>852</td><td>2016-05-23</td><td>2016-05-25</td><td>2</td><td>0</td></tr><tr><td>24</td><td>1167</td><td>2016-10-19</td><td>2016-10-20</td><td>1</td><td>2</td></tr><tr><td>24</td><td>1415</td><td>2017-01-03</td><td>2017-01-06</td><td>3</td><td>1</td></tr><tr><td>25</td><td>1052</td><td>2016-09-14</td><td>2016-09-17</td><td>3</td><td>0</td></tr><tr><td>25</td><td>1362</td><td>2016-12-14</td><td>2016-12-16</td><td>2</td><td>3</td></tr><tr><td>26</td><td>1158</td><td>2016-10-16</td><td>2016-10-18</td><td>2</td><td>0</td></tr><tr><td>26</td><td>1388</td><td>2016-12-24</td><td>2016-12-27</td><td>3</td><td>2</td></tr><tr><td>27</td><td>758</td><td>2016-08-05</td><td>2016-08-08</td><td>3</td><td>0</td></tr><tr><td>27</td><td>807</td><td>2016-08-22</td><td>2016-08-24</td><td>2</td><td>3</td></tr><tr><td>27</td><td>1031</td><td>2016-09-05</td><td>2016-09-07</td><td>2</td><td>2</td></tr><tr><td>27</td><td>1082</td><td>2016-09-26</td><td>2016-10-01</td><td>5</td><td>2</td></tr><tr><td>27</td><td>1275</td><td>2016-11-11</td><td>2016-11-17</td><td>6</td><td>5</td></tr><tr><td>27</td><td>1377</td><td>2016-12-18</td><td>2016-12-19</td><td>1</td><td>6</td></tr><tr><td>27</td><td>1476</td><td>2017-01-27</td><td>2017-01-28</td><td>1</td><td>1</td></tr><tr><td>28</td><td>872</td><td>2016-05-29</td><td>2016-06-03</td><td>5</td><td>0</td></tr><tr><td>28</td><td>886</td><td>2016-06-01</td><td>2016-06-05</td><td>4</td><td>5</td></tr><tr><td>28</td><td>901</td><td>2016-06-04</td><td>2016-06-08</td><td>4</td><td>4</td></tr><tr><td>28</td><td>725</td><td>2016-07-27</td><td>2016-08-01</td><td>5</td><td>4</td></tr><tr><td>28</td><td>1150</td><td>2016-10-13</td><td>2016-10-19</td><td>6</td><td>5</td></tr><tr><td>28</td><td>1459</td><td>2017-01-20</td><td>2017-01-22</td><td>2</td><td>6</td></tr><tr><td>29</td><td>611</td><td>2016-05-01</td><td>2016-05-06</td><td>5</td><td>0</td></tr><tr><td>29</td><td>894</td><td>2016-06-03</td><td>2016-06-04</td><td>1</td><td>5</td></tr><tr><td>29</td><td>1076</td><td>2016-09-23</td><td>2016-09-30</td><td>7</td><td>1</td></tr><tr><td>29</td><td>1185</td><td>2016-10-23</td><td>2016-10-28</td><td>5</td><td>7</td></tr><tr><td>29</td><td>1235</td><td>2016-11-01</td><td>2016-11-08</td><td>7</td><td>5</td></tr><tr><td>29</td><td>1568</td><td>2017-02-24</td><td>2017-03-03</td><td>7</td><td>7</td></tr><tr><td>30</td><td>604</td><td>2016-04-27</td><td>2016-04-29</td><td>2</td><td>0</td></tr><tr><td>30</td><td>1023</td><td>2016-07-10</td><td>2016-07-17</td><td>7</td><td>2</td></tr><tr><td>30</td><td>1136</td><td>2016-10-09</td><td>2016-10-14</td><td>5</td><td>7</td></tr><tr><td>31</td><td>598</td><td>2016-04-24</td><td>2016-04-26</td><td>2</td><td>0</td></tr><tr><td>31</td><td>606</td><td>2016-04-27</td><td>2016-04-28</td><td>1</td><td>2</td></tr><tr><td>31</td><td>728</td><td>2016-07-27</td><td>2016-07-31</td><td>4</td><td>1</td></tr><tr><td>32</td><td>920</td><td>2016-06-06</td><td>2016-06-10</td><td>4</td><td>0</td></tr><tr><td>33</td><td>624</td><td>2016-05-08</td><td>2016-05-14</td><td>6</td><td>0</td></tr><tr><td>33</td><td>1012</td><td>2016-07-05</td><td>2016-07-12</td><td>7</td><td>6</td></tr><tr><td>33</td><td>1053</td><td>2016-09-15</td><td>2016-09-16</td><td>1</td><td>7</td></tr><tr><td>33</td><td>1321</td><td>2016-11-25</td><td>2016-11-29</td><td>4</td><td>1</td></tr><tr><td>33</td><td>1344</td><td>2016-12-05</td><td>2016-12-10</td><td>5</td><td>4</td></tr><tr><td>33</td><td>1381</td><td>2016-12-21</td><td>2016-12-27</td><td>6</td><td>5</td></tr><tr><td>34</td><td>870</td><td>2016-05-28</td><td>2016-06-03</td><td>6</td><td>0</td></tr><tr><td>34</td><td>904</td><td>2016-06-04</td><td>2016-06-06</td><td>2</td><td>6</td></tr><tr><td>34</td><td>777</td><td>2016-08-14</td><td>2016-08-17</td><td>3</td><td>2</td></tr><tr><td>34</td><td>821</td><td>2016-08-24</td><td>2016-08-25</td><td>1</td><td>3</td></tr><tr><td>35</td><td>971</td><td>2016-06-18</td><td>2016-06-21</td><td>3</td><td>0</td></tr><tr><td>35</td><td>979</td><td>2016-06-22</td><td>2016-06-29</td><td>7</td><td>3</td></tr><tr><td>35</td><td>686</td><td>2016-07-18</td><td>2016-07-24</td><td>6</td><td>7</td></tr><tr><td>35</td><td>707</td><td>2016-07-23</td><td>2016-07-25</td><td>2</td><td>6</td></tr><tr><td>35</td><td>829</td><td>2016-08-28</td><td>2016-08-30</td><td>2</td><td>2</td></tr><tr><td>35</td><td>1480</td><td>2016-12-29</td><td>2017-02-04</td><td>37</td><td>2</td></tr><tr><td>35</td><td>1411</td><td>2017-01-01</td><td>2017-01-02</td><td>1</td><td>37</td></tr><tr><td>35</td><td>1436</td><td>2017-01-13</td><td>2017-01-14</td><td>1</td><td>1</td></tr><tr><td>35</td><td>1529</td><td>2017-02-13</td><td>2017-02-17</td><td>4</td><td>1</td></tr><tr><td>36</td><td>895</td><td>2016-06-03</td><td>2016-06-08</td><td>5</td><td>0</td></tr><tr><td>36</td><td>919</td><td>2016-06-06</td><td>2016-06-07</td><td>1</td><td>5</td></tr><tr><td>36</td><td>985</td><td>2016-06-24</td><td>2016-06-30</td><td>6</td><td>1</td></tr><tr><td>36</td><td>1003</td><td>2016-07-03</td><td>2016-07-07</td><td>4</td><td>6</td></tr><tr><td>36</td><td>748</td><td>2016-08-02</td><td>2016-08-04</td><td>2</td><td>4</td></tr><tr><td>36</td><td>750</td><td>2016-08-03</td><td>2016-08-09</td><td>6</td><td>2</td></tr><tr><td>37</td><td>688</td><td>2016-07-19</td><td>2016-07-21</td><td>2</td><td>0</td></tr><tr><td>37</td><td>705</td><td>2016-07-22</td><td>2016-07-26</td><td>4</td><td>2</td></tr><tr><td>37</td><td>1335</td><td>2016-12-01</td><td>2016-12-08</td><td>7</td><td>4</td></tr><tr><td>38</td><td>627</td><td>2016-05-08</td><td>2016-05-14</td><td>6</td><td>0</td></tr><tr><td>38</td><td>1033</td><td>2016-09-05</td><td>2016-09-07</td><td>2</td><td>6</td></tr><tr><td>38</td><td>1060</td><td>2016-09-17</td><td>2016-09-19</td><td>2</td><td>2</td></tr><tr><td>38</td><td>1078</td><td>2016-09-23</td><td>2016-09-30</td><td>7</td><td>2</td></tr><tr><td>38</td><td>1351</td><td>2016-12-06</td><td>2016-12-10</td><td>4</td><td>7</td></tr><tr><td>38</td><td>1416</td><td>2017-01-03</td><td>2017-01-08</td><td>5</td><td>4</td></tr><tr><td>38</td><td>1478</td><td>2017-01-28</td><td>2017-02-01</td><td>4</td><td>5</td></tr><tr><td>38</td><td>1556</td><td>2017-02-21</td><td>2017-02-27</td><td>6</td><td>4</td></tr><tr><td>39</td><td>601</td><td>2016-04-25</td><td>2016-05-01</td><td>6</td><td>0</td></tr><tr><td>39</td><td>899</td><td>2016-06-03</td><td>2016-06-09</td><td>6</td><td>6</td></tr><tr><td>39</td><td>1214</td><td>2016-10-29</td><td>2016-11-03</td><td>5</td><td>6</td></tr><tr><td>39</td><td>1380</td><td>2016-12-20</td><td>2016-12-25</td><td>5</td><td>5</td></tr><tr><td>39</td><td>1435</td><td>2017-01-12</td><td>2017-01-19</td><td>7</td><td>5</td></tr><tr><td>39</td><td>1454</td><td>2017-01-18</td><td>2017-01-19</td><td>1</td><td>7</td></tr><tr><td>39</td><td>1538</td><td>2017-02-16</td><td>2017-02-18</td><td>2</td><td>1</td></tr><tr><td>40</td><td>924</td><td>2016-06-07</td><td>2016-06-12</td><td>5</td><td>0</td></tr><tr><td>40</td><td>932</td><td>2016-06-07</td><td>2016-06-13</td><td>6</td><td>5</td></tr><tr><td>40</td><td>1018</td><td>2016-07-08</td><td>2016-07-13</td><td>5</td><td>6</td></tr><tr><td>40</td><td>1118</td><td>2016-10-03</td><td>2016-10-08</td><td>5</td><td>5</td></tr><tr><td>41</td><td>960</td><td>2016-06-15</td><td>2016-06-21</td><td>6</td><td>0</td></tr><tr><td>41</td><td>1144</td><td>2016-10-09</td><td>2016-10-10</td><td>1</td><td>6</td></tr><tr><td>42</td><td>561</td><td>2016-04-06</td><td>2016-04-10</td><td>4</td><td>0</td></tr><tr><td>42</td><td>590</td><td>2016-04-19</td><td>2016-04-24</td><td>5</td><td>4</td></tr><tr><td>42</td><td>851</td><td>2016-05-22</td><td>2016-05-29</td><td>7</td><td>5</td></tr><tr><td>42</td><td>770</td><td>2016-08-12</td><td>2016-08-15</td><td>3</td><td>7</td></tr><tr><td>42</td><td>1309</td><td>2016-11-23</td><td>2016-11-25</td><td>2</td><td>3</td></tr><tr><td>42</td><td>1444</td><td>2017-01-16</td><td>2017-01-22</td><td>6</td><td>2</td></tr><tr><td>43</td><td>1019</td><td>2016-07-08</td><td>2016-07-12</td><td>4</td><td>0</td></tr><tr><td>43</td><td>670</td><td>2016-07-14</td><td>2016-07-18</td><td>4</td><td>4</td></tr><tr><td>43</td><td>1088</td><td>2016-09-29</td><td>2016-10-01</td><td>2</td><td>4</td></tr><tr><td>43</td><td>1207</td><td>2016-10-27</td><td>2016-10-28</td><td>1</td><td>2</td></tr><tr><td>43</td><td>1227</td><td>2016-10-30</td><td>2016-11-04</td><td>5</td><td>1</td></tr><tr><td>43</td><td>1270</td><td>2016-11-10</td><td>2016-11-14</td><td>4</td><td>5</td></tr><tr><td>43</td><td>1524</td><td>2017-02-12</td><td>2017-02-13</td><td>1</td><td>4</td></tr><tr><td>43</td><td>1553</td><td>2017-02-20</td><td>2017-02-25</td><td>5</td><td>1</td></tr><tr><td>44</td><td>589</td><td>2016-04-19</td><td>2016-04-21</td><td>2</td><td>0</td></tr><tr><td>44</td><td>658</td><td>2016-05-21</td><td>2016-05-27</td><td>6</td><td>2</td></tr><tr><td>44</td><td>823</td><td>2016-08-25</td><td>2016-08-27</td><td>2</td><td>6</td></tr><tr><td>44</td><td>1295</td><td>2016-11-19</td><td>2016-11-21</td><td>2</td><td>2</td></tr><tr><td>44</td><td>1425</td><td>2017-01-08</td><td>2017-01-10</td><td>2</td><td>2</td></tr><tr><td>44</td><td>1552</td><td>2017-02-20</td><td>2017-02-22</td><td>2</td><td>2</td></tr><tr><td>45</td><td>802</td><td>2016-08-20</td><td>2016-08-27</td><td>7</td><td>0</td></tr><tr><td>45</td><td>800</td><td>2016-08-20</td><td>2016-08-25</td><td>5</td><td>7</td></tr><tr><td>45</td><td>846</td><td>2016-09-02</td><td>2016-09-05</td><td>3</td><td>5</td></tr><tr><td>45</td><td>1135</td><td>2016-10-09</td><td>2016-10-12</td><td>3</td><td>3</td></tr><tr><td>45</td><td>1303</td><td>2016-11-22</td><td>2016-11-24</td><td>2</td><td>3</td></tr><tr><td>46</td><td>752</td><td>2016-08-03</td><td>2016-08-08</td><td>5</td><td>0</td></tr><tr><td>46</td><td>1187</td><td>2016-10-23</td><td>2016-10-30</td><td>7</td><td>5</td></tr><tr><td>46</td><td>1291</td><td>2016-11-19</td><td>2016-11-22</td><td>3</td><td>7</td></tr><tr><td>46</td><td>1515</td><td>2017-02-10</td><td>2017-02-14</td><td>4</td><td>3</td></tr><tr><td>47</td><td>955</td><td>2016-06-13</td><td>2016-06-14</td><td>1</td><td>0</td></tr><tr><td>47</td><td>1056</td><td>2016-09-16</td><td>2016-09-23</td><td>7</td><td>1</td></tr><tr><td>48</td><td>603</td><td>2016-04-26</td><td>2016-04-29</td><td>3</td><td>0</td></tr><tr><td>48</td><td>628</td><td>2016-05-09</td><td>2016-05-11</td><td>2</td><td>3</td></tr><tr><td>48</td><td>914</td><td>2016-06-06</td><td>2016-06-11</td><td>5</td><td>2</td></tr><tr><td>48</td><td>986</td><td>2016-06-25</td><td>2016-06-30</td><td>5</td><td>5</td></tr><tr><td>48</td><td>824</td><td>2016-08-25</td><td>2016-08-27</td><td>2</td><td>5</td></tr><tr><td>48</td><td>1243</td><td>2016-11-03</td><td>2016-11-09</td><td>6</td><td>2</td></tr><tr><td>48</td><td>1546</td><td>2017-02-17</td><td>2017-02-20</td><td>3</td><td>6</td></tr><tr><td>48</td><td>1547</td><td>2017-02-18</td><td>2017-02-19</td><td>1</td><td>3</td></tr><tr><td>48</td><td>1581</td><td>2017-03-01</td><td>2017-03-06</td><td>5</td><td>1</td></tr><tr><td>49</td><td>888</td><td>2016-06-02</td><td>2016-06-09</td><td>7</td><td>0</td></tr><tr><td>49</td><td>793</td><td>2016-08-17</td><td>2016-08-23</td><td>6</td><td>7</td></tr><tr><td>49</td><td>826</td><td>2016-08-26</td><td>2016-08-30</td><td>4</td><td>6</td></tr><tr><td>49</td><td>1066</td><td>2016-09-18</td><td>2016-09-25</td><td>7</td><td>4</td></tr><tr><td>49</td><td>1200</td><td>2016-10-26</td><td>2016-11-02</td><td>7</td><td>7</td></tr><tr><td>49</td><td>1221</td><td>2016-10-30</td><td>2016-11-01</td><td>2</td><td>7</td></tr><tr><td>49</td><td>1536</td><td>2017-02-16</td><td>2017-02-22</td><td>6</td><td>2</td></tr><tr><td>50</td><td>787</td><td>2016-08-16</td><td>2016-08-19</td><td>3</td><td>0</td></tr><tr><td>50</td><td>1063</td><td>2016-09-18</td><td>2016-09-20</td><td>2</td><td>3</td></tr><tr><td>50</td><td>1224</td><td>2016-10-30</td><td>2016-10-31</td><td>1</td><td>2</td></tr><tr><td>50</td><td>1272</td><td>2016-11-10</td><td>2016-11-11</td><td>1</td><td>1</td></tr><tr><td>51</td><td>865</td><td>2016-05-28</td><td>2016-06-04</td><td>7</td><td>0</td></tr><tr><td>51</td><td>811</td><td>2016-08-23</td><td>2016-08-25</td><td>2</td><td>7</td></tr><tr><td>51</td><td>1165</td><td>2016-10-19</td><td>2016-10-24</td><td>5</td><td>2</td></tr><tr><td>51</td><td>1477</td><td>2017-01-28</td><td>2017-02-03</td><td>6</td><td>5</td></tr><tr><td>51</td><td>1550</td><td>2017-02-18</td><td>2017-02-19</td><td>1</td><td>6</td></tr><tr><td>52</td><td>822</td><td>2016-08-24</td><td>2016-08-31</td><td>7</td><td>0</td></tr><tr><td>52</td><td>1202</td><td>2016-10-26</td><td>2016-10-28</td><td>2</td><td>7</td></tr><tr><td>52</td><td>1258</td><td>2016-11-07</td><td>2016-11-12</td><td>5</td><td>2</td></tr><tr><td>52</td><td>1431</td><td>2017-01-10</td><td>2017-01-15</td><td>5</td><td>5</td></tr><tr><td>52</td><td>1534</td><td>2017-02-14</td><td>2017-02-19</td><td>5</td><td>5</td></tr><tr><td>53</td><td>855</td><td>2016-05-24</td><td>2016-05-25</td><td>1</td><td>0</td></tr><tr><td>53</td><td>987</td><td>2016-06-26</td><td>2016-06-30</td><td>4</td><td>1</td></tr><tr><td>54</td><td>622</td><td>2016-05-07</td><td>2016-05-14</td><td>7</td><td>0</td></tr><tr><td>54</td><td>642</td><td>2016-05-13</td><td>2016-05-18</td><td>5</td><td>7</td></tr><tr><td>54</td><td>889</td><td>2016-06-02</td><td>2016-06-04</td><td>2</td><td>5</td></tr><tr><td>54</td><td>668</td><td>2016-07-14</td><td>2016-07-15</td><td>1</td><td>2</td></tr><tr><td>54</td><td>1096</td><td>2016-09-30</td><td>2016-10-04</td><td>4</td><td>1</td></tr><tr><td>54</td><td>1328</td><td>2016-11-28</td><td>2016-12-02</td><td>4</td><td>4</td></tr><tr><td>55</td><td>734</td><td>2016-07-28</td><td>2016-08-03</td><td>6</td><td>0</td></tr><tr><td>55</td><td>1086</td><td>2016-09-28</td><td>2016-10-03</td><td>5</td><td>6</td></tr><tr><td>55</td><td>1163</td><td>2016-10-17</td><td>2016-10-19</td><td>2</td><td>5</td></tr><tr><td>55</td><td>1232</td><td>2016-10-30</td><td>2016-11-06</td><td>7</td><td>2</td></tr><tr><td>55</td><td>1327</td><td>2016-11-28</td><td>2016-12-04</td><td>6</td><td>7</td></tr><tr><td>55</td><td>1386</td><td>2016-12-24</td><td>2016-12-26</td><td>2</td><td>6</td></tr><tr><td>55</td><td>1512</td><td>2017-02-08</td><td>2017-02-09</td><td>1</td><td>2</td></tr><tr><td>55</td><td>1520</td><td>2017-02-12</td><td>2017-02-13</td><td>1</td><td>1</td></tr><tr><td>56</td><td>935</td><td>2016-06-08</td><td>2016-06-12</td><td>4</td><td>0</td></tr><tr><td>56</td><td>838</td><td>2016-08-29</td><td>2016-08-31</td><td>2</td><td>4</td></tr><tr><td>57</td><td>1348</td><td>2016-12-06</td><td>2016-12-07</td><td>1</td><td>0</td></tr><tr><td>57</td><td>1389</td><td>2016-12-25</td><td>2016-12-26</td><td>1</td><td>1</td></tr><tr><td>57</td><td>1466</td><td>2017-01-22</td><td>2017-01-29</td><td>7</td><td>1</td></tr><tr><td>57</td><td>1504</td><td>2017-02-06</td><td>2017-02-10</td><td>4</td><td>7</td></tr><tr><td>58</td><td>883</td><td>2016-05-30</td><td>2016-06-04</td><td>5</td><td>0</td></tr><tr><td>58</td><td>719</td><td>2016-07-27</td><td>2016-07-30</td><td>3</td><td>5</td></tr><tr><td>58</td><td>773</td><td>2016-08-12</td><td>2016-08-14</td><td>2</td><td>3</td></tr><tr><td>58</td><td>1113</td><td>2016-10-01</td><td>2016-10-04</td><td>3</td><td>2</td></tr><tr><td>58</td><td>1186</td><td>2016-10-23</td><td>2016-10-29</td><td>6</td><td>3</td></tr><tr><td>58</td><td>1208</td><td>2016-10-28</td><td>2016-11-03</td><td>6</td><td>6</td></tr><tr><td>58</td><td>1255</td><td>2016-11-06</td><td>2016-11-13</td><td>7</td><td>6</td></tr><tr><td>58</td><td>1261</td><td>2016-11-07</td><td>2016-11-13</td><td>6</td><td>7</td></tr><tr><td>58</td><td>1285</td><td>2016-11-16</td><td>2016-11-23</td><td>7</td><td>6</td></tr><tr><td>58</td><td>1293</td><td>2016-11-19</td><td>2016-11-22</td><td>3</td><td>7</td></tr><tr><td>58</td><td>1307</td><td>2016-11-23</td><td>2016-11-29</td><td>6</td><td>3</td></tr><tr><td>58</td><td>1322</td><td>2016-11-26</td><td>2016-11-29</td><td>3</td><td>6</td></tr><tr><td>58</td><td>1451</td><td>2017-01-17</td><td>2017-01-23</td><td>6</td><td>3</td></tr><tr><td>59</td><td>1080</td><td>2016-09-25</td><td>2016-09-26</td><td>1</td><td>0</td></tr><tr><td>59</td><td>1084</td><td>2016-09-28</td><td>2016-09-30</td><td>2</td><td>1</td></tr><tr><td>59</td><td>1170</td><td>2016-10-20</td><td>2016-10-25</td><td>5</td><td>2</td></tr><tr><td>59</td><td>1191</td><td>2016-10-25</td><td>2016-10-31</td><td>6</td><td>5</td></tr><tr><td>59</td><td>1239</td><td>2016-11-03</td><td>2016-11-05</td><td>2</td><td>6</td></tr><tr><td>59</td><td>1288</td><td>2016-11-17</td><td>2016-11-20</td><td>3</td><td>2</td></tr><tr><td>59</td><td>1573</td><td>2017-02-26</td><td>2017-02-27</td><td>1</td><td>3</td></tr><tr><td>60</td><td>676</td><td>2016-07-16</td><td>2016-07-18</td><td>2</td><td>0</td></tr><tr><td>61</td><td>701</td><td>2016-07-21</td><td>2016-07-23</td><td>2</td><td>0</td></tr><tr><td>61</td><td>756</td><td>2016-08-05</td><td>2016-08-11</td><td>6</td><td>2</td></tr><tr><td>61</td><td>1148</td><td>2016-10-11</td><td>2016-10-14</td><td>3</td><td>6</td></tr><tr><td>61</td><td>1218</td><td>2016-10-29</td><td>2016-10-31</td><td>2</td><td>3</td></tr><tr><td>61</td><td>1496</td><td>2017-02-04</td><td>2017-02-11</td><td>7</td><td>2</td></tr><tr><td>62</td><td>936</td><td>2016-06-08</td><td>2016-06-11</td><td>3</td><td>0</td></tr><tr><td>62</td><td>938</td><td>2016-06-09</td><td>2016-06-10</td><td>1</td><td>3</td></tr><tr><td>62</td><td>702</td><td>2016-07-21</td><td>2016-07-26</td><td>5</td><td>1</td></tr><tr><td>62</td><td>1081</td><td>2016-09-26</td><td>2016-10-03</td><td>7</td><td>5</td></tr><tr><td>62</td><td>1426</td><td>2017-01-09</td><td>2017-01-13</td><td>4</td><td>7</td></tr><tr><td>63</td><td>625</td><td>2016-05-08</td><td>2016-05-11</td><td>3</td><td>0</td></tr><tr><td>63</td><td>891</td><td>2016-06-02</td><td>2016-06-08</td><td>6</td><td>3</td></tr><tr><td>63</td><td>769</td><td>2016-08-12</td><td>2016-08-17</td><td>5</td><td>6</td></tr><tr><td>63</td><td>845</td><td>2016-09-02</td><td>2016-09-03</td><td>1</td><td>5</td></tr><tr><td>64</td><td>875</td><td>2016-05-30</td><td>2016-06-01</td><td>2</td><td>0</td></tr><tr><td>64</td><td>1122</td><td>2016-10-05</td><td>2016-10-09</td><td>4</td><td>2</td></tr><tr><td>64</td><td>1233</td><td>2016-10-31</td><td>2016-11-07</td><td>7</td><td>4</td></tr><tr><td>64</td><td>1446</td><td>2017-01-16</td><td>2017-01-22</td><td>6</td><td>7</td></tr><tr><td>64</td><td>1465</td><td>2017-01-22</td><td>2017-01-26</td><td>4</td><td>6</td></tr><tr><td>64</td><td>1582</td><td>2017-03-02</td><td>2017-03-03</td><td>1</td><td>4</td></tr><tr><td>65</td><td>650</td><td>2016-05-17</td><td>2016-05-23</td><td>6</td><td>0</td></tr><tr><td>66</td><td>950</td><td>2016-06-10</td><td>2016-06-13</td><td>3</td><td>0</td></tr><tr><td>66</td><td>736</td><td>2016-07-29</td><td>2016-08-01</td><td>3</td><td>3</td></tr><tr><td>66</td><td>1234</td><td>2016-11-01</td><td>2016-11-04</td><td>3</td><td>3</td></tr><tr><td>66</td><td>1264</td><td>2016-11-08</td><td>2016-11-12</td><td>4</td><td>3</td></tr><tr><td>67</td><td>638</td><td>2016-05-12</td><td>2016-05-17</td><td>5</td><td>0</td></tr><tr><td>67</td><td>645</td><td>2016-05-14</td><td>2016-05-20</td><td>6</td><td>5</td></tr><tr><td>67</td><td>874</td><td>2016-05-30</td><td>2016-06-05</td><td>6</td><td>6</td></tr><tr><td>67</td><td>1382</td><td>2016-12-22</td><td>2016-12-23</td><td>1</td><td>6</td></tr><tr><td>67</td><td>1580</td><td>2017-03-01</td><td>2017-03-06</td><td>5</td><td>1</td></tr><tr><td>67</td><td>1584</td><td>2017-03-03</td><td>2017-03-04</td><td>1</td><td>5</td></tr><tr><td>68</td><td>563</td><td>2016-04-07</td><td>2016-04-12</td><td>5</td><td>0</td></tr><tr><td>68</td><td>1027</td><td>2016-07-12</td><td>2016-07-19</td><td>7</td><td>5</td></tr><tr><td>68</td><td>1324</td><td>2016-11-27</td><td>2016-12-01</td><td>4</td><td>7</td></tr><tr><td>69</td><td>885</td><td>2016-05-31</td><td>2016-06-01</td><td>1</td><td>0</td></tr><tr><td>69</td><td>1055</td><td>2016-09-15</td><td>2016-09-20</td><td>5</td><td>1</td></tr><tr><td>69</td><td>1225</td><td>2016-10-30</td><td>2016-11-04</td><td>5</td><td>5</td></tr><tr><td>69</td><td>1246</td><td>2016-11-05</td><td>2016-11-12</td><td>7</td><td>5</td></tr><tr><td>70</td><td>585</td><td>2016-04-17</td><td>2016-04-22</td><td>5</td><td>0</td></tr><tr><td>70</td><td>860</td><td>2016-05-27</td><td>2016-05-29</td><td>2</td><td>5</td></tr><tr><td>70</td><td>1006</td><td>2016-07-03</td><td>2016-07-06</td><td>3</td><td>2</td></tr><tr><td>70</td><td>704</td><td>2016-07-22</td><td>2016-07-25</td><td>3</td><td>3</td></tr><tr><td>70</td><td>814</td><td>2016-08-24</td><td>2016-08-27</td><td>3</td><td>3</td></tr><tr><td>70</td><td>1092</td><td>2016-09-30</td><td>2016-10-03</td><td>3</td><td>3</td></tr><tr><td>70</td><td>1126</td><td>2016-10-07</td><td>2016-10-10</td><td>3</td><td>3</td></tr><tr><td>70</td><td>1325</td><td>2016-11-27</td><td>2016-12-04</td><td>7</td><td>3</td></tr><tr><td>70</td><td>1333</td><td>2016-11-30</td><td>2016-12-06</td><td>6</td><td>7</td></tr><tr><td>70</td><td>1365</td><td>2016-12-15</td><td>2016-12-18</td><td>3</td><td>6</td></tr><tr><td>70</td><td>1457</td><td>2017-01-19</td><td>2017-01-26</td><td>7</td><td>3</td></tr><tr><td>71</td><td>1009</td><td>2016-07-04</td><td>2016-07-05</td><td>1</td><td>0</td></tr><tr><td>71</td><td>681</td><td>2016-07-18</td><td>2016-07-21</td><td>3</td><td>1</td></tr><tr><td>71</td><td>712</td><td>2016-07-24</td><td>2016-07-25</td><td>1</td><td>3</td></tr><tr><td>72</td><td>902</td><td>2016-06-04</td><td>2016-06-09</td><td>5</td><td>0</td></tr><tr><td>72</td><td>961</td><td>2016-06-16</td><td>2016-06-22</td><td>6</td><td>5</td></tr><tr><td>72</td><td>1318</td><td>2016-11-25</td><td>2016-11-27</td><td>2</td><td>6</td></tr><tr><td>72</td><td>1396</td><td>2016-12-25</td><td>2016-12-28</td><td>3</td><td>2</td></tr><tr><td>73</td><td>1000</td><td>2016-07-01</td><td>2016-07-05</td><td>4</td><td>0</td></tr><tr><td>73</td><td>714</td><td>2016-07-25</td><td>2016-08-01</td><td>7</td><td>4</td></tr><tr><td>73</td><td>1159</td><td>2016-10-16</td><td>2016-10-21</td><td>5</td><td>7</td></tr><tr><td>73</td><td>1331</td><td>2016-11-29</td><td>2016-12-03</td><td>4</td><td>5</td></tr><tr><td>74</td><td>595</td><td>2016-04-22</td><td>2016-04-29</td><td>7</td><td>0</td></tr><tr><td>74</td><td>877</td><td>2016-05-30</td><td>2016-06-03</td><td>4</td><td>7</td></tr><tr><td>74</td><td>940</td><td>2016-06-09</td><td>2016-06-14</td><td>5</td><td>4</td></tr><tr><td>74</td><td>963</td><td>2016-06-16</td><td>2016-06-17</td><td>1</td><td>5</td></tr><tr><td>74</td><td>797</td><td>2016-08-18</td><td>2016-08-23</td><td>5</td><td>1</td></tr><tr><td>74</td><td>830</td><td>2016-08-28</td><td>2016-08-29</td><td>1</td><td>5</td></tr><tr><td>74</td><td>847</td><td>2016-09-03</td><td>2016-09-06</td><td>3</td><td>1</td></tr><tr><td>74</td><td>1093</td><td>2016-09-30</td><td>2016-10-06</td><td>6</td><td>3</td></tr><tr><td>74</td><td>1179</td><td>2016-10-22</td><td>2016-10-29</td><td>7</td><td>6</td></tr><tr><td>75</td><td>1013</td><td>2016-07-06</td><td>2016-07-11</td><td>5</td><td>0</td></tr><tr><td>75</td><td>1412</td><td>2017-01-01</td><td>2017-01-03</td><td>2</td><td>5</td></tr><tr><td>75</td><td>1458</td><td>2017-01-19</td><td>2017-01-20</td><td>1</td><td>2</td></tr><tr><td>76</td><td>976</td><td>2016-06-22</td><td>2016-06-24</td><td>2</td><td>0</td></tr><tr><td>76</td><td>683</td><td>2016-07-18</td><td>2016-07-25</td><td>7</td><td>2</td></tr><tr><td>76</td><td>1557</td><td>2017-02-21</td><td>2017-02-24</td><td>3</td><td>7</td></tr><tr><td>77</td><td>593</td><td>2016-04-21</td><td>2016-04-24</td><td>3</td><td>0</td></tr><tr><td>77</td><td>982</td><td>2016-06-23</td><td>2016-06-26</td><td>3</td><td>3</td></tr><tr><td>77</td><td>698</td><td>2016-07-20</td><td>2016-07-24</td><td>4</td><td>3</td></tr><tr><td>77</td><td>1104</td><td>2016-10-01</td><td>2016-10-02</td><td>1</td><td>4</td></tr><tr><td>77</td><td>1439</td><td>2017-01-15</td><td>2017-01-21</td><td>6</td><td>1</td></tr><tr><td>77</td><td>1461</td><td>2017-01-22</td><td>2017-01-26</td><td>4</td><td>6</td></tr><tr><td>78</td><td>568</td><td>2016-04-10</td><td>2016-04-11</td><td>1</td><td>0</td></tr><tr><td>78</td><td>646</td><td>2016-05-14</td><td>2016-05-17</td><td>3</td><td>1</td></tr><tr><td>78</td><td>700</td><td>2016-07-20</td><td>2016-07-25</td><td>5</td><td>3</td></tr><tr><td>78</td><td>1268</td><td>2016-11-09</td><td>2016-11-11</td><td>2</td><td>5</td></tr><tr><td>78</td><td>1281</td><td>2016-11-15</td><td>2016-11-18</td><td>3</td><td>2</td></tr><tr><td>78</td><td>1577</td><td>2017-02-27</td><td>2017-03-06</td><td>7</td><td>3</td></tr><tr><td>79</td><td>583</td><td>2016-04-16</td><td>2016-04-22</td><td>6</td><td>0</td></tr><tr><td>79</td><td>1054</td><td>2016-09-15</td><td>2016-09-16</td><td>1</td><td>6</td></tr><tr><td>79</td><td>1229</td><td>2016-10-30</td><td>2016-11-06</td><td>7</td><td>1</td></tr><tr><td>79</td><td>1345</td><td>2016-12-05</td><td>2016-12-08</td><td>3</td><td>7</td></tr><tr><td>79</td><td>1447</td><td>2017-01-16</td><td>2017-01-20</td><td>4</td><td>3</td></tr><tr><td>80</td><td>887</td><td>2016-06-01</td><td>2016-06-07</td><td>6</td><td>0</td></tr><tr><td>80</td><td>929</td><td>2016-06-07</td><td>2016-06-09</td><td>2</td><td>6</td></tr><tr><td>80</td><td>983</td><td>2016-06-23</td><td>2016-06-29</td><td>6</td><td>2</td></tr><tr><td>80</td><td>667</td><td>2016-07-13</td><td>2016-07-19</td><td>6</td><td>6</td></tr><tr><td>80</td><td>1071</td><td>2016-09-20</td><td>2016-09-24</td><td>4</td><td>6</td></tr><tr><td>80</td><td>1279</td><td>2016-11-14</td><td>2016-11-19</td><td>5</td><td>4</td></tr><tr><td>80</td><td>1367</td><td>2016-12-17</td><td>2016-12-20</td><td>3</td><td>5</td></tr><tr><td>81</td><td>1366</td><td>2016-12-16</td><td>2016-12-21</td><td>5</td><td>0</td></tr><tr><td>81</td><td>1443</td><td>2017-01-16</td><td>2017-01-23</td><td>7</td><td>5</td></tr><tr><td>81</td><td>1464</td><td>2017-01-22</td><td>2017-01-29</td><td>7</td><td>7</td></tr><tr><td>81</td><td>1506</td><td>2017-02-06</td><td>2017-02-09</td><td>3</td><td>7</td></tr><tr><td>81</td><td>1562</td><td>2017-02-23</td><td>2017-02-26</td><td>3</td><td>3</td></tr><tr><td>82</td><td>862</td><td>2016-05-27</td><td>2016-05-31</td><td>4</td><td>0</td></tr><tr><td>82</td><td>871</td><td>2016-05-29</td><td>2016-06-03</td><td>5</td><td>4</td></tr><tr><td>82</td><td>997</td><td>2016-07-01</td><td>2016-07-07</td><td>6</td><td>5</td></tr><tr><td>82</td><td>1277</td><td>2016-11-12</td><td>2016-11-17</td><td>5</td><td>6</td></tr><tr><td>82</td><td>1341</td><td>2016-12-04</td><td>2016-12-06</td><td>2</td><td>5</td></tr><tr><td>82</td><td>1406</td><td>2016-12-29</td><td>2016-12-30</td><td>1</td><td>2</td></tr><tr><td>83</td><td>572</td><td>2016-04-10</td><td>2016-04-17</td><td>7</td><td>0</td></tr><tr><td>83</td><td>869</td><td>2016-05-28</td><td>2016-06-03</td><td>6</td><td>7</td></tr><tr><td>83</td><td>878</td><td>2016-05-30</td><td>2016-06-05</td><td>6</td><td>6</td></tr><tr><td>83</td><td>995</td><td>2016-06-30</td><td>2016-07-05</td><td>5</td><td>6</td></tr><tr><td>83</td><td>674</td><td>2016-07-15</td><td>2016-07-19</td><td>4</td><td>5</td></tr><tr><td>83</td><td>798</td><td>2016-08-18</td><td>2016-08-22</td><td>4</td><td>4</td></tr><tr><td>83</td><td>1119</td><td>2016-10-04</td><td>2016-10-10</td><td>6</td><td>4</td></tr><tr><td>83</td><td>1379</td><td>2016-12-19</td><td>2016-12-26</td><td>7</td><td>6</td></tr><tr><td>84</td><td>954</td><td>2016-06-13</td><td>2016-06-18</td><td>5</td><td>0</td></tr><tr><td>84</td><td>819</td><td>2016-08-24</td><td>2016-08-26</td><td>2</td><td>5</td></tr><tr><td>84</td><td>1376</td><td>2016-12-17</td><td>2016-12-22</td><td>5</td><td>2</td></tr><tr><td>84</td><td>1384</td><td>2016-12-22</td><td>2016-12-29</td><td>7</td><td>5</td></tr><tr><td>85</td><td>647</td><td>2016-05-15</td><td>2016-05-18</td><td>3</td><td>0</td></tr><tr><td>85</td><td>1059</td><td>2016-09-17</td><td>2016-09-20</td><td>3</td><td>3</td></tr><tr><td>85</td><td>1320</td><td>2016-11-25</td><td>2016-11-26</td><td>1</td><td>3</td></tr><tr><td>85</td><td>1513</td><td>2017-02-09</td><td>2017-02-16</td><td>7</td><td>1</td></tr><tr><td>86</td><td>859</td><td>2016-05-26</td><td>2016-05-27</td><td>1</td><td>0</td></tr><tr><td>86</td><td>1057</td><td>2016-09-16</td><td>2016-09-21</td><td>5</td><td>1</td></tr><tr><td>86</td><td>1079</td><td>2016-09-24</td><td>2016-09-28</td><td>4</td><td>5</td></tr><tr><td>86</td><td>1108</td><td>2016-10-01</td><td>2016-10-02</td><td>1</td><td>4</td></tr><tr><td>86</td><td>1453</td><td>2017-01-17</td><td>2017-01-18</td><td>1</td><td>1</td></tr><tr><td>87</td><td>558</td><td>2016-04-06</td><td>2016-04-10</td><td>4</td><td>0</td></tr><tr><td>87</td><td>844</td><td>2016-09-02</td><td>2016-09-03</td><td>1</td><td>4</td></tr><tr><td>87</td><td>1103</td><td>2016-10-01</td><td>2016-10-04</td><td>3</td><td>1</td></tr><tr><td>87</td><td>1349</td><td>2016-12-06</td><td>2016-12-11</td><td>5</td><td>3</td></tr><tr><td>87</td><td>1456</td><td>2017-01-19</td><td>2017-01-24</td><td>5</td><td>5</td></tr><tr><td>88</td><td>866</td><td>2016-05-28</td><td>2016-05-30</td><td>2</td><td>0</td></tr><tr><td>88</td><td>757</td><td>2016-08-05</td><td>2016-08-12</td><td>7</td><td>2</td></tr><tr><td>88</td><td>1196</td><td>2016-10-26</td><td>2016-10-29</td><td>3</td><td>7</td></tr><tr><td>88</td><td>1273</td><td>2016-11-10</td><td>2016-11-17</td><td>7</td><td>3</td></tr><tr><td>88</td><td>1300</td><td>2016-11-21</td><td>2016-11-24</td><td>3</td><td>7</td></tr><tr><td>88</td><td>1359</td><td>2016-12-12</td><td>2016-12-14</td><td>2</td><td>3</td></tr><tr><td>88</td><td>1548</td><td>2017-02-18</td><td>2017-02-25</td><td>7</td><td>2</td></tr><tr><td>88</td><td>1575</td><td>2017-02-26</td><td>2017-03-04</td><td>6</td><td>7</td></tr><tr><td>89</td><td>817</td><td>2016-08-24</td><td>2016-08-27</td><td>3</td><td>0</td></tr><tr><td>89</td><td>1037</td><td>2016-09-08</td><td>2016-09-15</td><td>7</td><td>3</td></tr><tr><td>89</td><td>1101</td><td>2016-10-01</td><td>2016-10-06</td><td>5</td><td>7</td></tr><tr><td>89</td><td>1189</td><td>2016-10-24</td><td>2016-10-30</td><td>6</td><td>5</td></tr><tr><td>89</td><td>1253</td><td>2016-11-05</td><td>2016-11-07</td><td>2</td><td>6</td></tr><tr><td>89</td><td>1269</td><td>2016-11-09</td><td>2016-11-11</td><td>2</td><td>2</td></tr><tr><td>89</td><td>1399</td><td>2016-12-26</td><td>2016-12-28</td><td>2</td><td>2</td></tr><tr><td>89</td><td>1521</td><td>2017-02-12</td><td>2017-02-19</td><td>7</td><td>2</td></tr><tr><td>90</td><td>729</td><td>2016-07-28</td><td>2016-07-30</td><td>2</td><td>0</td></tr><tr><td>90</td><td>1174</td><td>2016-10-21</td><td>2016-10-28</td><td>7</td><td>2</td></tr><tr><td>90</td><td>1299</td><td>2016-11-21</td><td>2016-11-27</td><td>6</td><td>7</td></tr><tr><td>90</td><td>1405</td><td>2016-12-29</td><td>2017-01-03</td><td>5</td><td>6</td></tr><tr><td>91</td><td>636</td><td>2016-05-10</td><td>2016-05-16</td><td>6</td><td>0</td></tr><tr><td>91</td><td>732</td><td>2016-07-28</td><td>2016-08-01</td><td>4</td><td>6</td></tr><tr><td>91</td><td>1213</td><td>2016-10-28</td><td>2016-10-31</td><td>3</td><td>4</td></tr><tr><td>91</td><td>1397</td><td>2016-12-25</td><td>2016-12-29</td><td>4</td><td>3</td></tr><tr><td>92</td><td>942</td><td>2016-06-10</td><td>2016-06-16</td><td>6</td><td>0</td></tr><tr><td>92</td><td>1016</td><td>2016-07-07</td><td>2016-07-09</td><td>2</td><td>6</td></tr><tr><td>92</td><td>809</td><td>2016-08-23</td><td>2016-08-26</td><td>3</td><td>2</td></tr><tr><td>92</td><td>841</td><td>2016-08-31</td><td>2016-09-06</td><td>6</td><td>3</td></tr><tr><td>92</td><td>1527</td><td>2017-02-13</td><td>2017-02-15</td><td>2</td><td>6</td></tr><tr><td>92</td><td>1555</td><td>2017-02-20</td><td>2017-02-24</td><td>4</td><td>2</td></tr><tr><td>93</td><td>741</td><td>2016-07-30</td><td>2016-08-06</td><td>7</td><td>0</td></tr><tr><td>93</td><td>1169</td><td>2016-10-20</td><td>2016-10-24</td><td>4</td><td>7</td></tr><tr><td>93</td><td>1217</td><td>2016-10-29</td><td>2016-10-30</td><td>1</td><td>4</td></tr><tr><td>93</td><td>1355</td><td>2016-12-08</td><td>2016-12-10</td><td>2</td><td>1</td></tr><tr><td>93</td><td>1391</td><td>2016-12-25</td><td>2016-12-29</td><td>4</td><td>2</td></tr><tr><td>94</td><td>616</td><td>2016-05-02</td><td>2016-05-06</td><td>4</td><td>0</td></tr><tr><td>94</td><td>975</td><td>2016-06-21</td><td>2016-06-26</td><td>5</td><td>4</td></tr><tr><td>94</td><td>665</td><td>2016-07-13</td><td>2016-07-20</td><td>7</td><td>5</td></tr><tr><td>94</td><td>727</td><td>2016-07-27</td><td>2016-07-30</td><td>3</td><td>7</td></tr><tr><td>94</td><td>1241</td><td>2016-11-03</td><td>2016-11-10</td><td>7</td><td>3</td></tr><tr><td>94</td><td>1305</td><td>2016-11-22</td><td>2016-11-24</td><td>2</td><td>7</td></tr><tr><td>94</td><td>1312</td><td>2016-11-23</td><td>2016-11-26</td><td>3</td><td>2</td></tr><tr><td>94</td><td>1368</td><td>2016-12-17</td><td>2016-12-18</td><td>1</td><td>3</td></tr><tr><td>94</td><td>1518</td><td>2017-02-12</td><td>2017-02-14</td><td>2</td><td>1</td></tr><tr><td>94</td><td>1564</td><td>2017-02-23</td><td>2017-03-02</td><td>7</td><td>2</td></tr><tr><td>95</td><td>656</td><td>2016-05-19</td><td>2016-05-26</td><td>7</td><td>0</td></tr><tr><td>95</td><td>1048</td><td>2016-09-13</td><td>2016-09-16</td><td>3</td><td>7</td></tr><tr><td>95</td><td>1097</td><td>2016-10-01</td><td>2016-10-05</td><td>4</td><td>3</td></tr><tr><td>95</td><td>1543</td><td>2017-02-16</td><td>2017-02-23</td><td>7</td><td>4</td></tr><tr><td>96</td><td>607</td><td>2016-04-28</td><td>2016-05-02</td><td>4</td><td>0</td></tr><tr><td>96</td><td>623</td><td>2016-05-08</td><td>2016-05-15</td><td>7</td><td>4</td></tr><tr><td>96</td><td>671</td><td>2016-07-14</td><td>2016-07-18</td><td>4</td><td>7</td></tr><tr><td>96</td><td>780</td><td>2016-08-15</td><td>2016-08-16</td><td>1</td><td>4</td></tr><tr><td>96</td><td>1378</td><td>2016-12-18</td><td>2016-12-21</td><td>3</td><td>1</td></tr><tr><td>96</td><td>1438</td><td>2017-01-14</td><td>2017-01-16</td><td>2</td><td>3</td></tr><tr><td>96</td><td>1569</td><td>2017-02-24</td><td>2017-03-03</td><td>7</td><td>2</td></tr><tr><td>97</td><td>635</td><td>2016-05-10</td><td>2016-05-13</td><td>3</td><td>0</td></tr><tr><td>97</td><td>726</td><td>2016-07-27</td><td>2016-07-31</td><td>4</td><td>3</td></tr><tr><td>97</td><td>718</td><td>2016-07-27</td><td>2016-08-03</td><td>7</td><td>4</td></tr><tr><td>97</td><td>836</td><td>2016-08-29</td><td>2016-08-31</td><td>2</td><td>7</td></tr><tr><td>97</td><td>1395</td><td>2016-12-25</td><td>2016-12-26</td><td>1</td><td>2</td></tr><tr><td>97</td><td>1417</td><td>2017-01-03</td><td>2017-01-10</td><td>7</td><td>1</td></tr><tr><td>97</td><td>1528</td><td>2017-02-13</td><td>2017-02-15</td><td>2</td><td>7</td></tr><tr><td>98</td><td>631</td><td>2016-05-09</td><td>2016-05-15</td><td>6</td><td>0</td></tr><tr><td>98</td><td>884</td><td>2016-05-30</td><td>2016-06-04</td><td>5</td><td>6</td></tr><tr><td>98</td><td>1050</td><td>2016-09-13</td><td>2016-09-19</td><td>6</td><td>5</td></tr><tr><td>98</td><td>1402</td><td>2016-12-28</td><td>2016-12-30</td><td>2</td><td>6</td></tr><tr><td>99</td><td>632</td><td>2016-05-09</td><td>2016-05-10</td><td>1</td><td>0</td></tr><tr><td>99</td><td>691</td><td>2016-07-20</td><td>2016-07-25</td><td>5</td><td>1</td></tr><tr><td>99</td><td>1072</td><td>2016-09-20</td><td>2016-09-21</td><td>1</td><td>5</td></tr><tr><td>99</td><td>1408</td><td>2016-12-31</td><td>2017-01-01</td><td>1</td><td>1</td></tr><tr><td>99</td><td>1486</td><td>2017-01-31</td><td>2017-02-05</td><td>5</td><td>1</td></tr><tr><td>100</td><td>597</td><td>2016-04-23</td><td>2016-04-24</td><td>1</td><td>0</td></tr><tr><td>100</td><td>637</td><td>2016-05-11</td><td>2016-05-16</td><td>5</td><td>1</td></tr><tr><td>100</td><td>1315</td><td>2016-11-24</td><td>2016-11-29</td><td>5</td><td>5</td></tr><tr><td>100</td><td>1482</td><td>2017-01-29</td><td>2017-02-05</td><td>7</td><td>5</td></tr><tr><td>101</td><td>715</td><td>2016-07-25</td><td>2016-07-28</td><td>3</td><td>0</td></tr><tr><td>101</td><td>1332</td><td>2016-11-29</td><td>2016-12-05</td><td>6</td><td>3</td></tr><tr><td>101</td><td>1516</td><td>2017-02-10</td><td>2017-02-14</td><td>4</td><td>6</td></tr><tr><td>102</td><td>689</td><td>2016-07-19</td><td>2016-07-24</td><td>5</td><td>0</td></tr><tr><td>102</td><td>1343</td><td>2016-12-05</td><td>2016-12-07</td><td>2</td><td>5</td></tr><tr><td>103</td><td>972</td><td>2016-06-19</td><td>2016-06-21</td><td>2</td><td>0</td></tr><tr><td>103</td><td>992</td><td>2016-06-29</td><td>2016-07-06</td><td>7</td><td>2</td></tr><tr><td>103</td><td>1398</td><td>2016-12-26</td><td>2016-12-27</td><td>1</td><td>7</td></tr><tr><td>103</td><td>1485</td><td>2017-01-30</td><td>2017-02-03</td><td>4</td><td>1</td></tr><tr><td>104</td><td>837</td><td>2016-08-29</td><td>2016-09-02</td><td>4</td><td>0</td></tr><tr><td>104</td><td>1180</td><td>2016-10-22</td><td>2016-10-23</td><td>1</td><td>4</td></tr><tr><td>104</td><td>1522</td><td>2017-02-12</td><td>2017-02-14</td><td>2</td><td>1</td></tr><tr><td>104</td><td>1532</td><td>2017-02-14</td><td>2017-02-17</td><td>3</td><td>2</td></tr><tr><td>105</td><td>618</td><td>2016-05-03</td><td>2016-05-04</td><td>1</td><td>0</td></tr><tr><td>105</td><td>1525</td><td>2017-02-12</td><td>2017-02-17</td><td>5</td><td>1</td></tr><tr><td>106</td><td>610</td><td>2016-04-30</td><td>2016-05-03</td><td>3</td><td>0</td></tr><tr><td>106</td><td>708</td><td>2016-07-23</td><td>2016-07-30</td><td>7</td><td>3</td></tr><tr><td>106</td><td>1228</td><td>2016-10-30</td><td>2016-11-06</td><td>7</td><td>7</td></tr><tr><td>106</td><td>1271</td><td>2016-11-10</td><td>2016-11-15</td><td>5</td><td>7</td></tr><tr><td>106</td><td>1372</td><td>2016-12-17</td><td>2016-12-24</td><td>7</td><td>5</td></tr><tr><td>106</td><td>1510</td><td>2017-02-08</td><td>2017-02-14</td><td>6</td><td>7</td></tr><tr><td>107</td><td>586</td><td>2016-04-18</td><td>2016-04-24</td><td>6</td><td>0</td></tr><tr><td>107</td><td>1250</td><td>2016-11-05</td><td>2016-11-09</td><td>4</td><td>6</td></tr><tr><td>107</td><td>1354</td><td>2016-12-07</td><td>2016-12-08</td><td>1</td><td>4</td></tr><tr><td>107</td><td>1452</td><td>2017-01-17</td><td>2017-01-23</td><td>6</td><td>1</td></tr><tr><td>107</td><td>1494</td><td>2017-02-04</td><td>2017-02-06</td><td>2</td><td>6</td></tr><tr><td>108</td><td>1102</td><td>2016-10-01</td><td>2016-10-02</td><td>1</td><td>0</td></tr><tr><td>108</td><td>1392</td><td>2016-12-25</td><td>2016-12-31</td><td>6</td><td>1</td></tr><tr><td>109</td><td>614</td><td>2016-05-01</td><td>2016-05-05</td><td>4</td><td>0</td></tr><tr><td>109</td><td>621</td><td>2016-05-06</td><td>2016-05-13</td><td>7</td><td>4</td></tr><tr><td>109</td><td>654</td><td>2016-05-18</td><td>2016-05-23</td><td>5</td><td>7</td></tr><tr><td>109</td><td>810</td><td>2016-08-23</td><td>2016-08-25</td><td>2</td><td>5</td></tr><tr><td>109</td><td>1083</td><td>2016-09-27</td><td>2016-09-28</td><td>1</td><td>2</td></tr><tr><td>109</td><td>1298</td><td>2016-11-20</td><td>2016-11-24</td><td>4</td><td>1</td></tr><tr><td>109</td><td>1560</td><td>2017-02-23</td><td>2017-02-24</td><td>1</td><td>4</td></tr><tr><td>110</td><td>931</td><td>2016-06-07</td><td>2016-06-12</td><td>5</td><td>0</td></tr><tr><td>110</td><td>964</td><td>2016-06-16</td><td>2016-06-22</td><td>6</td><td>5</td></tr><tr><td>110</td><td>685</td><td>2016-07-18</td><td>2016-07-19</td><td>1</td><td>6</td></tr><tr><td>110</td><td>1041</td><td>2016-09-10</td><td>2016-09-13</td><td>3</td><td>1</td></tr><tr><td>110</td><td>1109</td><td>2016-10-01</td><td>2016-10-06</td><td>5</td><td>3</td></tr><tr><td>110</td><td>1162</td><td>2016-10-17</td><td>2016-10-19</td><td>2</td><td>5</td></tr><tr><td>110</td><td>1424</td><td>2017-01-07</td><td>2017-01-08</td><td>1</td><td>2</td></tr><tr><td>110</td><td>1489</td><td>2017-02-02</td><td>2017-02-08</td><td>6</td><td>1</td></tr><tr><td>111</td><td>605</td><td>2016-04-27</td><td>2016-05-04</td><td>7</td><td>0</td></tr><tr><td>111</td><td>959</td><td>2016-06-14</td><td>2016-06-21</td><td>7</td><td>7</td></tr><tr><td>111</td><td>786</td><td>2016-08-16</td><td>2016-08-20</td><td>4</td><td>7</td></tr><tr><td>111</td><td>1296</td><td>2016-11-19</td><td>2016-11-22</td><td>3</td><td>4</td></tr><tr><td>111</td><td>1353</td><td>2016-12-07</td><td>2016-12-12</td><td>5</td><td>3</td></tr><tr><td>112</td><td>921</td><td>2016-06-06</td><td>2016-06-07</td><td>1</td><td>0</td></tr><tr><td>112</td><td>776</td><td>2016-08-14</td><td>2016-08-18</td><td>4</td><td>1</td></tr><tr><td>112</td><td>801</td><td>2016-08-20</td><td>2016-08-25</td><td>5</td><td>4</td></tr><tr><td>112</td><td>1124</td><td>2016-10-06</td><td>2016-10-12</td><td>6</td><td>5</td></tr><tr><td>112</td><td>1530</td><td>2017-02-13</td><td>2017-02-19</td><td>6</td><td>6</td></tr><tr><td>113</td><td>1029</td><td>2016-09-05</td><td>2016-09-10</td><td>5</td><td>0</td></tr><tr><td>113</td><td>1085</td><td>2016-09-28</td><td>2016-10-02</td><td>4</td><td>5</td></tr><tr><td>113</td><td>1263</td><td>2016-11-08</td><td>2016-11-09</td><td>1</td><td>4</td></tr><tr><td>113</td><td>1495</td><td>2017-02-04</td><td>2017-02-11</td><td>7</td><td>1</td></tr><tr><td>113</td><td>1499</td><td>2017-02-05</td><td>2017-02-07</td><td>2</td><td>7</td></tr><tr><td>114</td><td>966</td><td>2016-06-16</td><td>2016-06-22</td><td>6</td><td>0</td></tr><tr><td>114</td><td>737</td><td>2016-07-29</td><td>2016-07-31</td><td>2</td><td>6</td></tr><tr><td>114</td><td>827</td><td>2016-08-26</td><td>2016-09-02</td><td>7</td><td>2</td></tr><tr><td>114</td><td>1540</td><td>2017-02-16</td><td>2017-02-19</td><td>3</td><td>7</td></tr><tr><td>115</td><td>596</td><td>2016-04-23</td><td>2016-04-30</td><td>7</td><td>0</td></tr><tr><td>115</td><td>943</td><td>2016-06-10</td><td>2016-06-17</td><td>7</td><td>7</td></tr><tr><td>115</td><td>1121</td><td>2016-10-04</td><td>2016-10-11</td><td>7</td><td>7</td></tr><tr><td>115</td><td>1154</td><td>2016-10-15</td><td>2016-10-19</td><td>4</td><td>7</td></tr><tr><td>115</td><td>1352</td><td>2016-12-07</td><td>2016-12-10</td><td>3</td><td>4</td></tr><tr><td>115</td><td>1554</td><td>2017-02-20</td><td>2017-02-23</td><td>3</td><td>3</td></tr><tr><td>115</td><td>1566</td><td>2017-02-24</td><td>2017-02-25</td><td>1</td><td>3</td></tr><tr><td>116</td><td>1455</td><td>2017-01-18</td><td>2017-01-20</td><td>2</td><td>0</td></tr><tr><td>116</td><td>1501</td><td>2017-02-05</td><td>2017-02-09</td><td>4</td><td>2</td></tr><tr><td>117</td><td>612</td><td>2016-05-01</td><td>2016-05-03</td><td>2</td><td>0</td></tr><tr><td>117</td><td>617</td><td>2016-05-02</td><td>2016-05-05</td><td>3</td><td>2</td></tr><tr><td>117</td><td>953</td><td>2016-06-12</td><td>2016-06-17</td><td>5</td><td>3</td></tr><tr><td>117</td><td>962</td><td>2016-06-16</td><td>2016-06-20</td><td>4</td><td>5</td></tr><tr><td>117</td><td>1002</td><td>2016-07-03</td><td>2016-07-04</td><td>1</td><td>4</td></tr><tr><td>117</td><td>1192</td><td>2016-10-26</td><td>2016-10-28</td><td>2</td><td>1</td></tr><tr><td>117</td><td>1247</td><td>2016-11-05</td><td>2016-11-08</td><td>3</td><td>2</td></tr><tr><td>117</td><td>1468</td><td>2017-01-23</td><td>2017-01-30</td><td>7</td><td>3</td></tr><tr><td>118</td><td>864</td><td>2016-05-28</td><td>2016-06-03</td><td>6</td><td>0</td></tr><tr><td>118</td><td>994</td><td>2016-06-30</td><td>2016-07-07</td><td>7</td><td>6</td></tr><tr><td>118</td><td>996</td><td>2016-07-01</td><td>2016-07-04</td><td>3</td><td>7</td></tr><tr><td>118</td><td>716</td><td>2016-07-26</td><td>2016-07-27</td><td>1</td><td>3</td></tr><tr><td>118</td><td>1374</td><td>2016-12-17</td><td>2016-12-22</td><td>5</td><td>1</td></tr><tr><td>118</td><td>1472</td><td>2017-01-24</td><td>2017-01-30</td><td>6</td><td>5</td></tr><tr><td>118</td><td>1481</td><td>2017-01-29</td><td>2017-02-01</td><td>3</td><td>6</td></tr><tr><td>119</td><td>1026</td><td>2016-07-12</td><td>2016-07-15</td><td>3</td><td>0</td></tr><tr><td>119</td><td>706</td><td>2016-07-22</td><td>2016-07-24</td><td>2</td><td>3</td></tr><tr><td>119</td><td>722</td><td>2016-07-27</td><td>2016-07-28</td><td>1</td><td>2</td></tr><tr><td>119</td><td>1413</td><td>2017-01-02</td><td>2017-01-05</td><td>3</td><td>1</td></tr><tr><td>119</td><td>1488</td><td>2017-02-01</td><td>2017-02-04</td><td>3</td><td>3</td></tr><tr><td>120</td><td>998</td><td>2016-07-01</td><td>2016-07-04</td><td>3</td><td>0</td></tr><tr><td>120</td><td>762</td><td>2016-08-07</td><td>2016-08-10</td><td>3</td><td>3</td></tr><tr><td>120</td><td>1089</td><td>2016-09-30</td><td>2016-10-06</td><td>6</td><td>3</td></tr><tr><td>120</td><td>1339</td><td>2016-12-03</td><td>2016-12-09</td><td>6</td><td>6</td></tr><tr><td>120</td><td>1483</td><td>2017-01-30</td><td>2017-01-31</td><td>1</td><td>6</td></tr><tr><td>120</td><td>1493</td><td>2017-02-04</td><td>2017-02-11</td><td>7</td><td>1</td></tr><tr><td>121</td><td>858</td><td>2016-05-25</td><td>2016-05-30</td><td>5</td><td>0</td></tr><tr><td>121</td><td>735</td><td>2016-07-28</td><td>2016-08-03</td><td>6</td><td>5</td></tr><tr><td>121</td><td>739</td><td>2016-07-30</td><td>2016-08-05</td><td>6</td><td>6</td></tr><tr><td>121</td><td>1049</td><td>2016-09-13</td><td>2016-09-16</td><td>3</td><td>6</td></tr><tr><td>121</td><td>1128</td><td>2016-10-08</td><td>2016-10-12</td><td>4</td><td>3</td></tr><tr><td>121</td><td>1215</td><td>2016-10-29</td><td>2016-11-02</td><td>4</td><td>4</td></tr><tr><td>121</td><td>1373</td><td>2016-12-17</td><td>2016-12-22</td><td>5</td><td>4</td></tr><tr><td>121</td><td>1393</td><td>2016-12-25</td><td>2016-12-31</td><td>6</td><td>5</td></tr><tr><td>122</td><td>1007</td><td>2016-07-04</td><td>2016-07-06</td><td>2</td><td>0</td></tr><tr><td>122</td><td>1036</td><td>2016-09-08</td><td>2016-09-10</td><td>2</td><td>2</td></tr><tr><td>122</td><td>1062</td><td>2016-09-17</td><td>2016-09-20</td><td>3</td><td>2</td></tr><tr><td>122</td><td>1166</td><td>2016-10-19</td><td>2016-10-23</td><td>4</td><td>3</td></tr><tr><td>122</td><td>1209</td><td>2016-10-28</td><td>2016-10-29</td><td>1</td><td>4</td></tr><tr><td>122</td><td>1245</td><td>2016-11-04</td><td>2016-11-06</td><td>2</td><td>1</td></tr><tr><td>122</td><td>1337</td><td>2016-12-02</td><td>2016-12-04</td><td>2</td><td>2</td></tr><tr><td>122</td><td>1385</td><td>2016-12-23</td><td>2016-12-28</td><td>5</td><td>2</td></tr><tr><td>122</td><td>1440</td><td>2017-01-15</td><td>2017-01-18</td><td>3</td><td>5</td></tr><tr><td>123</td><td>587</td><td>2016-04-19</td><td>2016-04-26</td><td>7</td><td>0</td></tr><tr><td>123</td><td>923</td><td>2016-06-07</td><td>2016-06-11</td><td>4</td><td>7</td></tr><tr><td>123</td><td>967</td><td>2016-06-16</td><td>2016-06-21</td><td>5</td><td>4</td></tr><tr><td>123</td><td>1223</td><td>2016-10-30</td><td>2016-10-31</td><td>1</td><td>5</td></tr><tr><td>123</td><td>1282</td><td>2016-11-15</td><td>2016-11-21</td><td>6</td><td>1</td></tr><tr><td>124</td><td>861</td><td>2016-05-27</td><td>2016-05-28</td><td>1</td><td>0</td></tr><tr><td>124</td><td>1210</td><td>2016-10-28</td><td>2016-11-01</td><td>4</td><td>1</td></tr><tr><td>124</td><td>1330</td><td>2016-11-29</td><td>2016-12-06</td><td>7</td><td>4</td></tr><tr><td>124</td><td>1403</td><td>2016-12-29</td><td>2017-01-04</td><td>6</td><td>7</td></tr><tr><td>124</td><td>1419</td><td>2017-01-05</td><td>2017-01-08</td><td>3</td><td>6</td></tr><tr><td>124</td><td>1531</td><td>2017-02-13</td><td>2017-02-19</td><td>6</td><td>3</td></tr><tr><td>125</td><td>576</td><td>2016-04-11</td><td>2016-04-12</td><td>1</td><td>0</td></tr><tr><td>126</td><td>754</td><td>2016-08-04</td><td>2016-08-08</td><td>4</td><td>0</td></tr><tr><td>126</td><td>806</td><td>2016-08-21</td><td>2016-08-27</td><td>6</td><td>4</td></tr><tr><td>126</td><td>1134</td><td>2016-10-08</td><td>2016-10-09</td><td>1</td><td>6</td></tr><tr><td>126</td><td>1364</td><td>2016-12-15</td><td>2016-12-21</td><td>6</td><td>1</td></tr><tr><td>126</td><td>1428</td><td>2017-01-09</td><td>2017-01-16</td><td>7</td><td>6</td></tr><tr><td>126</td><td>1500</td><td>2017-02-05</td><td>2017-02-09</td><td>4</td><td>7</td></tr><tr><td>127</td><td>643</td><td>2016-05-14</td><td>2016-05-16</td><td>2</td><td>0</td></tr><tr><td>127</td><td>853</td><td>2016-05-24</td><td>2016-05-29</td><td>5</td><td>2</td></tr><tr><td>127</td><td>879</td><td>2016-05-30</td><td>2016-06-01</td><td>2</td><td>5</td></tr><tr><td>127</td><td>1034</td><td>2016-09-06</td><td>2016-09-12</td><td>6</td><td>2</td></tr><tr><td>127</td><td>1226</td><td>2016-10-30</td><td>2016-11-04</td><td>5</td><td>6</td></tr><tr><td>127</td><td>1286</td><td>2016-11-16</td><td>2016-11-17</td><td>1</td><td>5</td></tr><tr><td>127</td><td>1579</td><td>2017-02-28</td><td>2017-03-05</td><td>5</td><td>1</td></tr><tr><td>128</td><td>717</td><td>2016-07-26</td><td>2016-07-28</td><td>2</td><td>0</td></tr><tr><td>128</td><td>815</td><td>2016-08-24</td><td>2016-08-25</td><td>1</td><td>2</td></tr><tr><td>128</td><td>1290</td><td>2016-11-19</td><td>2016-11-20</td><td>1</td><td>1</td></tr><tr><td>128</td><td>1574</td><td>2017-02-26</td><td>2017-02-27</td><td>1</td><td>1</td></tr><tr><td>128</td><td>1583</td><td>2017-03-03</td><td>2017-03-07</td><td>4</td><td>1</td></tr><tr><td>129</td><td>723</td><td>2016-07-27</td><td>2016-08-03</td><td>7</td><td>0</td></tr><tr><td>129</td><td>1360</td><td>2016-12-13</td><td>2016-12-19</td><td>6</td><td>7</td></tr><tr><td>129</td><td>1445</td><td>2017-01-16</td><td>2017-01-23</td><td>7</td><td>6</td></tr><tr><td>129</td><td>1509</td><td>2017-02-08</td><td>2017-02-14</td><td>6</td><td>7</td></tr><tr><td>130</td><td>580</td><td>2016-04-14</td><td>2016-04-17</td><td>3</td><td>0</td></tr><tr><td>130</td><td>613</td><td>2016-05-01</td><td>2016-05-04</td><td>3</td><td>3</td></tr><tr><td>130</td><td>910</td><td>2016-06-06</td><td>2016-06-08</td><td>2</td><td>3</td></tr><tr><td>130</td><td>779</td><td>2016-08-15</td><td>2016-08-21</td><td>6</td><td>2</td></tr><tr><td>130</td><td>1040</td><td>2016-09-09</td><td>2016-09-10</td><td>1</td><td>6</td></tr><tr><td>130</td><td>1475</td><td>2017-01-26</td><td>2017-02-02</td><td>7</td><td>1</td></tr><tr><td>131</td><td>559</td><td>2016-04-06</td><td>2016-04-08</td><td>2</td><td>0</td></tr><tr><td>131</td><td>655</td><td>2016-05-18</td><td>2016-05-19</td><td>1</td><td>2</td></tr><tr><td>131</td><td>881</td><td>2016-05-30</td><td>2016-06-05</td><td>6</td><td>1</td></tr><tr><td>131</td><td>760</td><td>2016-08-06</td><td>2016-08-10</td><td>4</td><td>6</td></tr><tr><td>131</td><td>1474</td><td>2017-01-25</td><td>2017-01-30</td><td>5</td><td>4</td></tr><tr><td>132</td><td>619</td><td>2016-05-04</td><td>2016-05-11</td><td>7</td><td>0</td></tr><tr><td>132</td><td>999</td><td>2016-07-01</td><td>2016-07-07</td><td>6</td><td>7</td></tr><tr><td>132</td><td>1090</td><td>2016-09-30</td><td>2016-10-07</td><td>7</td><td>6</td></tr><tr><td>132</td><td>1111</td><td>2016-10-01</td><td>2016-10-04</td><td>3</td><td>7</td></tr><tr><td>132</td><td>1301</td><td>2016-11-22</td><td>2016-11-24</td><td>2</td><td>3</td></tr><tr><td>132</td><td>1519</td><td>2017-02-12</td><td>2017-02-14</td><td>2</td><td>2</td></tr><tr><td>133</td><td>909</td><td>2016-06-06</td><td>2016-06-10</td><td>4</td><td>0</td></tr><tr><td>133</td><td>988</td><td>2016-06-27</td><td>2016-06-30</td><td>3</td><td>4</td></tr><tr><td>133</td><td>1149</td><td>2016-10-12</td><td>2016-10-19</td><td>7</td><td>3</td></tr><tr><td>133</td><td>1306</td><td>2016-11-22</td><td>2016-11-25</td><td>3</td><td>7</td></tr><tr><td>133</td><td>1363</td><td>2016-12-15</td><td>2016-12-20</td><td>5</td><td>3</td></tr><tr><td>133</td><td>1409</td><td>2017-01-01</td><td>2017-01-02</td><td>1</td><td>5</td></tr><tr><td>134</td><td>1004</td><td>2016-07-03</td><td>2016-07-08</td><td>5</td><td>0</td></tr><tr><td>134</td><td>1024</td><td>2016-07-11</td><td>2016-07-12</td><td>1</td><td>5</td></tr><tr><td>134</td><td>1045</td><td>2016-09-12</td><td>2016-09-14</td><td>2</td><td>1</td></tr><tr><td>134</td><td>1178</td><td>2016-10-22</td><td>2016-10-29</td><td>7</td><td>2</td></tr><tr><td>134</td><td>1219</td><td>2016-10-30</td><td>2016-11-05</td><td>6</td><td>7</td></tr><tr><td>134</td><td>1535</td><td>2017-02-15</td><td>2017-02-22</td><td>7</td><td>6</td></tr><tr><td>135</td><td>724</td><td>2016-07-27</td><td>2016-08-02</td><td>6</td><td>0</td></tr><tr><td>135</td><td>849</td><td>2016-09-05</td><td>2016-09-12</td><td>7</td><td>6</td></tr><tr><td>135</td><td>1289</td><td>2016-11-18</td><td>2016-11-21</td><td>3</td><td>7</td></tr><tr><td>136</td><td>584</td><td>2016-04-17</td><td>2016-04-19</td><td>2</td><td>0</td></tr><tr><td>136</td><td>661</td><td>2016-05-21</td><td>2016-05-26</td><td>5</td><td>2</td></tr><tr><td>136</td><td>1046</td><td>2016-09-12</td><td>2016-09-16</td><td>4</td><td>5</td></tr><tr><td>137</td><td>582</td><td>2016-04-16</td><td>2016-04-19</td><td>3</td><td>0</td></tr><tr><td>137</td><td>649</td><td>2016-05-17</td><td>2016-05-22</td><td>5</td><td>3</td></tr><tr><td>137</td><td>657</td><td>2016-05-20</td><td>2016-05-26</td><td>6</td><td>5</td></tr><tr><td>137</td><td>1014</td><td>2016-07-06</td><td>2016-07-07</td><td>1</td><td>6</td></tr><tr><td>137</td><td>1201</td><td>2016-10-26</td><td>2016-11-01</td><td>6</td><td>1</td></tr><tr><td>137</td><td>1280</td><td>2016-11-15</td><td>2016-11-18</td><td>3</td><td>6</td></tr><tr><td>138</td><td>768</td><td>2016-08-12</td><td>2016-08-18</td><td>6</td><td>0</td></tr><tr><td>138</td><td>796</td><td>2016-08-17</td><td>2016-08-21</td><td>4</td><td>6</td></tr><tr><td>138</td><td>1256</td><td>2016-11-06</td><td>2016-11-10</td><td>4</td><td>4</td></tr><tr><td>138</td><td>1283</td><td>2016-11-16</td><td>2016-11-18</td><td>2</td><td>4</td></tr><tr><td>138</td><td>1294</td><td>2016-11-19</td><td>2016-11-24</td><td>5</td><td>2</td></tr><tr><td>138</td><td>1358</td><td>2016-12-11</td><td>2016-12-18</td><td>7</td><td>5</td></tr><tr><td>138</td><td>1370</td><td>2016-12-17</td><td>2016-12-22</td><td>5</td><td>7</td></tr><tr><td>139</td><td>579</td><td>2016-04-14</td><td>2016-04-16</td><td>2</td><td>0</td></tr><tr><td>139</td><td>745</td><td>2016-08-01</td><td>2016-08-02</td><td>1</td><td>2</td></tr><tr><td>139</td><td>751</td><td>2016-08-03</td><td>2016-08-07</td><td>4</td><td>1</td></tr><tr><td>139</td><td>1042</td><td>2016-09-10</td><td>2016-09-12</td><td>2</td><td>4</td></tr><tr><td>139</td><td>1064</td><td>2016-09-18</td><td>2016-09-24</td><td>6</td><td>2</td></tr><tr><td>139</td><td>1433</td><td>2017-01-11</td><td>2017-01-17</td><td>6</td><td>6</td></tr><tr><td>139</td><td>1450</td><td>2017-01-17</td><td>2017-01-24</td><td>7</td><td>6</td></tr><tr><td>140</td><td>915</td><td>2016-06-06</td><td>2016-06-08</td><td>2</td><td>0</td></tr><tr><td>140</td><td>733</td><td>2016-07-28</td><td>2016-07-29</td><td>1</td><td>2</td></tr><tr><td>140</td><td>1098</td><td>2016-10-01</td><td>2016-10-03</td><td>2</td><td>1</td></tr><tr><td>140</td><td>1156</td><td>2016-10-15</td><td>2016-10-18</td><td>3</td><td>2</td></tr><tr><td>140</td><td>1259</td><td>2016-11-07</td><td>2016-11-14</td><td>7</td><td>3</td></tr><tr><td>140</td><td>1357</td><td>2016-12-10</td><td>2016-12-14</td><td>4</td><td>7</td></tr><tr><td>140</td><td>1361</td><td>2016-12-14</td><td>2016-12-17</td><td>3</td><td>4</td></tr><tr><td>140</td><td>1371</td><td>2016-12-17</td><td>2016-12-18</td><td>1</td><td>3</td></tr><tr><td>141</td><td>565</td><td>2016-04-08</td><td>2016-04-14</td><td>6</td><td>0</td></tr><tr><td>141</td><td>908</td><td>2016-06-05</td><td>2016-06-07</td><td>2</td><td>6</td></tr><tr><td>141</td><td>761</td><td>2016-08-06</td><td>2016-08-09</td><td>3</td><td>2</td></tr><tr><td>141</td><td>784</td><td>2016-08-16</td><td>2016-08-23</td><td>7</td><td>3</td></tr><tr><td>141</td><td>1254</td><td>2016-11-06</td><td>2016-11-10</td><td>4</td><td>7</td></tr><tr><td>141</td><td>1401</td><td>2016-12-27</td><td>2017-01-02</td><td>6</td><td>4</td></tr><tr><td>142</td><td>1369</td><td>2016-12-17</td><td>2016-12-23</td><td>6</td><td>0</td></tr><tr><td>142</td><td>1545</td><td>2017-02-17</td><td>2017-02-20</td><td>3</td><td>6</td></tr><tr><td>143</td><td>980</td><td>2016-06-23</td><td>2016-06-26</td><td>3</td><td>0</td></tr><tr><td>143</td><td>1155</td><td>2016-10-15</td><td>2016-10-22</td><td>7</td><td>3</td></tr><tr><td>143</td><td>1193</td><td>2016-10-26</td><td>2016-11-01</td><td>6</td><td>7</td></tr><tr><td>143</td><td>1222</td><td>2016-10-30</td><td>2016-11-01</td><td>2</td><td>6</td></tr><tr><td>143</td><td>1313</td><td>2016-11-23</td><td>2016-11-27</td><td>4</td><td>2</td></tr><tr><td>143</td><td>1394</td><td>2016-12-25</td><td>2016-12-28</td><td>3</td><td>4</td></tr><tr><td>143</td><td>1448</td><td>2017-01-16</td><td>2017-01-22</td><td>6</td><td>3</td></tr><tr><td>144</td><td>581</td><td>2016-04-15</td><td>2016-04-19</td><td>4</td><td>0</td></tr><tr><td>144</td><td>1087</td><td>2016-09-29</td><td>2016-10-01</td><td>2</td><td>4</td></tr><tr><td>144</td><td>1199</td><td>2016-10-26</td><td>2016-11-02</td><td>7</td><td>2</td></tr><tr><td>144</td><td>1297</td><td>2016-11-19</td><td>2016-11-20</td><td>1</td><td>7</td></tr><tr><td>144</td><td>1572</td><td>2017-02-25</td><td>2017-02-27</td><td>2</td><td>1</td></tr><tr><td>145</td><td>703</td><td>2016-07-22</td><td>2016-07-26</td><td>4</td><td>0</td></tr><tr><td>145</td><td>1077</td><td>2016-09-23</td><td>2016-09-24</td><td>1</td><td>4</td></tr><tr><td>145</td><td>1120</td><td>2016-10-04</td><td>2016-10-05</td><td>1</td><td>1</td></tr><tr><td>145</td><td>1145</td><td>2016-10-09</td><td>2016-10-13</td><td>4</td><td>1</td></tr><tr><td>145</td><td>1338</td><td>2016-12-02</td><td>2016-12-04</td><td>2</td><td>4</td></tr><tr><td>145</td><td>1471</td><td>2017-01-23</td><td>2017-01-24</td><td>1</td><td>2</td></tr><tr><td>146</td><td>890</td><td>2016-06-02</td><td>2016-06-05</td><td>3</td><td>0</td></tr><tr><td>146</td><td>664</td><td>2016-07-13</td><td>2016-07-16</td><td>3</td><td>3</td></tr><tr><td>146</td><td>789</td><td>2016-08-16</td><td>2016-08-23</td><td>7</td><td>3</td></tr><tr><td>146</td><td>804</td><td>2016-08-20</td><td>2016-08-27</td><td>7</td><td>7</td></tr><tr><td>146</td><td>1032</td><td>2016-09-05</td><td>2016-09-10</td><td>5</td><td>7</td></tr><tr><td>146</td><td>1479</td><td>2017-01-28</td><td>2017-02-03</td><td>6</td><td>5</td></tr><tr><td>147</td><td>771</td><td>2016-08-12</td><td>2016-08-16</td><td>4</td><td>0</td></tr><tr><td>148</td><td>678</td><td>2016-07-17</td><td>2016-07-21</td><td>4</td><td>0</td></tr><tr><td>148</td><td>765</td><td>2016-08-09</td><td>2016-08-12</td><td>3</td><td>4</td></tr><tr><td>148</td><td>783</td><td>2016-08-16</td><td>2016-08-23</td><td>7</td><td>3</td></tr><tr><td>148</td><td>808</td><td>2016-08-23</td><td>2016-08-25</td><td>2</td><td>7</td></tr><tr><td>148</td><td>812</td><td>2016-08-23</td><td>2016-08-29</td><td>6</td><td>2</td></tr><tr><td>148</td><td>1578</td><td>2017-02-27</td><td>2017-03-06</td><td>7</td><td>6</td></tr><tr><td>149</td><td>591</td><td>2016-04-20</td><td>2016-04-21</td><td>1</td><td>0</td></tr><tr><td>149</td><td>652</td><td>2016-05-18</td><td>2016-05-19</td><td>1</td><td>1</td></tr><tr><td>149</td><td>833</td><td>2016-08-28</td><td>2016-08-30</td><td>2</td><td>1</td></tr><tr><td>149</td><td>834</td><td>2016-08-29</td><td>2016-09-03</td><td>5</td><td>2</td></tr><tr><td>149</td><td>843</td><td>2016-09-01</td><td>2016-09-05</td><td>4</td><td>5</td></tr><tr><td>149</td><td>1146</td><td>2016-10-10</td><td>2016-10-16</td><td>6</td><td>4</td></tr><tr><td>149</td><td>1514</td><td>2017-02-09</td><td>2017-02-14</td><td>5</td><td>6</td></tr><tr><td>150</td><td>641</td><td>2016-05-13</td><td>2016-05-16</td><td>3</td><td>0</td></tr><tr><td>150</td><td>1100</td><td>2016-10-01</td><td>2016-10-06</td><td>5</td><td>3</td></tr><tr><td>150</td><td>1105</td><td>2016-10-01</td><td>2016-10-02</td><td>1</td><td>5</td></tr><tr><td>150</td><td>1177</td><td>2016-10-22</td><td>2016-10-23</td><td>1</td><td>1</td></tr><tr><td>150</td><td>1203</td><td>2016-10-26</td><td>2016-10-30</td><td>4</td><td>1</td></tr><tr><td>150</td><td>1432</td><td>2017-01-10</td><td>2017-01-13</td><td>3</td><td>4</td></tr><tr><td>151</td><td>893</td><td>2016-06-03</td><td>2016-06-06</td><td>3</td><td>0</td></tr><tr><td>151</td><td>1058</td><td>2016-09-16</td><td>2016-09-19</td><td>3</td><td>3</td></tr><tr><td>151</td><td>1115</td><td>2016-10-02</td><td>2016-10-05</td><td>3</td><td>3</td></tr><tr><td>152</td><td>730</td><td>2016-07-28</td><td>2016-07-30</td><td>2</td><td>0</td></tr><tr><td>152</td><td>1160</td><td>2016-10-16</td><td>2016-10-23</td><td>7</td><td>2</td></tr><tr><td>152</td><td>1197</td><td>2016-10-26</td><td>2016-11-01</td><td>6</td><td>7</td></tr><tr><td>152</td><td>1558</td><td>2017-02-21</td><td>2017-02-23</td><td>2</td><td>6</td></tr><tr><td>153</td><td>594</td><td>2016-04-22</td><td>2016-04-25</td><td>3</td><td>0</td></tr><tr><td>153</td><td>969</td><td>2016-06-17</td><td>2016-06-23</td><td>6</td><td>3</td></tr><tr><td>153</td><td>1460</td><td>2017-01-21</td><td>2017-01-24</td><td>3</td><td>6</td></tr><tr><td>153</td><td>1470</td><td>2017-01-23</td><td>2017-01-28</td><td>5</td><td>3</td></tr><tr><td>153</td><td>1507</td><td>2017-02-07</td><td>2017-02-10</td><td>3</td><td>5</td></tr><tr><td>154</td><td>968</td><td>2016-06-16</td><td>2016-06-17</td><td>1</td><td>0</td></tr><tr><td>154</td><td>1061</td><td>2016-09-17</td><td>2016-09-24</td><td>7</td><td>1</td></tr><tr><td>154</td><td>1168</td><td>2016-10-19</td><td>2016-10-25</td><td>6</td><td>7</td></tr><tr><td>154</td><td>1262</td><td>2016-11-07</td><td>2016-11-08</td><td>1</td><td>6</td></tr><tr><td>154</td><td>1539</td><td>2017-02-16</td><td>2017-02-18</td><td>2</td><td>1</td></tr><tr><td>155</td><td>575</td><td>2016-04-10</td><td>2016-04-11</td><td>1</td><td>0</td></tr><tr><td>155</td><td>577</td><td>2016-04-12</td><td>2016-04-15</td><td>3</td><td>1</td></tr><tr><td>155</td><td>1112</td><td>2016-10-01</td><td>2016-10-05</td><td>4</td><td>3</td></tr><tr><td>155</td><td>1310</td><td>2016-11-23</td><td>2016-11-24</td><td>1</td><td>4</td></tr><tr><td>155</td><td>1541</td><td>2017-02-16</td><td>2017-02-17</td><td>1</td><td>1</td></tr><tr><td>156</td><td>588</td><td>2016-04-19</td><td>2016-04-26</td><td>7</td><td>0</td></tr><tr><td>156</td><td>907</td><td>2016-06-05</td><td>2016-06-08</td><td>3</td><td>7</td></tr><tr><td>156</td><td>956</td><td>2016-06-13</td><td>2016-06-19</td><td>6</td><td>3</td></tr><tr><td>156</td><td>692</td><td>2016-07-20</td><td>2016-07-26</td><td>6</td><td>6</td></tr><tr><td>156</td><td>1462</td><td>2017-01-22</td><td>2017-01-29</td><td>7</td><td>6</td></tr><tr><td>156</td><td>1490</td><td>2017-02-03</td><td>2017-02-04</td><td>1</td><td>7</td></tr><tr><td>156</td><td>1561</td><td>2017-02-23</td><td>2017-02-27</td><td>4</td><td>1</td></tr><tr><td>157</td><td>648</td><td>2016-05-16</td><td>2016-05-20</td><td>4</td><td>0</td></tr><tr><td>157</td><td>1025</td><td>2016-07-12</td><td>2016-07-15</td><td>3</td><td>4</td></tr><tr><td>157</td><td>1047</td><td>2016-09-13</td><td>2016-09-17</td><td>4</td><td>3</td></tr><tr><td>157</td><td>1240</td><td>2016-11-03</td><td>2016-11-10</td><td>7</td><td>4</td></tr><tr><td>157</td><td>1551</td><td>2017-02-19</td><td>2017-02-22</td><td>3</td><td>7</td></tr><tr><td>158</td><td>825</td><td>2016-08-25</td><td>2016-08-29</td><td>4</td><td>0</td></tr><tr><td>158</td><td>840</td><td>2016-08-30</td><td>2016-09-03</td><td>4</td><td>4</td></tr><tr><td>158</td><td>1117</td><td>2016-10-03</td><td>2016-10-06</td><td>3</td><td>4</td></tr><tr><td>160</td><td>922</td><td>2016-06-06</td><td>2016-06-08</td><td>2</td><td>0</td></tr><tr><td>160</td><td>927</td><td>2016-06-07</td><td>2016-06-11</td><td>4</td><td>2</td></tr><tr><td>160</td><td>933</td><td>2016-06-07</td><td>2016-06-11</td><td>4</td><td>4</td></tr><tr><td>160</td><td>720</td><td>2016-07-27</td><td>2016-07-29</td><td>2</td><td>4</td></tr><tr><td>160</td><td>1565</td><td>2017-02-23</td><td>2017-02-26</td><td>3</td><td>2</td></tr><tr><td>161</td><td>639</td><td>2016-05-12</td><td>2016-05-16</td><td>4</td><td>0</td></tr><tr><td>161</td><td>653</td><td>2016-05-18</td><td>2016-05-25</td><td>7</td><td>4</td></tr><tr><td>161</td><td>911</td><td>2016-06-06</td><td>2016-06-10</td><td>4</td><td>7</td></tr><tr><td>161</td><td>1068</td><td>2016-09-19</td><td>2016-09-25</td><td>6</td><td>4</td></tr><tr><td>161</td><td>1190</td><td>2016-10-24</td><td>2016-10-31</td><td>7</td><td>6</td></tr><tr><td>161</td><td>1571</td><td>2017-02-25</td><td>2017-03-01</td><td>4</td><td>7</td></tr><tr><td>162</td><td>599</td><td>2016-04-24</td><td>2016-04-28</td><td>4</td><td>0</td></tr><tr><td>162</td><td>1205</td><td>2016-10-27</td><td>2016-11-02</td><td>6</td><td>4</td></tr><tr><td>162</td><td>1400</td><td>2016-12-26</td><td>2016-12-27</td><td>1</td><td>6</td></tr><tr><td>163</td><td>630</td><td>2016-05-09</td><td>2016-05-11</td><td>2</td><td>0</td></tr><tr><td>163</td><td>941</td><td>2016-06-10</td><td>2016-06-11</td><td>1</td><td>2</td></tr><tr><td>163</td><td>782</td><td>2016-08-16</td><td>2016-08-19</td><td>3</td><td>1</td></tr><tr><td>163</td><td>1075</td><td>2016-09-23</td><td>2016-09-27</td><td>4</td><td>3</td></tr><tr><td>163</td><td>1107</td><td>2016-10-01</td><td>2016-10-04</td><td>3</td><td>4</td></tr><tr><td>163</td><td>1265</td><td>2016-11-08</td><td>2016-11-13</td><td>5</td><td>3</td></tr><tr><td>163</td><td>1487</td><td>2017-02-01</td><td>2017-02-04</td><td>3</td><td>5</td></tr><tr><td>164</td><td>570</td><td>2016-04-10</td><td>2016-04-17</td><td>7</td><td>0</td></tr><tr><td>164</td><td>1010</td><td>2016-07-04</td><td>2016-07-06</td><td>2</td><td>7</td></tr><tr><td>164</td><td>742</td><td>2016-07-31</td><td>2016-08-06</td><td>6</td><td>2</td></tr><tr><td>164</td><td>1284</td><td>2016-11-16</td><td>2016-11-20</td><td>4</td><td>6</td></tr><tr><td>164</td><td>1292</td><td>2016-11-19</td><td>2016-11-21</td><td>2</td><td>4</td></tr><tr><td>165</td><td>640</td><td>2016-05-12</td><td>2016-05-15</td><td>3</td><td>0</td></tr><tr><td>165</td><td>857</td><td>2016-05-25</td><td>2016-05-30</td><td>5</td><td>3</td></tr><tr><td>165</td><td>900</td><td>2016-06-03</td><td>2016-06-09</td><td>6</td><td>5</td></tr><tr><td>165</td><td>897</td><td>2016-06-03</td><td>2016-06-09</td><td>6</td><td>6</td></tr><tr><td>165</td><td>892</td><td>2016-06-03</td><td>2016-06-06</td><td>3</td><td>6</td></tr><tr><td>165</td><td>1141</td><td>2016-10-09</td><td>2016-10-10</td><td>1</td><td>3</td></tr><tr><td>165</td><td>1375</td><td>2016-12-17</td><td>2016-12-21</td><td>4</td><td>1</td></tr><tr><td>166</td><td>644</td><td>2016-05-14</td><td>2016-05-21</td><td>7</td><td>0</td></tr><tr><td>166</td><td>781</td><td>2016-08-16</td><td>2016-08-23</td><td>7</td><td>7</td></tr><tr><td>166</td><td>1526</td><td>2017-02-12</td><td>2017-02-14</td><td>2</td><td>7</td></tr><tr><td>167</td><td>854</td><td>2016-05-24</td><td>2016-05-31</td><td>7</td><td>0</td></tr><tr><td>167</td><td>1414</td><td>2017-01-02</td><td>2017-01-05</td><td>3</td><td>7</td></tr><tr><td>168</td><td>930</td><td>2016-06-07</td><td>2016-06-10</td><td>3</td><td>0</td></tr><tr><td>168</td><td>792</td><td>2016-08-16</td><td>2016-08-19</td><td>3</td><td>3</td></tr><tr><td>168</td><td>794</td><td>2016-08-17</td><td>2016-08-21</td><td>4</td><td>3</td></tr><tr><td>168</td><td>1249</td><td>2016-11-05</td><td>2016-11-09</td><td>4</td><td>4</td></tr><tr><td>168</td><td>1266</td><td>2016-11-08</td><td>2016-11-12</td><td>4</td><td>4</td></tr><tr><td>169</td><td>573</td><td>2016-04-10</td><td>2016-04-15</td><td>5</td><td>0</td></tr><tr><td>169</td><td>659</td><td>2016-05-21</td><td>2016-05-27</td><td>6</td><td>5</td></tr><tr><td>169</td><td>974</td><td>2016-06-20</td><td>2016-06-21</td><td>1</td><td>6</td></tr><tr><td>169</td><td>746</td><td>2016-08-01</td><td>2016-08-08</td><td>7</td><td>1</td></tr><tr><td>169</td><td>1356</td><td>2016-12-09</td><td>2016-12-13</td><td>4</td><td>7</td></tr><tr><td>169</td><td>1427</td><td>2017-01-09</td><td>2017-01-10</td><td>1</td><td>4</td></tr><tr><td>170</td><td>567</td><td>2016-04-10</td><td>2016-04-17</td><td>7</td><td>0</td></tr><tr><td>170</td><td>944</td><td>2016-06-10</td><td>2016-06-14</td><td>4</td><td>7</td></tr><tr><td>170</td><td>1194</td><td>2016-10-26</td><td>2016-10-30</td><td>4</td><td>4</td></tr><tr><td>170</td><td>1267</td><td>2016-11-09</td><td>2016-11-16</td><td>7</td><td>4</td></tr><tr><td>170</td><td>1342</td><td>2016-12-04</td><td>2016-12-10</td><td>6</td><td>7</td></tr><tr><td>171</td><td>574</td><td>2016-04-10</td><td>2016-04-12</td><td>2</td><td>0</td></tr><tr><td>171</td><td>981</td><td>2016-06-23</td><td>2016-06-27</td><td>4</td><td>2</td></tr><tr><td>171</td><td>1181</td><td>2016-10-23</td><td>2016-10-29</td><td>6</td><td>4</td></tr><tr><td>171</td><td>1329</td><td>2016-11-29</td><td>2016-12-04</td><td>5</td><td>6</td></tr><tr><td>171</td><td>1567</td><td>2017-02-24</td><td>2017-03-02</td><td>6</td><td>5</td></tr><tr><td>172</td><td>984</td><td>2016-06-24</td><td>2016-06-28</td><td>4</td><td>0</td></tr><tr><td>172</td><td>709</td><td>2016-07-24</td><td>2016-07-29</td><td>5</td><td>4</td></tr><tr><td>172</td><td>749</td><td>2016-08-02</td><td>2016-08-08</td><td>6</td><td>5</td></tr><tr><td>172</td><td>839</td><td>2016-08-29</td><td>2016-09-03</td><td>5</td><td>6</td></tr><tr><td>172</td><td>1142</td><td>2016-10-09</td><td>2016-10-13</td><td>4</td><td>5</td></tr><tr><td>172</td><td>1171</td><td>2016-10-20</td><td>2016-10-25</td><td>5</td><td>4</td></tr><tr><td>172</td><td>1336</td><td>2016-12-02</td><td>2016-12-07</td><td>5</td><td>5</td></tr><tr><td>172</td><td>1421</td><td>2017-01-05</td><td>2017-01-10</td><td>5</td><td>5</td></tr><tr><td>172</td><td>1491</td><td>2017-02-03</td><td>2017-02-05</td><td>2</td><td>5</td></tr><tr><td>173</td><td>913</td><td>2016-06-06</td><td>2016-06-07</td><td>1</td><td>0</td></tr><tr><td>173</td><td>669</td><td>2016-07-14</td><td>2016-07-21</td><td>7</td><td>1</td></tr><tr><td>173</td><td>1350</td><td>2016-12-06</td><td>2016-12-09</td><td>3</td><td>7</td></tr><tr><td>173</td><td>1429</td><td>2017-01-09</td><td>2017-01-13</td><td>4</td><td>3</td></tr><tr><td>174</td><td>917</td><td>2016-06-06</td><td>2016-06-08</td><td>2</td><td>0</td></tr><tr><td>174</td><td>1015</td><td>2016-07-06</td><td>2016-07-11</td><td>5</td><td>2</td></tr><tr><td>174</td><td>682</td><td>2016-07-18</td><td>2016-07-21</td><td>3</td><td>5</td></tr><tr><td>174</td><td>1276</td><td>2016-11-12</td><td>2016-11-13</td><td>1</td><td>3</td></tr><tr><td>175</td><td>867</td><td>2016-05-28</td><td>2016-06-03</td><td>6</td><td>0</td></tr><tr><td>175</td><td>799</td><td>2016-08-19</td><td>2016-08-23</td><td>4</td><td>6</td></tr><tr><td>175</td><td>1094</td><td>2016-09-30</td><td>2016-10-05</td><td>5</td><td>4</td></tr><tr><td>175</td><td>1133</td><td>2016-10-08</td><td>2016-10-10</td><td>2</td><td>5</td></tr><tr><td>175</td><td>1407</td><td>2016-12-30</td><td>2017-01-06</td><td>7</td><td>2</td></tr><tr><td>176</td><td>592</td><td>2016-04-21</td><td>2016-04-26</td><td>5</td><td>0</td></tr><tr><td>176</td><td>1143</td><td>2016-10-09</td><td>2016-10-15</td><td>6</td><td>5</td></tr><tr><td>176</td><td>1278</td><td>2016-11-13</td><td>2016-11-19</td><td>6</td><td>6</td></tr><tr><td>176</td><td>1383</td><td>2016-12-22</td><td>2016-12-26</td><td>4</td><td>6</td></tr><tr><td>176</td><td>1511</td><td>2017-02-08</td><td>2017-02-10</td><td>2</td><td>4</td></tr><tr><td>176</td><td>1570</td><td>2017-02-24</td><td>2017-02-27</td><td>3</td><td>2</td></tr><tr><td>177</td><td>785</td><td>2016-08-16</td><td>2016-08-19</td><td>3</td><td>0</td></tr><tr><td>177</td><td>831</td><td>2016-08-28</td><td>2016-09-04</td><td>7</td><td>3</td></tr><tr><td>177</td><td>1176</td><td>2016-10-21</td><td>2016-10-24</td><td>3</td><td>7</td></tr><tr><td>177</td><td>1503</td><td>2017-02-05</td><td>2017-02-08</td><td>3</td><td>3</td></tr><tr><td>178</td><td>991</td><td>2016-06-28</td><td>2016-07-05</td><td>7</td><td>0</td></tr><tr><td>178</td><td>816</td><td>2016-08-24</td><td>2016-08-28</td><td>4</td><td>7</td></tr><tr><td>178</td><td>1211</td><td>2016-10-28</td><td>2016-10-31</td><td>3</td><td>4</td></tr><tr><td>178</td><td>1242</td><td>2016-11-03</td><td>2016-11-04</td><td>1</td><td>3</td></tr><tr><td>179</td><td>662</td><td>2016-05-21</td><td>2016-05-23</td><td>2</td><td>0</td></tr><tr><td>179</td><td>1021</td><td>2016-07-09</td><td>2016-07-10</td><td>1</td><td>2</td></tr><tr><td>179</td><td>1497</td><td>2017-02-04</td><td>2017-02-05</td><td>1</td><td>1</td></tr><tr><td>180</td><td>905</td><td>2016-06-04</td><td>2016-06-09</td><td>5</td><td>0</td></tr><tr><td>180</td><td>1559</td><td>2017-02-22</td><td>2017-02-25</td><td>3</td><td>5</td></tr><tr><td>180</td><td>1563</td><td>2017-02-23</td><td>2017-03-01</td><td>6</td><td>3</td></tr><tr><td>181</td><td>937</td><td>2016-06-08</td><td>2016-06-11</td><td>3</td><td>0</td></tr><tr><td>181</td><td>958</td><td>2016-06-13</td><td>2016-06-18</td><td>5</td><td>3</td></tr><tr><td>181</td><td>1022</td><td>2016-07-10</td><td>2016-07-11</td><td>1</td><td>5</td></tr><tr><td>181</td><td>677</td><td>2016-07-16</td><td>2016-07-20</td><td>4</td><td>1</td></tr><tr><td>181</td><td>731</td><td>2016-07-28</td><td>2016-08-03</td><td>6</td><td>4</td></tr><tr><td>181</td><td>1346</td><td>2016-12-05</td><td>2016-12-11</td><td>6</td><td>6</td></tr><tr><td>182</td><td>571</td><td>2016-04-10</td><td>2016-04-12</td><td>2</td><td>0</td></tr><tr><td>182</td><td>928</td><td>2016-06-07</td><td>2016-06-09</td><td>2</td><td>2</td></tr><tr><td>182</td><td>1008</td><td>2016-07-04</td><td>2016-07-10</td><td>6</td><td>2</td></tr><tr><td>182</td><td>740</td><td>2016-07-30</td><td>2016-08-02</td><td>3</td><td>6</td></tr><tr><td>182</td><td>1188</td><td>2016-10-24</td><td>2016-10-25</td><td>1</td><td>3</td></tr><tr><td>182</td><td>1230</td><td>2016-10-30</td><td>2016-11-06</td><td>7</td><td>1</td></tr><tr><td>182</td><td>1231</td><td>2016-10-30</td><td>2016-11-03</td><td>4</td><td>7</td></tr><tr><td>182</td><td>1308</td><td>2016-11-23</td><td>2016-11-24</td><td>1</td><td>4</td></tr><tr><td>182</td><td>1317</td><td>2016-11-25</td><td>2016-11-28</td><td>3</td><td>1</td></tr><tr><td>182</td><td>1326</td><td>2016-11-28</td><td>2016-12-02</td><td>4</td><td>3</td></tr><tr><td>182</td><td>1410</td><td>2017-01-01</td><td>2017-01-05</td><td>4</td><td>4</td></tr><tr><td>182</td><td>1422</td><td>2017-01-06</td><td>2017-01-09</td><td>3</td><td>4</td></tr><tr><td>183</td><td>939</td><td>2016-06-09</td><td>2016-06-13</td><td>4</td><td>0</td></tr><tr><td>183</td><td>1067</td><td>2016-09-19</td><td>2016-09-26</td><td>7</td><td>4</td></tr><tr><td>183</td><td>1147</td><td>2016-10-10</td><td>2016-10-14</td><td>4</td><td>7</td></tr><tr><td>183</td><td>1437</td><td>2017-01-13</td><td>2017-01-17</td><td>4</td><td>4</td></tr><tr><td>184</td><td>608</td><td>2016-04-28</td><td>2016-04-30</td><td>2</td><td>0</td></tr><tr><td>184</td><td>880</td><td>2016-05-30</td><td>2016-06-03</td><td>4</td><td>2</td></tr><tr><td>184</td><td>684</td><td>2016-07-18</td><td>2016-07-21</td><td>3</td><td>4</td></tr><tr><td>184</td><td>1251</td><td>2016-11-05</td><td>2016-11-09</td><td>4</td><td>3</td></tr><tr><td>185</td><td>578</td><td>2016-04-13</td><td>2016-04-19</td><td>6</td><td>0</td></tr><tr><td>185</td><td>863</td><td>2016-05-28</td><td>2016-06-01</td><td>4</td><td>6</td></tr><tr><td>185</td><td>898</td><td>2016-06-03</td><td>2016-06-07</td><td>4</td><td>4</td></tr><tr><td>185</td><td>925</td><td>2016-06-07</td><td>2016-06-13</td><td>6</td><td>4</td></tr><tr><td>185</td><td>672</td><td>2016-07-14</td><td>2016-07-17</td><td>3</td><td>6</td></tr><tr><td>185</td><td>679</td><td>2016-07-17</td><td>2016-07-22</td><td>5</td><td>3</td></tr><tr><td>185</td><td>693</td><td>2016-07-20</td><td>2016-07-22</td><td>2</td><td>5</td></tr><tr><td>185</td><td>711</td><td>2016-07-24</td><td>2016-07-27</td><td>3</td><td>2</td></tr><tr><td>185</td><td>1125</td><td>2016-10-06</td><td>2016-10-09</td><td>3</td><td>3</td></tr><tr><td>185</td><td>1183</td><td>2016-10-23</td><td>2016-10-28</td><td>5</td><td>3</td></tr><tr><td>185</td><td>1441</td><td>2017-01-16</td><td>2017-01-23</td><td>7</td><td>5</td></tr><tr><td>185</td><td>1463</td><td>2017-01-22</td><td>2017-01-29</td><td>7</td><td>7</td></tr><tr><td>186</td><td>615</td><td>2016-05-01</td><td>2016-05-04</td><td>3</td><td>0</td></tr><tr><td>186</td><td>1153</td><td>2016-10-15</td><td>2016-10-18</td><td>3</td><td>3</td></tr><tr><td>186</td><td>1248</td><td>2016-11-05</td><td>2016-11-07</td><td>2</td><td>3</td></tr><tr><td>186</td><td>1467</td><td>2017-01-22</td><td>2017-01-25</td><td>3</td><td>2</td></tr><tr><td>187</td><td>633</td><td>2016-05-09</td><td>2016-05-15</td><td>6</td><td>0</td></tr><tr><td>187</td><td>868</td><td>2016-05-28</td><td>2016-06-01</td><td>4</td><td>6</td></tr><tr><td>187</td><td>957</td><td>2016-06-13</td><td>2016-06-17</td><td>4</td><td>4</td></tr><tr><td>187</td><td>695</td><td>2016-07-20</td><td>2016-07-26</td><td>6</td><td>4</td></tr><tr><td>187</td><td>743</td><td>2016-07-31</td><td>2016-08-02</td><td>2</td><td>6</td></tr><tr><td>187</td><td>766</td><td>2016-08-10</td><td>2016-08-11</td><td>1</td><td>2</td></tr><tr><td>187</td><td>1404</td><td>2016-12-29</td><td>2016-12-31</td><td>2</td><td>1</td></tr><tr><td>188</td><td>912</td><td>2016-06-06</td><td>2016-06-07</td><td>1</td><td>0</td></tr><tr><td>188</td><td>690</td><td>2016-07-19</td><td>2016-07-23</td><td>4</td><td>1</td></tr><tr><td>188</td><td>710</td><td>2016-07-24</td><td>2016-07-31</td><td>7</td><td>4</td></tr><tr><td>188</td><td>747</td><td>2016-08-01</td><td>2016-08-04</td><td>3</td><td>7</td></tr><tr><td>188</td><td>1030</td><td>2016-09-05</td><td>2016-09-09</td><td>4</td><td>3</td></tr><tr><td>188</td><td>1390</td><td>2016-12-25</td><td>2016-12-30</td><td>5</td><td>4</td></tr><tr><td>189</td><td>699</td><td>2016-07-20</td><td>2016-07-22</td><td>2</td><td>0</td></tr><tr><td>189</td><td>753</td><td>2016-08-03</td><td>2016-08-04</td><td>1</td><td>2</td></tr><tr><td>189</td><td>1204</td><td>2016-10-27</td><td>2016-10-29</td><td>2</td><td>1</td></tr><tr><td>189</td><td>1449</td><td>2017-01-17</td><td>2017-01-19</td><td>2</td><td>2</td></tr><tr><td>189</td><td>1576</td><td>2017-02-26</td><td>2017-03-01</td><td>3</td><td>2</td></tr><tr><td>190</td><td>600</td><td>2016-04-24</td><td>2016-05-01</td><td>7</td><td>0</td></tr><tr><td>190</td><td>989</td><td>2016-06-27</td><td>2016-06-28</td><td>1</td><td>7</td></tr><tr><td>190</td><td>1017</td><td>2016-07-08</td><td>2016-07-09</td><td>1</td><td>1</td></tr><tr><td>190</td><td>774</td><td>2016-08-13</td><td>2016-08-18</td><td>5</td><td>1</td></tr><tr><td>190</td><td>1517</td><td>2017-02-11</td><td>2017-02-16</td><td>5</td><td>5</td></tr><tr><td>191</td><td>1039</td><td>2016-09-09</td><td>2016-09-15</td><td>6</td><td>0</td></tr><tr><td>191</td><td>1302</td><td>2016-11-22</td><td>2016-11-23</td><td>1</td><td>6</td></tr><tr><td>191</td><td>1323</td><td>2016-11-27</td><td>2016-12-04</td><td>7</td><td>1</td></tr><tr><td>191</td><td>1502</td><td>2017-02-05</td><td>2017-02-07</td><td>2</td><td>7</td></tr><tr><td>191</td><td>1508</td><td>2017-02-08</td><td>2017-02-15</td><td>7</td><td>2</td></tr><tr><td>192</td><td>903</td><td>2016-06-04</td><td>2016-06-11</td><td>7</td><td>0</td></tr><tr><td>192</td><td>680</td><td>2016-07-17</td><td>2016-07-21</td><td>4</td><td>7</td></tr><tr><td>193</td><td>634</td><td>2016-05-09</td><td>2016-05-15</td><td>6</td><td>0</td></tr><tr><td>193</td><td>926</td><td>2016-06-07</td><td>2016-06-08</td><td>1</td><td>6</td></tr><tr><td>193</td><td>977</td><td>2016-06-22</td><td>2016-06-24</td><td>2</td><td>1</td></tr><tr><td>193</td><td>675</td><td>2016-07-15</td><td>2016-07-17</td><td>2</td><td>2</td></tr><tr><td>193</td><td>835</td><td>2016-08-29</td><td>2016-08-31</td><td>2</td><td>2</td></tr><tr><td>193</td><td>1043</td><td>2016-09-11</td><td>2016-09-17</td><td>6</td><td>2</td></tr><tr><td>193</td><td>1238</td><td>2016-11-03</td><td>2016-11-09</td><td>6</td><td>6</td></tr><tr><td>194</td><td>1095</td><td>2016-09-30</td><td>2016-10-05</td><td>5</td><td>0</td></tr><tr><td>195</td><td>721</td><td>2016-07-27</td><td>2016-07-31</td><td>4</td><td>0</td></tr><tr><td>195</td><td>842</td><td>2016-08-31</td><td>2016-09-04</td><td>4</td><td>4</td></tr><tr><td>195</td><td>1074</td><td>2016-09-22</td><td>2016-09-29</td><td>7</td><td>4</td></tr><tr><td>195</td><td>1184</td><td>2016-10-23</td><td>2016-10-28</td><td>5</td><td>7</td></tr><tr><td>195</td><td>1473</td><td>2017-01-24</td><td>2017-01-31</td><td>7</td><td>5</td></tr><tr><td>195</td><td>1484</td><td>2017-01-30</td><td>2017-01-31</td><td>1</td><td>7</td></tr><tr><td>196</td><td>952</td><td>2016-06-11</td><td>2016-06-14</td><td>3</td><td>0</td></tr><tr><td>196</td><td>673</td><td>2016-07-14</td><td>2016-07-19</td><td>5</td><td>3</td></tr><tr><td>196</td><td>1314</td><td>2016-11-23</td><td>2016-11-28</td><td>5</td><td>5</td></tr><tr><td>196</td><td>1340</td><td>2016-12-04</td><td>2016-12-09</td><td>5</td><td>5</td></tr><tr><td>197</td><td>993</td><td>2016-06-30</td><td>2016-07-07</td><td>7</td><td>0</td></tr><tr><td>197</td><td>764</td><td>2016-08-09</td><td>2016-08-16</td><td>7</td><td>7</td></tr><tr><td>197</td><td>1091</td><td>2016-09-30</td><td>2016-10-07</td><td>7</td><td>7</td></tr><tr><td>197</td><td>1172</td><td>2016-10-20</td><td>2016-10-27</td><td>7</td><td>7</td></tr><tr><td>197</td><td>1304</td><td>2016-11-22</td><td>2016-11-29</td><td>7</td><td>7</td></tr><tr><td>197</td><td>1387</td><td>2016-12-24</td><td>2016-12-27</td><td>3</td><td>7</td></tr><tr><td>198</td><td>978</td><td>2016-06-22</td><td>2016-06-23</td><td>1</td><td>0</td></tr><tr><td>198</td><td>1011</td><td>2016-07-04</td><td>2016-07-11</td><td>7</td><td>1</td></tr><tr><td>198</td><td>1065</td><td>2016-09-18</td><td>2016-09-21</td><td>3</td><td>7</td></tr><tr><td>198</td><td>1116</td><td>2016-10-03</td><td>2016-10-04</td><td>1</td><td>3</td></tr><tr><td>198</td><td>1138</td><td>2016-10-09</td><td>2016-10-14</td><td>5</td><td>1</td></tr><tr><td>198</td><td>1161</td><td>2016-10-17</td><td>2016-10-22</td><td>5</td><td>5</td></tr><tr><td>198</td><td>1216</td><td>2016-10-29</td><td>2016-11-05</td><td>7</td><td>5</td></tr><tr><td>198</td><td>1420</td><td>2017-01-05</td><td>2017-01-10</td><td>5</td><td>7</td></tr></table>"
                    },
                    "metadata": {}
                }
            ],
            "execution_count": 8
        },
        {
            "cell_type": "code",
            "source": [
                "--Kérdezzük le szálláshelyenként, hogy ott összesen hány főre foglaltak (felnőtt + gyermek együttesen)!\r\n",
                "\r\n",
                "--a. Szűrjük le a legkevesebb foglalással rendelkező szálláshelyet!\r\n",
                "\r\n",
                "--b. Csak a szálláshely neve és a foglalásszám jelenjen meg!\r\n",
                "\r\n",
                "\r\n",
                "SELECT  sum(f.GYERMEK_SZAM+f.FELNOTT_SZAM),\r\n",
                "        SZALLAS_NEV\r\n",
                "from foglalas f join szoba sz on f.SZOBA_FK=sz.SZOBA_ID\r\n",
                "                join szallashely szh on szh.SZALLAS_ID=sz.SZALLAS_FK\r\n",
                "group by SZALLAS_NEV\r\n",
                "where sum(f.GYERMEK_SZAM+f.FELNOTT_SZAM) not in \r\n",
                "(\r\n",
                "    SELECT\r\n",
                "    from foglalas f join szoba sz on f.SZOBA_FK=sz.SZOBA_ID\r\n",
                "                join szallashely szh on szh.SZALLAS_ID=sz.SZALLAS_FK\r\n",
                ")\r\n",
                "\r\n",
                ""
            ],
            "metadata": {
                "azdata_cell_guid": "af21de55-be26-41fa-acfe-1f3b54bc5cac",
                "language": "sql",
                "tags": []
            },
            "outputs": [
{
    "output_type": "error",
    "evalue": "Msg 156, Level 15, State 1, Line 13\r\nIncorrect syntax near the keyword 'where'.",
    "ename": "",
    "traceback": []
}, {
    "output_type": "display_data",
    "data": {
        "text/html": "Total execution time: 00:00:00.004"
    },
    "metadata": {}
}
],
            "execution_count": 2
        }
    ]
}