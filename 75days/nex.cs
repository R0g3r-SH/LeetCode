using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using UnityEngine.UI;
public class GetApiData : MonoBehaviour
{
public string URL;
public InputField id;
public GameObject playerStatusPanel;
public void GetData()



{
StartCoroutine(FetchData());
}
public IEnumerator FetchData()
{
using (UnityWebRequest request = UnityWebRequest.Get(URL + id.text))
{
yield return request.SendWebRequest();
if (request.result == UnityWebRequest.Result.ConnectionError)
{
Debug.Log(request.error);
}
else
{
PlayerStatus playerStat = new PlayerStatus();
playerStat = JsonUtility.FromJson<PlayerStatus>(request.downloadHandler.text);
playerStatusPanel.transform.GetChild(0).GetComponent<Text>().text = playerStat.playerName;
playerStatusPanel.transform.GetChild(1).GetComponent<Text>().text = "HP : " + playerStat.hp.ToString();
playerStatusPanel.transform.GetChild(2).GetComponent<Text>().text = "MP : " + playerStat.mp.ToString();
playerStatusPanel.transform.GetChild(3).GetComponent<Text>().text = "Attack : " + playerStat.atk.ToString();
playerStatusPanel.transform.GetChild(4).GetComponent<Text>().text = "Defende : " + playerStat.def.ToString();
playerStatusPanel.transform.GetChild(5).GetComponent<Text>().text = "Agility : " + playerStat.agi.ToString();
}
}
}
}