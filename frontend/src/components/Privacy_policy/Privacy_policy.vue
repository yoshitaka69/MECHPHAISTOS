<style>
.title {
    font-size: 24px;
    font-weight: bold;
    text-decoration: underline;
    color: #333; /* 読みやすい薄い黒 */
    margin-bottom: 10px; /* タイトルとコンテンツの間に余白を追加 */
}

.text-content {
    margin-left: 20px;
    font-size: 16px; /* 読みやすい大きさに変更 */
    color: #555; /* コントラストを強めた灰色 */
    line-height: 1.6; /* 行間を広げて読みやすく */
    padding-bottom: 20px; /* セクション間に余白を追加 */
}

ul, ol {
    padding-left: 40px; /* リストのインデントを調整 */
    margin-bottom: 20px; /* リストと次のコンテンツ間に余白を追加 */
}

li {
    margin-bottom: 10px; /* リスト項目間に余白を追加 */
}

p {
    margin-bottom: 15px; /* 段落間に余白を追加 */
}

.surface-section {
    background-color: #f9f9f9; /* コンテンツエリアに薄い背景色を追加 */
    padding: 20px;
    border-radius: 8px; /* コーナーを丸くしてモダンな印象に */
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); /* 軽い影を付けて立体感を出す */
}

.border-bottom-1 {
    border-bottom: 1px solid #ddd; /* セクション間に薄いボーダーを追加 */
    padding-bottom: 15px;
    margin-bottom: 30px; /* セクション間の余白を広げる */
}
</style>

<template>
    <div class="surface-section px-4 py-5 md:px-6 lg:px-8">
        <div class="flex md:align-items-center md:justify-content-between flex-column md:flex-row pb-4 border-bottom-1 surface-border">
            <div class="mb-3 lg:mb-0">
                <div class="title">Define</div>
                <br /><!-- 変更された部分 -->
                <div class="text-content">
                    The web app "MECHPHAISTOS" is based in Japan and is entirely run by Yoshitaka Noto.<br />
                    We will refer to them as "I," "we," and "our company," and refer to our customers as "USERS" and "companies."<br />
                    In addition, the applications and services provided by our company are referred to as "MECHPHAISTOS", "apps", "websites", or "services".<br /><br />

                    As a form provided by the app,<br /><br />
                    <!-- 追加されたブランク行 -->

                    <ol>
                        <li>Critical Equipment List</li>
                        <li>Repairing Cost List</li>
                        <li>NearMiss List</li>
                        <li>Spear Parts List</li>
                        <li>Energy form List</li>
                    </ol>
                </div>
            </div>
        </div>

        <div class="flex md:align-items-center md:justify-content-between flex-column md:flex-row pb-4 border-bottom-1 surface-border">
            <div class="mb-3 lg:mb-0">
                <div class="title">How does MECHPHAISTOS collect data about users?</div>
                <br />
                <div class="text-content">
                    MECHPHAISTOS collects users' data below.<br /><br />

                    <ol>
                        <li>When USERS visit a Web app MECHPHAISTOS.</li>
                        <li>When USERS create a user account, and USERS update USERS' account.</li>
                        <li>When USERS use MECHPHAISTOS in MacOS, Windows, Linux, iOS, Android.</li>
                        <li>When USERS submit support, privacy, legal, or other requests to us.</li>
                        <li>When we are working with researching current and potential customers.</li>
                        <li>When USERS post topics or comments on the form provided by MECHPHAISTOS.</li>
                        <li>In particular, MECHPHAISTOS collects USERS' equipment maintenance information, processes the information, and shares it with other USERS.</li>
                        <li>When we are researching potential customers, we may search the public World Wide Web and paid business databases.</li>
                        <li>We do not otherwise purchase or receive data about you from data brokers or other private services.</li>
                    </ol>
                </div>
            </div>
        </div>

        <div class="flex md:align-items-center md:justify-content-between flex-column md:flex-row pb-4 border-bottom-1 surface-border">
            <div class="mb-3 lg:mb-0">
                <div class="title">What data does MECHPHAISTOS collect about me and why?</div>
                <br />
                <div class="text-content">
                    <p>
                        MECHPHAISTOS lets you add equipment information, topics, comments, and attachments to various forms<br />
                        and saves them on your local device and server.<br />
                        These data are associated with your MECHPHAISTOS account.<br />
                        The saved data cannot be viewed by anyone<br />
                        other than the server administrator.<br />
                        The saved data cannot be viewed by anyone other than the server administrator.<br />
                        However, some data can be shared among various users.<br />
                        below the data<br />
                    </p>
                    <ol>
                        <li>USER's account in the same group.</li>
                        <li>Equipment information.</li>
                        <li>Equipment repairing information</li>
                    </ol>

                    <p>
                        MECHPHAISTOS stores data in local storage to provide quick offline access to the data.<br />
                        MECHPHAISTOS does not encrypt locally stored data to provide quick search functionality.<br />
                    </p>
                </div>
            </div>
        </div>

        <div class="flex md:align-items-center md:justify-content-between flex-column md:flex-row pb-4 border-bottom-1 surface-border">
            <div class="mb-3 lg:mb-0">
                <div class="title">MECHPHAISTOS collects data about how you use the MECHPHAISTOS service.</div>
                <br />
                <div class="text-content">
                    <p>
                        Network request data, such as date and time, IP address, and URL<br />
                        Number of notes, notebooks, tags, files and their total data size<br />
                    </p>
                    <ol>
                        <li>MECHPHAISTOS uses this data for the following purposes</li>
                        <li>To keep our services running quickly and reliably</li>
                        <li>To debug and develop our apps and websites</li>
                        <li>To protect MECHPHAISTOS from abuse and technical attacks</li>
                        <li>To create statistics about plugin usage and popularity</li>
                        <li>To improve search results on our website (for SEO)</li>
                        <li>To improve the usability of the MECHPHAISTOS</li>
                    </ol>
                    <p>MECHPHAISTOS typically deletes log entries containing identifiable information within a few weeks, but may retain logs longer if necessary in specific cases, such as investigating a particular incident.</p>
                </div>
            </div>
        </div>

        <div class="flex md:align-items-center md:justify-content-between flex-column md:flex-row pb-4 border-bottom-1 surface-border">
            <div class="mb-3 lg:mb-0">
                <div class="title">MECHPHAISTOS collects data about how you use our website.</div>
                <br />
                <div class="text-content">
                    <p>
                        When USERS visit the MECHPHAISTOS website, MECHPHAISTOS uses cookies, server logs, and other methods to collect data about the pages you visit. MECHPHAISTOS also collects technical information about the software and computers
                        you use, including:
                    </p>
                    <ul>
                        <li>IP addresses of users and companies</li>
                        <li>Web browser software you use</li>
                        <li>Equipment information user input</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="flex md:align-items-center md:justify-content-between flex-column md:flex-row pb-4 border-bottom-1 surface-border">
            <div class="mb-3 lg:mb-0">
                <div class="title">MECHPHAISTOS uses data about how the website is used for the following purposes.</div>
                <br />
                <div class="text-content">
                    <p>How to use MECHPHAISTOS's data.</p>
                    <ul>
                        <li>To optimize our website to make it quick and easy to use</li>
                        <li>For diagnosing and debugging technical errors</li>
                        <li>To protect our website from abuse and technical attacks</li>
                        <li>To create statistics on package popularity</li>
                        <li>To generate statistics about the types of software and computers used by our visitors</li>
                        <li>
                            To collect statistics about visitor searches and needs to guide the development of new website pages<br />
                            and features
                        </li>
                        <li>To Determine who to contact for product announcements, service changes, and new features</li>
                        <li>To disclose equipment demand information and share demand information</li>
                    </ul>

                    <p>
                        Please note that MECHPHAISTOS does not disclose personal names of users, company names, or equipment<br />
                        names that characterize specific equipment.
                    </p>

                    <p>
                        MECHPHAISTOS may retain log entries of all types of visitors for longer periods as necessary in<br />
                        specific cases, such as investigating specific incidents.<br />
                        MECHPHAISTOS stores aggregated statistics indefinitely, but those statistics do not include<br />
                        personally identifiable data.
                    </p>
                </div>
            </div>
        </div>

        <div class="flex md:align-items-center md:justify-content-between flex-column md:flex-row pb-4 border-bottom-1 surface-border">
            <div class="mb-3 lg:mb-0">
                <div class="title">MECHPHAISTOS collects account data.</div>
                <br />
                <div class="text-content">
                    <p>
                        Basically, MECHPHAISTOS services require a MECHPHAISTOS account.<br />
                        A valid email address is required to create a MECHPHAISTOS account.<br />
                        MECHPHAISTOS uses this data to provide you with access to functionality and to identify you publicly<br />
                        and within MECHPHAISTOS services. You do not need to specify your personal or business name to create<br />
                        a MECHPHAISTOS account. You can also use a pseudonym instead. You can also open multiple accounts.
                    </p>

                    <ul>
                        <li>To check whether the email address for registration is correct.</li>
                        <li>Reminds you that your free trial will expire in 3 days.</li>
                        <li>Notify me when my free trial has expired.</li>
                        <li>Notify me of a failed payment.</li>
                        <li>We will notify you that your account has been disabled due to a failed payment.</li>
                        <li>If you become a paid user, we will invite you to a lounge that is only accessible to paid users.</li>
                        <li>You will receive a 3-day notice for annual subscription renewals.</li>
                        <li>To contact you about special circumstances related to your account.</li>
                        <li>Contact us about a support request.</li>
                        <li>Contact us about legal claims such as DMCA takedown requests and privacy violations.</li>
                        <li>To contact you regarding support requests.</li>
                        <li>To contact you regarding legal claims, such as DMCA takedown requests and privacy violations.</li>
                        <li>To announce new MECHPHAISTOS products, service changes, and features.</li>
                    </ul>
                    <p>
                        MECHPHAISTOS stores your account data as long as your account is open.<br />
                        If your account data is also included in your plugin data, MECHPHAISTOS will also save that data for as long as you save the plugin.
                    </p>
                </div>
            </div>
        </div>

        <div class="flex md:align-items-center md:justify-content-between flex-column md:flex-row pb-4 border-bottom-1 surface-border">
            <div class="mb-3 lg:mb-0">
                <div class="title">MECHPHAISTOS collects payment card data.</div>
                <br />
                <div class="text-content">
                    <p>
                        To continue using the MECHPHAISTOS service after your free trial expires, MECHPHAISTOS requires<br />
                        payment card data. MECHPHAISTOS itself does not collect or store sufficient information to charge<br />
                        the card itself. Rather, Stripe collects that data on behalf of MECHPHAISTOS and provides<br />
                        MECHPHAISTOS security tokens that enable MECHPHAISTOS to create fees and subscriptions. Stripe meets<br />
                        the highest level of PCI compliance (Level 1). Please see our Security page for more information.<br />
                        MECHPHAISTOS uses payment card data only to bill you for MECHPHAISTOS services.<br />
                        MECHPHAISTOS instructs Stripe to store your payment card data for as long as you use the paid<br />
                        MECHPHAISTOS service.<br />
                        MECHPHAISTOS collects billing addresses.<br />
                        In Japan, MECHPHAISTOS services are subject to consumption tax. However, those residing outside Japan<br />
                        are exempt from consumption tax.<br />
                        MECHPHAISTOS collects your billing address to confirm whether you reside in Japan. This is required<br />
                        by the Japanese National Tax Agency.<br />
                        MECHPHAISTOS securely stores this information using Stripe.<br />
                    </p>
                </div>
            </div>
        </div>

        <div class="flex md:align-items-center md:justify-content-between flex-column md:flex-row pb-4 border-bottom-1 surface-border">
            <div class="mb-3 lg:mb-0">
                <div class="title">MECHPHAISTOS collects data regarding communications.</div>
                <br />
                <div class="text-content">
                    <p>
                        MECHPHAISTOS collects data about you when you submit MECHPHAISTOS support requests, legal<br />
                        complaints, privacy inquiries, and business inquiries. This data typically includes your name and<br />
                        email address, but may also include your company and other affiliations.<br />
                    </p>

                    <p>MECHPHAISTOS uses USER's contact data for the following purposes:</p>
                    <ul>
                        <li>To respond to you.</li>
                        <li>To create aggregate statistics about responses.</li>
                        <li>To Protect MECHPHAISTOS from legal claims.</li>
                        <li>MECHPHAISTOS will store communications for as long as they serve these purposes.</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="flex md:align-items-center md:justify-content-between flex-column md:flex-row pb-4 border-bottom-1 surface-border">
            <div class="mb-3 lg:mb-0">
                <div class="title">Where does MECHPHAISTOS store data about me?</div>
                <br />
                <div class="text-content">
                    <p>
                        MECHPHAISTOS stores account data, notes data, website usage data, and plug-ins on servers in the<br />
                        United States.<br />
                        I sometimes import those data to my Japanese computer.<br />
                        I use the data to develop, debug, and maintain my services.<br />
                        Data is erased from your computer when it is no longer needed.<br />
                    </p>
                </div>
            </div>
        </div>

        <div class="flex md:align-items-center md:justify-content-between flex-column md:flex-row pb-4 border-bottom-1 surface-border">
            <div class="mb-3 lg:mb-0">
                <div class="title">Is MECHPHAISTOS compliant with the EU General Data Protection Regulation?</div>
                <br />
                <div class="text-content">
                    <p>
                        MECHPHAISTOS respects your right to privacy under Regulation (EU) 2016/679, the European Union's<br />
                        General Data Protection Regulation (GDPR).<br />
                        The information that MECHPHAISTOS is required to provide under the GDPR is provided throughout our privacy questions and answers.<br />
                        As well as information regarding specific rights, such as access, rectification, erasure, data portability, and objecting to<br />
                        automated decision-making.<br />
                        GDPR does not apply to everyone worldwide.<br />
                        However, MECHPHAISTOS's policy is to do our best to provide the same privacy information, controls, and protections to all users,<br />
                        regardless of whether GDPR applies or not.<br />
                    </p>
                </div>
            </div>
        </div>

        <div class="flex md:align-items-center md:justify-content-between flex-column md:flex-row pb-4 border-bottom-1 surface-border">
            <div class="mb-3 lg:mb-0">
                <div class="title">How can I access data about me?</div>
                <br />
                <div class="text-content">You can access your account data at any time by visiting your MECHPHAISTOS's account page.</div>
            </div>
        </div>

        <div class="flex md:align-items-center md:justify-content-between flex-column md:flex-row pb-4 border-bottom-1 surface-border">
            <div class="mb-3 lg:mb-0">
                <div class="title">How can I change or erase data about me?</div>
                <div class="text-content">
                    <p>
                        MECHPHAISTOS shares equipment maintenance information and risk assessment data such as near misses<br />
                        with other users.<br />
                        However, we do not disclose or share any specific information that could identify<br />
                        your company.<br />
                        MECHPHAISTOS does not sell information that identifies you to others.<br />
                        However, information about demand and trends for parts will be provided to external companies for<br />
                        commercial purposes while maintaining anonymity.<br />
                    </p>
                </div>
            </div>
        </div>

        <div class="flex md:align-items-center md:justify-content-between flex-column md:flex-row pb-4 border-bottom-1 surface-border">
            <div class="mb-3 lg:mb-0">
                <div class="title">Does MECHPHAISTOS share data about me with others?</div>
                <br />
                <div class="text-content">
                    <p>
                        MECHPHAISTOS shares equipment maintenance information and risk assessment data such as near misses<br />
                        with other users.<br />
                        However, we do not disclose or share any specific information that could identify<br />
                        your company.<br />
                        MECHPHAISTOS does not sell information that identifies you to others.<br />
                        However, information about demand and trends for parts will be provided to external companies for<br />
                        commercial purposes while maintaining anonymity.<br />
                    </p>
                </div>
            </div>
        </div>

        <div class="flex md:align-items-center md:justify-content-between flex-column md:flex-row pb-4 border-bottom-1 surface-border">
            <div class="mb-3 lg:mb-0">
                <div class="title">MECHPHAISTOS uses services provided by other companies to provide</div>
                <br />
                <div class="text-content">
                    <p>
                        Some of these services may independently collect data about you for their own purposes.<br />
                        Some of these services may be used to collect information about your online activities across<br />
                        various websites, and we provide details about those websites below.<br />
                    </p>

                    <p>MECHPHAISTOS uses a cloud computing platform:</p>
                    <ul>
                        <li>MECHPHAISTOS uses Amazon Web Services servers and services in service regions around the world to power the MECHPHAISTOS service. You can read the AWS Privacy Policy online.</li>
                        <li>MECHPHAISTOS uses Heroku servers and services in the United States service region to power the MECHPHAISTOS service. You can read Heroku's privacy policy online.</li>
                        <li>MECHPHAISTOS uses Stripe.</li>
                        <li>MECHPHAISTOS uses Stripe to collect and use card payment data and billing information. Stripe's privacy policy is available online.</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="flex md:align-items-center md:justify-content-between flex-column md:flex-row pb-4 border-bottom-1 surface-border">
            <div class="mb-3 lg:mb-0">
                <div class="title">Who do I contact about MECHPHAISTOS and my privacy?</div>
                <div class="text-content">
                    <p>
                        Questions or complaints can be directed to:<br /><br />
                        Name: Yoshitaka Noto<br />
                        e-mail: Yoshitaka.noto@rond-tech.com<br />
                        address: 472-1 La Terre room103<br />
                        Toyama prefecture, Toyama city, Kurosaki 472-1<br />
                        zip-code: 939-8214<br />
                        country: Japan<br />
                    </p>
                </div>
            </div>
        </div>

        <div class="flex md:align-items-center md:justify-content-between flex-column md:flex-row pb-4 border-bottom-1 surface-border">
            <div class="mb-3 lg:mb-0">
                <div class="title">How can I see the changes?</div>
                <br />
                <div class="text-content">
                    <p>
                        MECHPHAISTOS announces the next version on the MECHPHAISTOS blog.<br />
                        In the meantime, MECHPHAISTOS may update contact information or minor changes by updating the Privacy Policy page without announcement.<br />
                        MECHPHAISTOS may change the way it announces changes in future privacy versions.<br />
                        You can check the change history of the MECHPHAISTOS documentation Git repository.<br />
                    </p>
                </div>
            </div>
        </div>

        <div class="flex md:align-items-center md:justify-content-between flex-column md:flex-row pb-4 border-bottom-1 surface-border">
            <div class="mb-3 lg:mb-0">
                <div class="title">About advertising</div>
                <br />
                <div class="text-content">
                    <p>
                        This blog uses third-party advertising services (Google AdSense, A8.net) and uses cookies to display<br />
                        advertisements for products and services that match the interests of users.<br />
                        Cookies allow this site to identify your computer, but they do not allow us to identify you personally.<br />
                        For more information on how to disable cookies and Google AdSense, please see "Advertising - Policies and Terms -<br />
                        Google".<br />
                        MECHPHAISTOS is also a participant in the Amazon Services LLC Associates Program, an affiliate<br />
                        advertising program designed to provide a means for sites to earn advertising fees by advertising<br />
                        and linking to Amazon.co.jp.<br />
                    </p>
                </div>
            </div>
        </div>

        <div class="flex md:align-items-center md:justify-content-between flex-column md:flex-row pb-4 border-bottom-1 surface-border">
            <div class="mb-3 lg:mb-0">
                <div class="title">About access analysis tools</div>
                <br />
                <div class="text-content">This blog uses Google's access analysis tool "Google Analytics."This Google Analytics uses cookies to collect traffic data. Traffic data is collected anonymously and does not personally identify you.</div>
            </div>
        </div>
    </div>
</template>
