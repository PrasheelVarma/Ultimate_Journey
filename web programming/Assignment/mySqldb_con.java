import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

/**
 * A simple Java program to demonstrate establishing a JDBC connection to a MySQL database.
 */
public class JdbcConnection {

    public static void main(String[] args) {

        // Database connection details
        // TODO: Replace with your actual database details
        String jdbcUrl = "jdbc:mysql://localhost:3306/your_database_name";
        String username = "your_username";
        String password = "your_password";

        Connection connection = null;

        try {
            // Step 1: Register the JDBC driver
            // This is not strictly necessary for modern drivers (JDBC 4.0 and above)
            // as they are automatically loaded, but it is good practice to show.
            Class.forName("com.mysql.cj.jdbc.Driver");
            System.out.println("JDBC Driver Registered!");

            // Step 2: Establish the connection
            // The DriverManager.getConnection method attempts to establish a connection to the given database URL.
            System.out.println("Connecting to the database...");
            connection = DriverManager.getConnection(jdbcUrl, username, password);
            System.out.println("Connection established successfully!");

        } catch (ClassNotFoundException e) {
            // Catch this exception if the JDBC driver class is not found in the classpath.
            System.err.println("JDBC Driver not found. Make sure the MySQL Connector/J JAR is in your classpath.");
            e.printStackTrace();
        } catch (SQLException e) {
            // Catch this exception for any errors related to the database connection.
            System.err.println("Connection failed!");
            e.printStackTrace();
        } finally {
            // Step 3: Close the connection
            // It is crucial to close the connection in a finally block to ensure it is always closed,
            // even if an exception occurs.
            if (connection != null) {
                try {
                    connection.close();
                    System.out.println("Connection closed.");
                } catch (SQLException e) {
                    System.err.println("Error closing the connection.");
                    e.printStackTrace();
                }
            }
        }
    }
}
