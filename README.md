Finance Application
An application where you can input and track your expenses and transactions.

TEAM
Team Members: George Jeff Onyango
Role: Do the whole project from scratch to the end.
Why role: it is best that the role sharpen our role in APIs and CLIs

TECHNOLOGIES
Github
Asp.Net Core Web Api
Mongodb database to store all data

CHALLENGE

Many individuals and businesses struggle to keep track of all their income sources and expenses accurately. This can lead to overspending, missed bills, and a lack of awareness about where money is going.
Solution: A financial calculation app can automatically categorize and track all transactions by syncing with bank accounts, credit cards, and other financial institutions. It provides a clear and real-time view of spending patterns and income streams.

Limitation: While the app can provide tools and reminders, it cannot alter a user's inherent spending habits or resolve psychological issues without additional behavioral interventions or counseling.

RISKS
Potential Impact: Inability to reliably sync with banks and other financial institutions can lead to incomplete or outdated financial information.
Safeguards:
API Management: Use robust API management tools to handle connections with financial institutions.
Regular Updates: Keep integration modules updated to accommodate changes in external APIs.
Ethical Considerations
Potential Impact: Ethical issues, such as misuse of user data or manipulative practices, can harm the app's reputation and user trust.

INFRASTRUCTURE
Main Branch (main):

The main branch is the production-ready branch that contains stable code. All deployments to production are made from this branch.

Automated Builds:

Every commit to the main branch triggers an automated build process. This ensures that the codebase is always in a deployable state.
Testing:
During the build, all tests (unit, integration, and end-to-end) are executed to verify code integrity and functionality.

Initial Data Import:

Upon first deployment, the app is populated with essential data through migration scripts. These scripts ensure that the database schema is set up correctly and initial data is inserted.
API Integration:
For dynamic data, the app integrates with external APIs to fetch and update data in real-time. APIs are used for financial transactions, market data, and other relevant information.

End-to-End Testing:

End-to-end tests simulate real user scenarios from start to finish. These tests are automated using tools like Cypress or Selenium, ensuring that the entire application flow works as intended.

EXISTING SOLUTIONS
1. Mint
Similarities:
Both Mint and the proposed app focus on personal finance management.
Features include budget tracking, expense categorization, and financial goal setting.
Integration with multiple financial institutions for automatic transaction tracking.
Differences:
Mint has been established for many years and has a large user base and extensive features.
Mint includes credit score monitoring and investment tracking, which may not be available in the initial version of the proposed app.
The proposed app aims to provide a more user-friendly interface and more robust customization options.
