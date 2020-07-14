def insert_sort(lst):
    count = 0
    for i in range(0, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
            count += 1
        lst[j + 1] = key

    return count


st = "-84077 96950 29391 -66148 66021 -63427 -51548 22496 87856 -43008 33293 -58260 -45920 97736 35216 54199 7667 -48216 -83820 38146 26771 -83753 -15078 -62875 -38316 -73927 -79357 31673 15475 18677 57233 40224 -78033 -34868 -92516 12571 -57415 -65565 -86453 28712 -74217 -62044 -97318 89917 -40128 81286 52886 86614 -2474 -80740 48094 19391 38479 95006 -77936 99473 -67160 -28857 82559 -1743 -10225 63275 -83566 -16792 -70702 -96475 77356 79631 62739 -5781 37081 29046 1544 41229 -40140 -19120 -18601 -72975 64718 90251 -58970 -63616 60962 -1752 -15810 39851 -71892 4394 -17077 97294 4804 49761 -47430 2607 84214 51496 5353 -90679 1704 27247 -82638 65718 53369 20 63299 -61038 76951 -55819 51286 16748 70290 -87701 -52071 -88741 67748 81187 13399 -9757 83885 -90449 -83623 -86352 -43081 2913 87518 -8505 -7230 57067 -6200 -96607 -14877 -57520 43234 1326 -52502 14654 54283 -78953 -77843 -31169 -10232 13166 35776 41381 95349 45182 12198 55635 -65533 97711 27280 17351 -51221 43278 -54071 48734 -3547 -95273 -89676 -92522 -4254 -28317 -44129 -11391 97842 -80218 98750 -91240 -2995 30918 33787 -90782 35203 12017 -64401 -83556 69361 56178 -20150 -15865 71457 12145 10812 -94004 88111 -58772 -59035 76269 -30317 -92540 -73150 27629 -10019 2872 -57897 -30503 -84445 -86570 -43190 -86265 74265 57110 56908 16963 -831 -50940 47367 59749 42346 -80962 6331 -73477 44777 25608 -27074 -35242 -35096 83599 58811 -71959 -64658 -10958 48250 -62469 -1453 -44378 -38402 48274 -56860 19727 -813 8288 -20482 -39845 61639 91811 -4304 92140 -3456 1277 69818 64232 -88144 -70097 72231 59770 -17762 77615 -61352 17087 69290 23729 44954 69202 -20332 79789 78007 34083 99455 30872 24223 -8464 899 -61204 -74739 -40783 88942 -36813 -99542 -30563 36035 32613 50844 -13143 -7487 -43670 -73750 67618 87746 -31340 -27752 50029 58087 -56792 -30763 -74337 18188 22480 -75929 38392 95386 83910 -7413 91244 69495 22149 -87103 -7612 54836 46051 -6988 -82821 71981 -44882 -27538 67971 -4368 -44496 40695 91045 92028 -43522 97552 -8519 -66546 -85765 -77672 17160 15783 -66746 -9576 66932 34677 -76177 -20153 -83420 -59971 18186 -56234 64331 20275 23263 82773 -33198 49996 -41110 -21624 66820 8191 -57510 32161 -53273 53403 82165 29613 -34773 39497 -34423 83245 58067 2404 -8061 22717 -35911 83198 -22333 -85076 -42604 56023 27024 6975 -18034 98911 4704 -33411 -97879 -21667 71426 25749 28788 -35304 -80794 75135 -2936 33333 3591 83384 86821 16646 37568 85511 39857 38700 -45031 50034 -78941 -42130 -72728 -14427 -25850 -434 44899 72733 -90029 25088 49633 35500 -54186 -58640 82870 78200 36028 41936 -29618 64641 50966 79611 35259 86135 64502 -46255 -77486 -44350 -81372 -29906 -12838 -47866 -47573 -73817 95930 62092 -18039 20550 18309 -75362 -3513 -85314 9595 76576 99164 9278 -43913 -22547 -75731 -7122 -27236 -43568 -30683 17942 79548 -16181 -29216 68117 -95324 -40612 3544 -32428 67002 -24675 41364 29972 -93152 -37040 -6023 -87669 -20803 83625 -27196 -56855 17205 -95389 -16572 -27805 -24213 -73019 -62366 28635 62912 20128 -90817 23308 93717 -4257 60222 -95653 54648 -59691 -16636 12635 30776 -77129 13623 16884 -15329 -27841 15564 28109 -74066 68073 23867 2480 75165 2882 -69785 1498 78042 -66238 -55943 -73746 43187 -15736 -82326 -18048 -10722 62122 65247 9828 -70588 10925 50164 -62899 90529 -7476 -70088 -42541 -10983 11947 88310 16206 -48755 -75407 -95033 33053 -55415 -40498 -4168 -78985 87142 -82016 20591 -862 93162 -80199 -97066 92025 -10166 15222 -41202 -50968 28980 -81239 52267 -47402 -18939 26606 80638 -28616 -90379 85112 -75022 -49433 -25403 69187 68736 82631 -50341 -94558 51839 -97973 77248 -8624 30625 -19573 551 13677 42209 -88077 -61887 -30379 78155 12206 -5934 -85881 3416 90886 -57518 8249 -7155 -6151 35702 -32909 -3273 -88445 -76047 52619 -80080 -86415 87666 87736 -17522 -41503 -91317 -36848 -87355 -68307 -72323 -3577 -80841 19128 -90895 -81456 71007 50947 -90572 -32835 -95461 36428 65104 -8051 95791 -36695 77946 63553 -53729 29821 -58365 27278 -10223 -55157 -17284 -85231 63827 -5529 33457 -29421 7668 -88826 74454 -10380 44766 66648 -50880 36950 3077 53736 41957 58613 97780 57908 15500 -22311 -10833 -63264 -80613 -44732 -65680 -58650 -13968 22350 -48676 2817 97998 56286 -48708 -3061 36586 44762 -95340 -15922 -38166 -56486 -22354 -73417 -99048 82425 -49912 84734 -57926 2144 -56477 -73814 -67882 -67023 -84620 22328 4664 -90555 10560 -35710 75991 88929 -56985 61908 86603 -76006 84868 91092 -6741 -71314 -78653 -83244 31067 -94759 57344 54278 -6031 -34936 72327 -24973 30885 -84680 86915 -96271 -11981 69360 -80028 33249 -90740 90481 57393 -89504 -36350 -18219 53027 17604 -5569 -72705 -6106 26357 -95544 57791 -46862 -12666 78047 -10784 -185 -32711 197 18408 71379 -9377 -11625 81598 65075 -36905 -30535 -5367 86416 -59113 83477 -43043 35899 75846 -25657 -26897 -91785 -32249 75762 -69919 -28321 31169 37284 46228 33272 -48045 74038 97625 35039 56053 14783 36778 58448 -283 46558 -27042 89560 -13031 72244 59093 82733 -29822 -68117 46370 -43418 48505 -946 41883 -2957 14549 94895 -11765 19474 -19520 -31422 2915 2102 -94643 21069 45251 90448 56023 14635 60645 21451 -24802 9706 -88604 68316 43880 67041 -18335 -77190 40107 91482 -28104 59513 -79111 77328 -40961 -87177 1410 34997 26860 -17773 82409 -9410 52149 98518 -74469 -20036 -10153 23401 -15475 -17835 77600 -57279 -26657 -97231 -60796 76697 -83779 1383 70115 63437 55099 -84468 -76060 11006 93309 -91476 -20153 -68995 -55533 65488 25256 -92214 -38688 48061 -4878 -90485 -87862 20739 -85054 -240 98760"
lst = st.strip().split()

print(insert_sort(lst))

for
