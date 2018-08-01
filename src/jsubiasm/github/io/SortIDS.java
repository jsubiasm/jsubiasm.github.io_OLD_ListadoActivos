/**
 * 
 */
package jsubiasm.github.io;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;

/**
 * @author Empleado
 *
 */
public class SortIDS
{

	/**
	 * @param args
	 */
	public static void main(String[] args) throws Exception
	{
		Map<Long, String> map = new HashMap<Long, String>();

		BufferedReader reader = new BufferedReader(new FileReader("C:\\_PELAYO\\Software\\Eclipse Neon\\workspace\\jsubiasm.github.io_OLD_ListadoActivos\\anterior_a_github\\testR.txt"));

		String line = null;
		while ((line = reader.readLine()) != null)
		{
			try
			{
				map.put(Long.valueOf(line), "OK");
			}
			catch (Exception e)
			{
				System.out.println("Error al parsear [" + line + "]");
			}
		}
		reader.close();

		List<Long> lista = new ArrayList<Long>();
		lista.addAll(map.keySet());
		Collections.sort(lista);

		BufferedWriter writer = new BufferedWriter(new FileWriter("C:\\_PELAYO\\Software\\Eclipse Neon\\workspace\\jsubiasm.github.io_OLD_ListadoActivos\\anterior_a_github\\testW.txt"));
		for (Iterator<Long> iterator = lista.iterator(); iterator.hasNext();)
		{
			Long id = (Long) iterator.next();
			writer.write("" + id + "\n");
		}
		writer.close();
	}

}
