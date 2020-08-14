#include <iostream>
#include <string>
#include <list>
#include <cppunit/TestCase.h>
#include <cppunit/TestFixture.h>
#include <cppunit/ui/text/TextTestRunner.h>
#include <cppunit/extensions/HelperMacros.h>
#include <cppunit/extensions/TestFactoryRegistry.h>
#include <cppunit/TestResult.h>
#include <cppunit/TestResultCollector.h>
#include <cppunit/TestRunner.h>
#include <cppunit/BriefTestProgressListener.h>
#include <cppunit/CompilerOutputter.h>
#include <cppunit/XmlOutputter.h>
#include <netinet/in.h>

#include "Player.hpp"

using namespace CppUnit;
using namespace std;

class TestPlayer : public CppUnit::TestFixture
{
    CPPUNIT_TEST_SUITE(TestPlayer);
    CPPUNIT_TEST(testdisplayBoard);
    CPPUNIT_TEST(testplacePeice);
    CPPUNIT_TEST(testisBoardEmpty);
    CPPUNIT_TEST(testCheckWin);
    CPPUNIT_TEST_SUITE_END();

public:
    void setUp(void);
    void tearDown(void);

protected:
    void testdisplayBoard(void);
    void testplacePeice(void);
    void testisBoardEmpty(void);
    void testCheckWin(void);
private:
    Player *mTestObj;
};

void TestPlayer::testdisplayBoard(void){
    CPPUNIT_ASSERT(mTestObj -> displayBoard());
}
void TestPlayer::testplacePeice(void){
    CPPUNIT_ASSERT(mTestObj -> placePeice(0,0,'x') == 'x');
}
void TestPlayer::testisBoardEmpty(void){
    CPPUNIT_ASSERT(mTestObj -> isBoardClear());
}
void TestPlayer::testCheckWin(void){
    mTestObj -> placePeice(0,0,'x');
    mTestObj -> placePeice(0,1,'x');
    mTestObj -> placePeice(0,2,'x');
    CPPUNIT_ASSERT( (mTestObj -> checkWin('x') ));
}

void TestPlayer::setUp(void){
    mTestObj = new Player();
}

void TestPlayer::tearDown(){
    delete mTestObj;
}

CPPUNIT_TEST_SUITE_REGISTRATION(TestPlayer);

int main(int argc, char * argv[]){
    // informs test-listener about testresults
    CPPUNIT_NS::TestResult testresult;

    // register listener for collecting the test-results
    CPPUNIT_NS::TestResultCollector collectedresults;
    testresult.addListener (&collectedresults);

    // register listener for per-test progress output
    CPPUNIT_NS::BriefTestProgressListener progress;
    testresult.addListener (&progress);

    // insert test-suite at test-runner by registry
    CPPUNIT_NS::TestRunner testrunner;
    testrunner.addTest (CPPUNIT_NS::TestFactoryRegistry::getRegistry().makeTest ());
    testrunner.run(testresult);

    // output results in compiler-format
    CPPUNIT_NS::CompilerOutputter compileroutputter(&collectedresults, std::cerr);
    compileroutputter.write ();

    // Output XML for Jenkins CPPunit plugin
    ofstream xmlFileOut("cppTestPlayer.xml");
    XmlOutputter xmlOut(&collectedresults, xmlFileOut);
    xmlOut.write();

    // return 0 if tests were successful
    return collectedresults.wasSuccessful() ? 0 : 1;
}
