#Gaussian with Labels

#Gaussian 1

#these are the inputs
input color1 = 0;
input color2 = 255;
input color3 = 0;
input color4 = 255;
input color5 = 0;
input color6 = 0;

input period3 = 16.5;

input gauss1 = no;
input gauss2 = no;
input gauss3 = yes;
input vidyaswitch = no;

input atrlengthgauss = 21;

input atrbandsgauss = yes;
input atrbandsgaussa = yes;
input atrbandsgauss2 = yes;
input atrbandsgauss2a = yes;
input atrbandsgauss3 = yes;
input atrbandsgauss3a = yes;

input multipliergauss = 0.99;
input multipliergaussa = 0.70;
input multipliergauss2 = -0.5;
input multipliergauss2a = 0.5;
input multipliergauss3 = 0.4;
input multipliergauss3a = 0.1;

input labels = yes;

input paintbars = no;
input paintbars2 = no;
input paintbars3 = no;
input paintwtd = yes;

def gaussprice = vwap;
input GFlineweight = 3;
def atrlineweight = 1;

def symbol = (6.28318531) / period3;
def beta = (1 – Cos(symbol)) / (0.18911732);

def alpha = -beta + Sqr(Power(beta, 2) + (2 * beta));

#this the engine - the guts

rec GF = (Power(alpha, 4)) * gaussprice + (4 * (1 - alpha)) * GF[1] - 6 * Power(1 - alpha, 2) * GF[2] + 4 * Power(1 - alpha, 3) * GF[3] - Power(1 - alpha, 4) * GF[4];

#this is drawing the line

#Gaussian 3

#these are the inputs
def gaussprice3 = vwap;

def symbol3 = (6.28318531) / period3;
def beta3 = (1 – Cos(symbol3)) / (0.18911732);

def alpha3 = -beta3 + Sqr(Power(beta3, 2) + (2 * beta3));

#this the engine - the guts

rec GF3 = (Power(alpha3, 4)) * gaussprice3 + (4 * (1 - alpha3)) * GF3[1] - 6 * Power(1 - alpha3, 2) * GF3[2] + 4 * Power(1 - alpha3, 3) * GF3[3] - Power(1 - alpha3, 4) * GF3[4];

#this is drawing the line

def long1 = GF3 > GF3[1];
def short1 = GF3 < GF3[1];

def long2 = GF3 > GF3[1];
def short2 = GF3 < GF3[1];

def long3 = GF3 > GF3[1];
def short3 = GF3 < GF3[1];

plot Gaussian3 = if gauss3 then GF3 else Double.NaN;
AssignPriceColor(if paintbars3 and long3 then CreateColor(color1, color2, color3) else if paintbars3 and short3 then CreateColor(color4, color5, color6) else Color.CURRENT);
Gaussian3.AssignValueColor(if long3 then Color.MAGENTA else if short3 then Color.GRAY else Color.CURRENT);
Gaussian3.SetLineWeight(GFlineweight);

#WTD EHMA

#----- Study One -----#

# WTDEHMA



#ATR 1
input usewtdatr = yes;

def atrgauss = ExpAverage(high - low, atrlengthgauss);

plot longatrgauss = if atrbandsgauss and long3 then GF3 + multipliergauss * Ceil(atrgauss / TickSize()) * TickSize() else Double.NaN;
longatrgauss.AssignValueColor(CreateColor(color1, color2, color3));
longatrgauss.SetLineWeight(atrlineweight);

plot shortatrgauss = if atrbandsgauss and short3 then GF3 - multipliergauss * Ceil(atrgauss / TickSize()) * TickSize() else Double.NaN;
shortatrgauss.AssignValueColor(CreateColor(color4, color5, color6));
shortatrgauss.SetLineWeight(atrlineweight);

plot longatrgaussa = if atrbandsgaussa and long3 then GF3 + multipliergaussa * Ceil(atrgauss / TickSize()) * TickSize() else Double.NaN;
longatrgaussa.AssignValueColor(CreateColor(color1, color2, color3));
longatrgaussa.SetLineWeight(atrlineweight);

plot shortatrgaussa = if atrbandsgaussa and short3 then GF3 - multipliergaussa * Ceil(atrgauss / TickSize()) * TickSize() else Double.NaN;
shortatrgaussa.AssignValueColor(CreateColor(color4, color5, color6));
shortatrgaussa.SetLineWeight(atrlineweight);

#ATR 2

input atrlengthgauss2 = 5;

def atrgauss2 = ExpAverage(high - low, atrlengthgauss);

plot longatrgauss2 = if atrbandsgauss2 and long2 then GF3 + multipliergauss2 * Ceil(atrgauss2 / TickSize()) * TickSize() else Double.NaN;
longatrgauss2.AssignValueColor(CreateColor(color1, color2, color3));
longatrgauss2.SetLineWeight(atrlineweight);

plot shortatrgauss2 = if atrbandsgauss2 and short2 then GF3 - multipliergauss2 * Ceil(atrgauss2 / TickSize()) * TickSize() else Double.NaN;
shortatrgauss2.AssignValueColor(CreateColor(color4, color5, color6));
shortatrgauss2.SetLineWeight(atrlineweight);

plot longatrgauss2a = if atrbandsgauss2a and long2 then GF3 + multipliergauss2a * Ceil(atrgauss2 / TickSize()) * TickSize() else Double.NaN;
longatrgauss2a.AssignValueColor(CreateColor(color1, color2, color3));
longatrgauss2a.SetLineWeight(atrlineweight);

plot shortatrgauss2a = if atrbandsgauss2a and short2 then GF3 - multipliergauss2a * Ceil(atrgauss2 / TickSize()) * TickSize() else Double.NaN;
shortatrgauss2a.AssignValueColor(CreateColor(color4, color5, color6));
shortatrgauss2a.SetLineWeight(atrlineweight);

#ATR 3

input atrlengthgauss3 = 5;

def atrgauss3 = ExpAverage(high - low, atrlengthgauss);

plot longatrgauss3 = if atrbandsgauss3 and long3 then GF3 + multipliergauss3 * Ceil(atrgauss3 / TickSize()) * TickSize() else Double.NaN;
longatrgauss3.AssignValueColor(CreateColor(color1, color2, color3));
longatrgauss3.SetLineWeight(atrlineweight);

plot shortatrgauss3 = if atrbandsgauss3 and short3 then GF3 - multipliergauss3 * Ceil(atrgauss3 / TickSize()) * TickSize() else Double.NaN;
shortatrgauss3.AssignValueColor(CreateColor(color4, color5, color6));
shortatrgauss3. SetLineWeight(atrlineweight);

plot longatrgauss3a = if atrbandsgauss3a and long3 then GF3 + multipliergauss3a * Ceil(atrgauss3 / TickSize()) * TickSize() else Double.NaN;
longatrgauss3a.AssignValueColor(CreateColor(color1, color2, color3));
longatrgauss3a.SetLineWeight(atrlineweight);

plot shortatrgauss3a = if atrbandsgauss3a and short3 then GF3 - multipliergauss3a * Ceil(atrgauss3 / TickSize()) * TickSize() else Double.NaN;
shortatrgauss3a.AssignValueColor(CreateColor(color4, color5, color6));
shortatrgauss3a. SetLineWeight(atrlineweight);

#Labels

input tickdecimal = 2;

#current candle

AddLabel(long3 and labels, "Strike Price " + Round (GF3, tickdecimal), Color.MAGENTA);
AddLabel(long3 and labels, " " + Round (longatrgauss2, tickdecimal) + " " , Color.GREEN);
AddLabel(long3 and labels, " " + Round (longatrgauss, tickdecimal) + " " , Color.GREEN);
AddLabel(long3 and labels, " " + Round (longatrgaussa, tickdecimal) + " " , Color.GREEN);
AddLabel(long3 and labels, " " + Round (longatrgauss2a, tickdecimal) + " " , Color.GREEN);
AddLabel(long3 and labels, " " + Round (longatrgauss3, tickdecimal) + " " , Color.GREEN);
AddLabel(long3 and labels, " " + Round (longatrgauss3a, tickdecimal) + " " , Color.GREEN);

AddLabel(short3 and labels, "Strike Price " + Round (GF3, tickdecimal), Color.GRAY);
AddLabel(short3 and labels, " " + Round (shortatrgauss2, tickdecimal) + " " , Color.RED);
AddLabel(short3 and labels, " " + Round (shortatrgauss, tickdecimal) + " " , Color.RED);
AddLabel(short3 and labels, " " + Round (shortatrgaussa, tickdecimal) + " " , Color.RED);
AddLabel(short3 and labels, " " + Round (shortatrgauss2a, tickdecimal) + " " , Color.RED);
AddLabel(short3 and labels, " " + Round (shortatrgauss3, tickdecimal) + " " , Color.RED);
AddLabel(short3 and labels, " " + Round (shortatrgauss3a, tickdecimal) + " " , Color.RED);

#define the differences
def GF3_diff = GF3 - GF[1];
def atrgauss2_diff = longatrgauss2 - longatrgauss2[1];
def atrgauss_diff = longatrgauss - longatrgauss[1];
def atrgaussa_diff = longatrgaussa - longatrgaussa[1];
def atrgauss2a_diff = longatrgauss2a - longatrgauss2a[1];
def atrgauss3_diff = longatrgauss3 - longatrgauss3[1];
def atrgauss3a_diff = longatrgauss3a - longatrgauss3a[1];

#next candle
def second_candle = GF3 + GF3_diff;
def second_longatrgauss2 = longatrgauss2 + atrgauss2_diff;
def second_longatrgauss = longatrgauss + atrgauss_diff;
def second_longatrgaussa = longatrgaussa + atrgaussa_diff;
def second_longatrgauss2a = longatrgauss2a + atrgauss2a_diff;
def second_longatrgauss3 = longatrgauss3 + atrgauss3_diff;
def second_longatrgauss3a = longatrgauss3a + atrgauss3a_diff;

AddLabel(long3 and labels, " Next Candle ", Color.Yellow);
AddLabel(long3 and labels, " " + Round (second_candle, tickdecimal), Color.MAGENTA);
AddLabel(long3 and labels, " " + Round (second_longatrgauss2, tickdecimal) + " " , Color.GREEN);
AddLabel(long3 and labels, " " + Round (second_longatrgauss, tickdecimal) + " " , Color.GREEN);
AddLabel(long3 and labels, " " + Round (second_longatrgaussa, tickdecimal) + " " , Color.GREEN);
AddLabel(long3 and labels, " " + Round (second_longatrgauss2a, tickdecimal) + " " , Color.GREEN);
AddLabel(long3 and labels, " " + Round (second_longatrgauss3, tickdecimal) + " " , Color.GREEN);
AddLabel(long3 and labels, " " + Round (second_longatrgauss3a, tickdecimal) + " " , Color.GREEN);

def second_shortatrgauss2 = shortatrgauss2 - atrgauss2_diff;
def second_shortatrgauss = shortatrgauss - atrgauss_diff;
def second_shortatrgaussa = shortatrgaussa - atrgaussa_diff;
def second_shortatrgauss2a = shortatrgauss2a - atrgauss2a_diff;
def second_shortatrgauss3 = shortatrgauss3 - atrgauss3_diff;
def second_shortatrgauss3a = shortatrgauss3a - atrgauss3a_diff;

#third candle
AddLabel(long3 and labels, " Third Candle ", Color.Yellow);
def third_candle = second_candle + GF3_diff;
def third_longatrgauss2 = second_longatrgauss2 + atrgauss2_diff;
def third_longatrgauss = second_longatrgauss + atrgauss_diff;
def third_longatrgaussa = second_longatrgaussa + atrgaussa_diff;
def third_longatrgauss2a = second_longatrgauss2a + atrgauss2a_diff;
def third_longatrgauss3 = second_longatrgauss3 + atrgauss3_diff;
def third_longatrgauss3a = second_longatrgauss3a + atrgauss3a_diff;

AddLabel(long3 and labels, " " + Round (third_candle, tickdecimal), Color.MAGENTA);
AddLabel(long3 and labels, " " + Round (third_longatrgauss2, tickdecimal) + " " , Color.GREEN);
AddLabel(long3 and labels, " " + Round (third_longatrgauss, tickdecimal) + " " , Color.GREEN);
AddLabel(long3 and labels, " " + Round (third_longatrgaussa, tickdecimal) + " " , Color.GREEN);
AddLabel(long3 and labels, " " + Round (third_longatrgauss2a, tickdecimal) + " " , Color.GREEN);
AddLabel(long3 and labels, " " + Round (third_longatrgauss3, tickdecimal) + " " , Color.GREEN);
AddLabel(long3 and labels, " " + Round (third_longatrgauss3a, tickdecimal) + " " , Color.GREEN);
