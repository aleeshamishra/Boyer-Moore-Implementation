import org.bson.Document;
import org.bson.conversions.Bson;

import com.mongodb.MongoClient;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.model.Filters;
import com.mongodb.client.model.Projections;

public class BoyerMooreTest {
	private static final String DATABASE_NAME = "BM";
	private static final String COLLECTION_NAME = "BM_DATA";
	private static final MongoClient CLIENT = new MongoClient();

	public static void main(String[] args) {
		MongoCollection<Document> collection = CLIENT.getDatabase(DATABASE_NAME).getCollection(COLLECTION_NAME);
		Bson projection = Projections.fields(Projections.include("data"), Projections.excludeId());
		BoyerMoore boyerMoore = new BoyerMoore();

		for (int i = 1; i <= 54; i++) {
			Bson filter = Filters.eq("seq", i);
			String text = collection.find(filter).projection(projection).first().toJson();
			String pattern = text.substring(0, text.length() - 1) + "!";

			long startTime = System.nanoTime();
			int position = boyerMoore.search(text, pattern);
			long endTime = System.nanoTime();
			long elapsedtime = endTime - startTime;
//			System.out.println(
//					text.length() + "     -      " + elapsedtime / 1000000 + "  milliseconds - Pattern Position found at: " + position);
			System.out.println(
					"KB: " + (double) (Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory()) / 1024);
		}

	}

}
