export module filterer;
import std;
export void column_filter(std::istream& in, std::ostream& out)
{
    std::string str;
    while (std::getline(in, str))
    {
        using namespace std::views;
        using namespace std::string_view_literals;
        auto entries = str | split(" "sv) | transform([](auto&& r){return std::string_view(r);});
        for (auto [i, s] : enumerate(entries) | take(10))
        {
            // column 6 is ra, column 8 is dec, column 10 is parallax
            if (i == 6)
                std::println(out, "{}", s);
            else if (i == 8 || i == 10)
                std::println(out, ",{}", s);
        }
    }
};
