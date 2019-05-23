using System;
namespace Simplex_G
{
    class Simplex
    {
        int []x_col;
        int []x_row;
        double[,] Table;
        public Simplex(double[,] table)
        {
            Table = new double[table.GetLength(0), table.GetLength(1)];
            for (int i = 0; i < table.GetLength(0); i++)
                for (int j = 0; j < table.GetLength(1); j++)
                    Table[i, j] = table[i, j];
            x_col = new int[table.GetLength(0) - 1];
            x_row = new int[table.GetLength(1) - 1];
            for (int i = 0; i < x_row.Length; i++)
                x_row[i] = i + 1;
            int last_index = x_row.Length - 1;
            for (int j = 0; j < x_col.Length; j++)
                x_col[j] = j + x_row[last_index] + 1;
        }
        public void FullCalc()
        {
            int k, l;
            while (Analys(out k, out l))
            {
                Calculate(k, l);
                Print();
            }
            GetAnswer();
        }
        void Calculate(int k, int l)
        {
            int t;
            t = x_col[k - 1];
            x_col[k - 1] = x_row[l];
            x_row[l] = t;

            for (int i = 0; i < Table.GetLength(0); i++)
                if (i != k)
                    for (int j = 0; j < Table.GetLength(1); j++)
                    {
                        if (j == l)
                            continue;
                        Table[i, j] = Table[i, j] - Table[i, l] * Table[k, j] / Table[k, l];
                    }
                else
                    continue;
            Table[k, l] = 1 / Table[k, l];
            for (int j = 0; j < Table.GetLength(1); j++)
                if (j == l)
                    continue;
                else
                    Table[k, j] = Table[k, l] * Table[k, j];
            for (int i = 0; i < Table.GetLength(0); i++)
                if (i == k)
                    continue;
                else
                    Table[i, l] = -Table[k, l] * Table[i, l];
        }
        bool Analys(out int main_b, out int main_F)
        {
            main_b = -1;
            main_F = -1;
            int index_b = Table.GetLength(1) - 1;
            int max_index_b = 0;
            bool flag_b = false;
            bool flag_f = false;
            bool main_flag = false;
            int max_index_F = 0;
            for (int i = 1; i < Table.GetLength(0); i++)
                if (Table[i, index_b] < 0)
                {
                    max_index_b = i;
                    flag_b = true;
                    break;
                }
            if (flag_b)
            {
                for (int i = max_index_b; i < Table.GetLength(0); i++)
                    if (Table[i, index_b] < 0 && Table[max_index_b, index_b] > Table[i, index_b])
                        max_index_b = i;
                for (int f = 0; f < Table.GetLength(1) - 1; f++)
                    if (Table[max_index_b, f] < 0)
                    {
                        max_index_F = f;
                        flag_f = true;
                        break;
                    }
                if (flag_f)
                {
                    for (int f = max_index_F; f < Table.GetLength(1) - 1; f++)
                        if (Table[max_index_b, f] < 0 && Table[max_index_b, f] < Table[max_index_b, max_index_F])
                            max_index_F = f;
                    main_b = max_index_b;
                    main_F = max_index_F;
                    main_flag = true;
                    Console.WriteLine("Have Solution. Search x");
                }
                else
                    Console.WriteLine("Not solution (b)");
            }
            else
            {
                for (int f = 0; f < Table.GetLength(1) - 1; f++)
                    if (Table[0, f] < 0)
                    {
                        max_index_F = f;
                        flag_f = true;
                        break;
                    }
                if (flag_f)
                {
                    for (int f = max_index_F; f < Table.GetLength(1) - 1; f++)
                        if (Table[0, f] < 0 && Table[0, max_index_F] > Table[0, f])
                            max_index_F = f;
                    for (int i = 1; i < Table.GetLength(0); i++)
                        if (Table[i, max_index_F] > 0 && Table[i, index_b] > 0)
                        {
                            max_index_b = i;
                            flag_b = true;
                            break;
                        }
                    if (flag_b)
                    {
                        for (int b = max_index_b; b < Table.GetLength(0); b++)
                            if (Table[b, max_index_F] > 0 && Table[b, index_b] > 0 &&
                                   Table[b, index_b] / Table[b, max_index_F] <
                                   Table[max_index_b, index_b] / Table[max_index_b, max_index_F])
                                max_index_b = b;
                        main_b = max_index_b;
                        main_F = max_index_F;
                        main_flag = true;
                        Console.WriteLine("Have Solution. Search x");
                    }
                    else
                        Console.WriteLine("Not solution");
                }
                else
                    Console.WriteLine("Search x");
            }
            return main_flag;
        }
        public void Print()
        {
            Console.Write("\t");
            for (int i = 0; i < x_row.Length; i++)
                Console.Write(x_row[i] + "\t");
            Console.Write("b\n");
            Console.WriteLine("-------------------------");
            Console.Write("F|\t");
            for (int j = 0; j < Table.GetLength(1); j++)
                Console.Write($"{Table[0, j]:0.###}\t");
            Console.WriteLine();
            for (int i = 1; i < Table.GetLength(0); i++)
            {
                Console.Write($"{x_col[i - 1]}|\t");
                for (int j = 0; j < Table.GetLength(1); j++)
                    Console.Write($"{Table[i, j]:0.###}\t");
                Console.WriteLine();
            }
        }
        public void GetAnswer()
        {
            double x1 = -100, x2 = -100;
            int index_b = Table.GetLength(1) - 1;
            for (int i = 0; i < x_row.Length; i++)
            {
                if (x_row[i] == 1)
                    x1 = 0;
                if (x_row[i] == 2)
                    x2 = 0;
            }
            for (int i = 0; i < x_col.Length; i++)
            {
                if (x_col[i] == 1)
                    x1 = Table[i + 1, index_b];
                if (x_col[i] == 2)
                    x2 = Table[i + 1, index_b]; ;
            }
            Console.WriteLine($"x1 = {x1:0.###}, x2 = {x2:0.###}");

        }
        /*
         double[,] table_int_main = new double[,]
            {
                { -1, -2, 0 },
                { 2, 2, 7 },
                { 4, -5, 9 },
                { 0, 1, 3 },
                { 1, 0, 0 }
            };
            Simplex_G.Simplex s = new Simplex_G.Simplex(table_int_main);
            s.Print();
            s.FullCalc();
         */
    }
}