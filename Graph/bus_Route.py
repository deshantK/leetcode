import time
import queue
def solve(bus_dic, adj, src, dest):
    #q = queue.Queue()
    q = []
    q.insert(0, (src, 0))
    visited = set()
    while q:
        st, cnt = q.pop()
        if st == dest:
            return cnt
        visited.add(st)
        bus = adj[st]
        for b in bus:
            sts = bus_dic[b]
            for s in sts:
                if s not in visited:
                    q.insert(0,(s, cnt+1))
    return -1

    



bus_route = [[1,2,8,12,15,18,42,43,49,51,58,67,69,71,85,92,102,113,121,135,136,140,206,216,231,247,260,261,263,269,271,276,286,290,304,314,322,330,335,338,339,349,357,362,364,373,379,387,406,417,427,445,461],[82,84,171,184,187,343,455],[12,23,48,65,95,98,99,116,131,151,156,157,159,162,173,176,188,209,214,231,243,244,249,282,303,323,328,336,339,344,349,355,361,370,395,399,423],[1,4,13,15,17,40,43,50,55,56,63,65,67,68,72,77,81,87,88,89,101,106,107,114,116,126,128,131,132,135,140,148,161,164,170,171,173,176,177,178,180,183,188,192,198,211,221,232,242,256,257,262,270,273,274,275,277,282,283,284,300,326,341,343,344,355,365,373,381,385,388,405,414,415,419,426,428,432,435,447,453,465,467,468,473],[0,8,9,10,22,40,43,44,51,55,62,70,85,99,103,104,110,118,122,124,139,148,169,192,196,199,202,203,204,209,222,224,242,243,258,259,260,268,270,281,283,294,325,342,343,349,352,355,357,374,378,386,387,390,409,423,431,438,439,440,460,472],[142,184],[6,23,27,30,37,38,48,60,88,112,126,159,175,211,212,217,245,249,278,298,335,342,359,374,385,408,422,444,450,452,455,464,474],[9,60,61,91,93,103,122,124,134,138,143,148,170,197,204,205,210,212,215,247,256,257,265,275,279,287,305,311,312,321,336,338,342,350,351,352,353,370,372,374,401,422,454,456,461],[15,17,29,38,43,59,68,71,83,92,101,107,125,126,142,145,176,178,184,189,193,195,198,200,208,213,224,229,231,233,244,251,265,272,274,297,314,315,325,334,363,367,369,373,374,414,436,439,444,449,464],[18,41,64,69,102,108,135,136,148,171,173,192,193,221,224,285,303,313,344,355,395,420,428,432,474],[3,6,13,16,20,21,26,29,34,37,42,64,70,85,87,94,100,117,125,135,141,142,149,150,159,161,163,166,172,177,180,188,209,217,225,243,247,252,253,256,258,273,285,290,300,301,302,303,313,323,327,334,337,345,354,358,362,363,372,374,391,392,399,403,406,410,412,414,428,436,440,444,455,456,461,470],[3,10,13,21,25,34,38,45,46,47,52,54,57,63,75,85,86,88,93,95,97,99,105,121,125,128,145,153,154,156,163,166,177,180,181,189,205,211,213,220,266,277,280,297,298,299,308,337,338,346,360,365,366,367,375,396,398,406,410,417,423,428,439,450,451,459,466,473],[5,13,20,24,32,35,38,43,48,49,57,61,71,81,84,90,94,99,107,118,119,127,131,140,142,147,150,155,163,178,187,201,214,215,218,223,225,236,243,250,266,270,273,275,296,297,298,306,307,314,315,316,319,320,322,331,356,358,362,366,369,371,378,383,386,387,392,394,399,400,406,412,415,420,427,430,439,440,444,459,464,468,469],[0,9,27,31,47,48,55,58,60,63,75,87,95,101,109,120,124,125,129,151,160,164,176,179,231,235,252,259,260,299,304,309,315,317,319,324,364,386,389,405,415,417,421,424,437,439,469,474],[2,6,7,15,19,26,34,36,40,49,50,51,54,63,74,82,83,84,85,93,98,107,125,129,131,134,138,144,147,173,182,186,205,206,213,223,230,237,238,242,250,251,264,270,280,284,286,287,300,301,313,315,319,326,332,336,337,340,355,356,361,363,365,370,375,394,396,397,399,414,415,428,431,435,437,440,444,451,457,461,464,466,472],[22,28,37,39,45,59,63,65,89,97,108,110,120,122,145,150,157,158,167,173,180,183,186,187,195,196,197,202,203,204,206,211,213,218,228,246,250,251,274,280,293,294,317,318,328,334,351,353,360,365,376,377,388,393,396,421,422,423,424,435,441,451,459,460,464,472,473],[0,6,13,14,20,37,46,51,70,74,90,91,100,110,121,131,150,161,178,181,202,203,206,215,223,225,235,237,248,252,256,261,269,287,290,293,312,316,318,325,335,337,344,350,363,364,375,376,410,414,417,418,423,428,431,445,452,465,469,471],[7,26,34,37,38,39,40,41,42,49,50,51,74,88,90,98,101,104,105,106,111,127,133,140,145,152,159,161,167,168,181,183,186,188,197,215,222,235,236,238,246,251,254,259,262,271,278,287,288,304,312,313,322,325,326,330,334,335,340,343,353,357,362,363,370,379,382,385,392,401,404,405,417,420,423,432,433,436,437,440,443,447],[2,13,35,36,40,50,59,76,82,96,97,100,108,115,124,140,141,146,148,151,157,164,165,166,169,172,177,185,187,193,196,212,220,221,240,260,268,273,278,281,284,295,299,314,325,327,346,365,379,395,396,398,405,407,408,417,436,448,462,463],[4,12,18,21,33,45,65,69,71,73,74,83,84,94,98,103,112,114,118,139,141,145,147,166,183,187,189,195,202,220,226,237,240,242,252,254,263,265,268,274,277,278,284,305,317,325,332,356,357,358,372,382,385,386,387,391,396,398,401,403,409,425,437,438,444,447,456,458,459,466],[1,3,17,22,25,37,57,62,98,99,104,118,130,149,199,204,230,263,302,307,319,340,390,426,439,443,451],[12,18,20,24,30,41,42,56,58,64,69,78,83,87,92,98,99,103,117,119,123,126,139,143,156,163,171,176,178,181,182,189,194,204,236,238,244,245,246,250,252,255,261,269,270,273,275,276,277,292,294,317,324,325,330,352,359,368,370,372,397,403,410,425,426,429,431,434,442,447,452,463,471],[17,22,63,77,80,124,129,141,173,175,177,185,190,211,214,223,232,238,240,241,261,285,289,306,328,344,346,357,369,370,376,395,418,421,424,451,452,457,463,474],[20,30,80,82,85,99,104,129,134,145,146,148,149,167,169,177,178,229,235,246,249,264,278,335,336,381,392,428,454],[3,4,13,22,24,31,34,36,43,45,54,56,57,59,63,65,67,72,77,86,90,93,95,99,101,113,120,123,125,126,133,135,136,139,141,151,169,193,197,204,208,209,219,223,234,241,245,247,264,275,287,290,308,311,313,318,321,330,331,335,339,346,349,350,357,367,384,386,387,396,409,423,429,450,456,467],[40,157,178,196,210,224,305,318,353],[24,36,37,46,57,58,63,78,100,113,116,126,141,155,158,169,182,193,198,205,215,239,240,243,247,248,277,311,312,337,338,349,353,363,373,380,387,393,400,406,422,424,425,434,440,441,447,452,461],[36,82,97,103,107,137,227,239,245,251,270,290,301,339,429,470],[6,14,29,31,32,50,64,69,70,75,93,94,97,99,103,107,109,111,140,151,162,172,183,185,191,195,212,236,238,247,253,261,283,287,288,299,301,308,318,323,324,333,346,349,350,353,357,358,359,363,388,389,391,402,407,423,456,457,460,462,465,473],[1,16,17,33,47,78,82,94,96,99,110,116,117,125,126,141,150,154,157,182,186,227,232,235,236,238,242,255,257,276,279,290,302,303,309,315,330,331,333,352,359,360,374,389,392,396,405,415,425,435,452,453,474],[3,18,21,26,27,29,37,39,43,52,60,61,62,76,84,87,128,129,132,142,145,148,185,200,232,237,240,265,269,281,282,291,307,309,317,334,345,347,351,352,355,394,408,414,417,421,428,446,454,457,463,473],[98,273,299,362,411],[0,8,9,10,15,19,22,27,57,60,112,121,129,140,157,171,199,205,213,244,275,277,284,309,321,324,326,332,345,349,351,356,379,393,399,420,425,432,434,440,456,462,464,468],[2,3,14,24,38,40,49,68,71,73,75,85,107,130,140,142,171,173,174,175,183,188,190,195,196,207,212,222,233,237,239,241,267,282,298,310,313,316,338,341,344,348,357,358,374,381,384,398,413,424,426,436,460,468,469,472],[6,7,11,13,14,21,24,27,46,56,63,69,94,96,98,99,113,121,125,139,141,144,155,172,178,201,207,211,221,223,229,235,237,238,239,241,243,245,266,270,287,304,319,320,324,327,349,350,358,364,376,385,393,396,402,407,416,419,420,422,429,436,438,443,446,450,456,469],[0,10,13,14,16,22,26,41,55,57,62,69,72,85,115,117,119,120,123,151,161,171,174,181,183,196,202,214,219,228,232,233,237,238,241,246,247,248,251,267,297,306,319,330,344,348,357,360,367,368,388,394,395,396,421,423,429,436,437,438,443,445,457,463,467,469],[0,1,9,14,47,58,103,104,107,153,157,160,164,171,178,179,180,189,216,220,225,261,262,279,291,297,300,306,312,395,398,446,450,465],[0,1,5,16,19,32,42,52,56,57,78,85,88,115,121,135,136,138,148,157,158,165,167,169,172,182,190,191,199,201,206,212,218,220,223,238,239,264,268,269,273,284,285,292,294,298,300,307,315,320,324,325,331,341,342,349,355,372,386,388,411,417,423,436,438,441,450,462],[57,59,70,89,90,102,110,116,117,121,122,135,136,140,149,163,166,191,193,277,279,289,301,327,335,338,346,363,365,378,382,383,397,400,418,419,430,450,454],[12,27,37,40,47,51,56,59,62,70,88,101,110,114,127,133,143,161,162,163,164,175,183,185,186,187,196,198,204,208,213,215,223,226,227,233,234,241,245,246,257,260,272,276,299,304,307,309,319,322,337,339,340,358,360,362,363,370,371,403,405,406,407,410,415,416,423,427,444,450,454,472],[5,21,46,53,60,90,91,100,101,111,119,131,145,177,178,186,194,217,221,225,226,234,266,287,290,323,326,336,342,343,349,378,386,387,390,397,415,430,448,451,459,461],[7,10,27,44,49,70,100,102,111,122,128,154,155,183,188,191,198,221,223,227,234,237,247,253,255,268,302,313,317,330,340,371,383,384,392,398,400,412,425,439,450,461,463,474],[6,10,11,17,19,28,41,50,53,70,73,87,88,95,111,123,124,128,132,139,142,150,152,155,161,164,167,172,173,175,200,204,208,213,219,221,222,226,234,235,240,242,254,259,260,266,269,273,274,286,294,314,321,324,325,328,335,339,343,346,350,352,353,367,368,370,382,396,404,406,409,412,415,421,438,445,447,452,465,474],[1,10,15,41,49,56,64,73,74,75,76,80,83,110,112,117,122,128,145,150,151,154,164,166,177,189,195,196,212,215,225,234,236,239,240,270,274,279,291,302,314,316,324,331,332,343,348,352,354,355,366,373,379,408,419,420,425,436,441,442,444,445,447,463,464,468],[1,2,6,8,11,22,23,26,27,39,40,42,48,62,65,67,74,79,105,120,122,127,130,132,142,143,149,151,152,173,176,182,187,190,196,203,218,219,220,225,232,238,248,251,253,258,261,262,264,269,273,277,280,282,291,327,332,334,337,340,346,361,365,373,375,392,406,408,416,443,444,453,458,469],[47,67,88,90,154,163,223],[101,105,140,195,223,389,471],[6,11,14,20,25,30,36,46,50,55,56,59,61,78,80,99,102,104,106,119,130,134,138,149,151,154,155,158,161,169,182,192,196,197,212,213,216,224,225,244,249,258,266,272,277,279,282,284,288,293,294,295,303,304,308,312,313,314,319,327,329,335,346,352,356,358,369,373,374,400,409,411,414,416,422,424],[2,4,31,33,37,39,42,43,50,57,66,82,88,99,101,107,108,114,120,135,138,141,142,148,155,157,195,197,199,224,238,248,257,283,295,299,306,327,329,332,333,348,352,353,372,373,383,398,399,401,405,429,430,440,447,449,450,457,462],[10,14,16,17,21,23,26,28,32,41,44,61,62,66,74,81,115,118,136,154,157,164,166,169,173,180,197,209,210,214,218,234,239,241,243,244,245,261,274,278,279,282,285,299,317,320,331,334,352,369,370,371,397,400,407,414,424,429,433,437,443,445,447,452,454,463,470],[3,13,52,60,63,76,95,103,142,154,178,201,220,223,298,315,348,402,414,438,448],[0,19,54,76,85,114,153,185,215,217,241,257,304,363,378,391,408],[20,33,34,90,91,103,149,154,178,187,260,261,273,292,342,344,375,378,382,386,424,436,437],[101,162,179,202,280,286,351,417],[57,134,242,292,312,335,418],[5,40,43,45,150,185,207,215,227,255,259,284,285,288,311,320,321,338,354,382,387,408,416,438,470],[7,9,15,22,27,44,47,53,60,83,86,90,93,94,98,100,101,109,112,113,120,126,130,132,133,147,153,160,181,183,187,193,198,209,212,217,227,231,232,236,239,240,243,251,259,260,262,265,273,291,296,298,299,307,308,310,314,328,336,340,342,343,352,361,379,388,392,403,404,411,417,424,432,435,437,440,448,459,464],[5,10,18,32,40,42,54,55,62,63,64,66,67,78,79,81,101,106,111,119,132,137,144,145,148,153,166,167,175,181,183,187,198,203,204,206,217,226,230,231,233,241,251,258,263,269,271,273,279,283,288,297,305,315,323,328,331,338,345,346,347,348,355,361,369,371,382,383,389,391,395,399,400,402,416,425,428,429,430,442,444,449,470],[0,5,10,13,17,22,48,55,56,60,63,65,66,79,90,106,111,133,157,160,194,196,201,206,244,262,267,273,278,282,298,300,309,311,316,327,328,339,342,350,360,361,363,370,374,379,384,388,389,392,403,427,437,445,448,450,468],[26,52,53,56,57,60,62,67,77,82,86,88,93,96,124,153,156,173,177,178,191,194,195,221,226,260,266,267,282,295,305,317,327,328,332,333,335,342,347,350,355,363,376,378,379,419,424,427,428,431,438,442,446,451,452,457,460,474],[23,43,65,71,75,91,117,120,128,151,175,177,182,194,241,263,267,272,279,291,327,334,337,381,392,458],[4,15,30,34,52,60,63,64,72,73,78,87,96,97,110,119,121,123,124,126,136,139,141,154,164,167,176,177,189,195,199,201,202,204,211,216,222,234,242,246,248,256,263,286,293,295,314,317,322,325,335,338,342,354,356,357,364,367,380,384,391,397,400,401,403,412,413,416,419,450,455,456,457,459,464],[11,43,44,49,54,74,95,102,131,143,148,160,178,187,188,193,196,207,211,213,216,221,229,246,248,266,269,277,295,303,340,355,356,363,369,380,407,416,436,467,472],[137,300,308],[10,24,32,39,44,54,73,101,102,106,113,137,140,154,191,195,204,247,254,259,275,292,308,327,356,367,377,378,398,404,425,446,447,454,463,466],[1,5,30,60,64,94,129,135,142,145,162,205,210,213,222,246,252,256,259,263,275,278,306,309,338,348,368,411,449,463],[0,6,27,31,40,42,55,66,70,76,81,106,122,146,147,148,149,152,165,169,183,187,192,194,197,200,207,209,211,219,228,234,235,239,247,251,255,256,257,261,269,274,279,282,289,291,302,307,311,312,331,333,338,365,367,373,382,385,392,397,402,407,412,430,451,455,469,470],[4,5,14,15,20,41,51,73,80,85,90,106,115,136,141,144,148,149,159,162,180,187,213,225,227,234,255,272,281,287,290,319,324,360,362,370,375,376,390,397,401,404,405,436,445,449,459,469,473],[14,36,46,76,103,119,125,132,138,151,156,171,189,201,238,245,273,286,292,308,326,340,344,363,373,377,470],[43,50,53,57,67,80,88,89,94,98,104,109,130,143,149,176,183,186,188,199,210,217,219,226,228,229,231,256,259,283,293,298,308,313,314,315,323,349,356,363,374,389,393,398,402,410,419,458,468],[6,8,31,46,51,62,66,67,68,74,90,97,121,123,125,136,150,154,156,161,182,199,223,233,238,261,266,278,290,294,295,298,299,304,310,314,322,324,329,344,358,363,371,388,390,391,396,401,404,409,412,421,422,426,442,445,456,459,461,462,467,471,473],[50,65,70,89,94,99,141,143,154,167,170,177,188,199,203,218,246,248,250,256,268,274,283,294,310,423,439,459,460,464,474],[3,8,9,17,31,32,33,39,48,49,52,56,61,71,76,79,88,103,109,123,139,140,149,156,176,180,186,187,201,204,210,236,260,261,266,269,279,280,287,291,296,304,317,335,338,339,348,350,355,363,367,377,391,392,394,398,401,429,447,448,462,467,470,472],[0,1,3,4,9,29,31,34,39,45,51,53,58,59,64,66,74,88,89,98,99,100,108,109,110,112,113,131,140,148,154,156,165,169,172,190,199,213,228,246,247,253,257,258,264,267,268,274,286,296,300,302,307,312,322,333,362,370,390,391,393,399,412,423,429,432,443,444,455,462,463,467],[2,6,17,43,46,59,69,72,74,76,83,92,97,116,118,129,142,144,147,151,166,167,175,184,211,215,221,224,239,244,256,344,346,366,369,371,374,375,386,389,399,406,407,414,416,450,471],[1,5,9,11,17,24,25,27,29,34,36,37,39,40,42,47,63,65,66,76,88,93,95,96,112,115,126,131,132,136,142,146,150,159,160,162,166,169,175,177,185,207,226,227,229,231,241,243,253,257,263,273,274,276,280,283,286,293,298,299,301,308,313,318,326,330,331,338,343,358,366,377,385,388,394,397,400,403,428,435,445,452,461,469,474],[3,25,37,57,109,186,271,294,439,453,463,465],[98,99,125,159,178,266,270,278,297,330,405,466,470],[4,14,20,81,85,95,115,134,197,205,230,231,257,284,310,363,378,382,390,396,413,423,438],[4,11,15,21,49,59,65,67,68,72,74,98,115,123,157,192,205,220,221,232,252,258,261,272,280,290,292,300,308,315,319,339,347,350,355,361,364,368,380,389,398,399,410,413,416,418,422,427,433,438,440,454,473],[6,23,40,42,49,56,57,79,82,87,88,103,114,116,124,130,158,160,165,243,290,358,390,398,407,428,443,453],[1,3,4,15,21,52,62,70,86,100,103,123,130,136,140,150,151,159,160,162,170,174,175,177,189,191,195,197,199,201,205,207,212,214,224,231,237,239,243,252,264,267,274,276,277,298,310,317,319,326,330,332,335,336,347,348,353,355,359,362,370,379,398,401,403,415,417,431,434,436,439,445,453,455,458,464,469,470,472,473],[16,24,28,41,54,63,69,70,77,80,84,88,90,94,111,117,135,142,144,153,158,164,172,176,178,186,187,207,210,237,243,247,264,272,276,279,288,297,300,308,313,317,320,328,359,363,409,415,428,429,441,462,467],[16,27,28,34,68,71,72,99,109,118,119,150,152,190,195,203,218,224,231,235,237,241,243,260,269,285,295,303,312,315,323,347,355,380,410,441,449],[14,27,42,63,74,79,93,103,105,114,125,127,130,137,138,142,144,181,188,228,230,246,295,309,356,392,422,459,464],[32,42,62,81,82,85,93,97,111,128,136,141,142,188,194,198,229,251,274,283,294,295,346,353,402,409,410],[8,21,32,46,50,65,80,86,97,102,118,123,124,131,135,140,159,193,211,212,228,237,239,243,266,284,300,313,360,386,402,412,416,428,430,440,448,452,455,460,469],[1,4,11,26,53,65,69,80,85,89,94,97,108,119,120,121,128,144,152,174,175,177,179,199,217,229,249,261,267,277,279,283,297,300,302,313,314,324,327,343,344,347,358,359,362,369,377,380,407,413,416,417,424,427,429,439,444,445,447,462,473],[23,159,200,229,265,381,438],[9,17,25,56,61,79,108,156,163,164,175,176,188,193,223,249,262,271,278,289,292,299,303,305,320,333,349,358,373,375,377,395,407,437,447,448,468,472],[7,16,20,25,26,32,33,43,44,52,67,69,86,92,96,114,131,139,156,170,183,184,185,189,190,206,215,252,254,259,262,268,283,284,289,291,295,301,304,326,349,355,357,359,361,362,365,372,374,392,406,408,411,423,424,444,446,470],[3,7,14,15,16,18,35,45,51,52,63,68,76,82,86,93,96,97,101,107,108,133,147,149,153,154,160,161,163,166,177,180,190,192,199,201,202,205,219,230,238,246,247,249,262,267,269,273,274,277,278,279,282,283,287,293,296,299,309,310,329,334,336,343,347,349,367,383,396,406,409,413,416,425,437,441,458,463,467,468,470],[2,12,23,38,40,53,79,100,110,119,128,138,140,163,164,167,170,171,179,194,202,241,254,256,260,263,276,286,297,301,343,355,369,385,389,395,405,406,425,430,431,441,445,466],[5,26,39,40,45,49,61,70,71,86,91,100,105,114,118,130,131,153,156,158,167,184,193,201,221,223,225,230,232,233,234,235,261,271,308,317,321,330,333,335,341,345,363,370,371,379,385,390,394,408,409,410,413,423,426,427,428,437,438,439,446,448,457,464],[8,11,13,17,18,20,41,51,55,60,68,74,76,85,92,112,121,124,139,144,154,159,173,176,178,179,181,186,189,194,195,197,207,213,218,228,247,251,261,268,273,274,276,277,287,298,311,315,319,321,328,336,338,348,350,351,354,356,366,367,369,374,379,390,403,409,413,417,423,424,425,426,430,466]]

src = 107
dest = 158
adj = {}
bus = "bus"
bus_dic = {}
for i in range(len(bus_route)):
    bus_no = bus+str(i)
    stations = bus_route[i]
    bus_dic[bus_no] = stations
    for s in stations:
        if s not in adj:
            adj[s] = []
        adj[s].append(bus_no)
#print (adj)
#print (len(bus_dic))
start = time.time()
cnt = solve(bus_dic, adj, src, dest)
end = time.time()
print ((end-start)*1000)
print (cnt)